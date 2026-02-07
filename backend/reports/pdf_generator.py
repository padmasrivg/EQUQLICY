"""
PDF Report Generator for simulation results
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.pdfgen import canvas
from datetime import datetime
import io


class PDFReportGenerator:
    """Generate professional PDF reports for policy simulations"""
    
    def __init__(self):
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#34495E'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Body text style
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=11,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=12,
            fontName='Helvetica'
        ))
    
    def generate_simulation_report(self, simulation_results, explanation_text):
        """
        Generate PDF report for a single simulation
        
        Args:
            simulation_results: Simulation results dictionary
            explanation_text: AI-generated explanation
        
        Returns:
            PDF file as bytes
        """
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter,
                              topMargin=0.75*inch, bottomMargin=0.75*inch)
        
        # Container for document elements
        elements = []
        
        # Title
        title = Paragraph(
            "EQUQLICY: Gender Policy Impact Report",
            self.styles['CustomTitle']
        )
        elements.append(title)
        elements.append(Spacer(1, 0.2*inch))
        
        # Metadata
        policy = simulation_results["policy"]
        date_generated = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        
        metadata_text = f"<b>Generated:</b> {date_generated}<br/>"
        metadata_text += f"<b>Policy Name:</b> {policy['name']}<br/>"
        metadata_text += f"<b>Policy Type:</b> {policy['type_name']}"
        
        metadata = Paragraph(metadata_text, self.styles['CustomBody'])
        elements.append(metadata)
        elements.append(Spacer(1, 0.3*inch))
        
        # Policy Details Section
        elements.append(Paragraph("Policy Configuration", self.styles['SectionHeader']))
        
        policy_details = [
            ['Parameter', 'Value'],
            ['Policy Type', policy['type_name']],
            ['Policy Strength', f"{policy['percentage']}%"],
            ['Duration', f"{policy['duration']} years"],
            ['Total Budget', f"${policy['budget']:,.0f}"],
            ['Description', policy['description']]
        ]
        
        policy_table = Table(policy_details, colWidths=[2.5*inch, 4*inch])
        policy_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498DB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        elements.append(policy_table)
        elements.append(Spacer(1, 0.3*inch))
        
        # Key Results Section
        elements.append(Paragraph("Key Results", self.styles['SectionHeader']))
        
        final = simulation_results["final_metrics"]
        risk = simulation_results["risk"]
        
        results_data = [
            ['Metric', 'Value', 'Impact'],
            ['Pay Gap Reduction', f"{final['pay_gap_reduction']:.1f}%", 
             self._get_impact_label(final['pay_gap_reduction'], 'pay_gap')],
            ['Final Pay Gap', f"{final['final_pay_gap']:.1f}%", ''],
            ['Employment Ratio Increase', f"{final['employment_improvement']:.1f}%",
             self._get_impact_label(final['employment_improvement'], 'employment')],
            ['Female Leadership', f"{final['final_leadership']['female']:.1f}%", ''],
            ['Total Budget Spent', f"${final['total_budget_spent']:,.0f}", ''],
            ['Risk Level', f"{risk['level'].upper()} ({risk['score']:.0f}/100)",
             self._get_risk_color(risk['level'])]
        ]
        
        results_table = Table(results_data, colWidths=[2.5*inch, 2*inch, 1.5*inch])
        results_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2ECC71')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ]))
        
        elements.append(results_table)
        elements.append(Spacer(1, 0.3*inch))
        
        # Timeline Data Summary
        elements.append(Paragraph("Timeline Summary", self.styles['SectionHeader']))
        
        timeline = simulation_results["timeline"]
        timeline_text = f"<b>Year 0 (Baseline):</b> Pay Gap = {timeline['pay_gap'][0]:.1f}%<br/>"
        timeline_text += f"<b>Year {policy['duration']} (Final):</b> Pay Gap = {timeline['pay_gap'][-1]:.1f}%<br/>"
        timeline_text += f"<b>Total Improvement:</b> {timeline['pay_gap'][0] - timeline['pay_gap'][-1]:.1f} percentage points"
        
        timeline_para = Paragraph(timeline_text, self.styles['CustomBody'])
        elements.append(timeline_para)
        elements.append(Spacer(1, 0.3*inch))
        
        # AI Explanation Section
        elements.append(Paragraph("AI Analysis & Insights", self.styles['SectionHeader']))
        
        # Clean up explanation text for PDF
        clean_explanation = explanation_text.replace('**', '<b>').replace('**', '</b>')
        clean_explanation = clean_explanation.replace('\n\n', '<br/><br/>')
        
        explanation_para = Paragraph(clean_explanation, self.styles['CustomBody'])
        elements.append(explanation_para)
        elements.append(Spacer(1, 0.3*inch))
        
        # Footer note
        footer_text = "<i>This report was generated by PolicySim, an AI-powered gender policy impact simulator. " \
                     "Results are based on statistical models and should be used as guidance alongside expert consultation.</i>"
        footer = Paragraph(footer_text, self.styles['CustomBody'])
        elements.append(Spacer(1, 0.2*inch))
        elements.append(footer)
        
        # Build PDF
        doc.build(elements)
        
        # Get PDF data
        pdf_data = buffer.getvalue()
        buffer.close()
        
        return pdf_data
    
    def _get_impact_label(self, value, metric_type):
        """Get impact label based on value"""
        if metric_type == 'pay_gap':
            if value > 15:
                return "Strong"
            elif value > 8:
                return "Moderate"
            else:
                return "Limited"
        elif metric_type == 'employment':
            if value > 8:
                return "High"
            elif value > 3:
                return "Moderate"
            else:
                return "Low"
        return ""
    
    def _get_risk_color(self, risk_level):
        """Get risk level descriptor"""
        if risk_level == "low":
            return "✓ Manageable"
        elif risk_level == "medium":
            return "⚠ Moderate"
        else:
            return "⚠ High"


# Create singleton instance
pdf_generator = PDFReportGenerator()