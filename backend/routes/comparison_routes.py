"""
Routes for policy comparison operations
"""
from flask import Blueprint, request, jsonify, send_file
from services.simulation_engine import simulation_engine
from services.ai_explainer import explain_comparison
from reports.pdf_generator import pdf_generator
import io

comparison_bp = Blueprint('comparison', __name__)


@comparison_bp.route('/api/compare', methods=['POST'])
def compare_policies():
    """
    Compare two policy configurations
    
    Expected JSON body:
    {
        "policy_a": {
            "policy_type": "equal_pay",
            "percentage": 75,
            "duration": 5,
            "budget": 2000000,
            "policy_name": "Policy A"
        },
        "policy_b": {
            "policy_type": "leadership_quota",
            "percentage": 40,
            "duration": 7,
            "budget": 1500000,
            "policy_name": "Policy B"
        }
    }
    """
    try:
        data = request.get_json()
        
        policy_a = data.get('policy_a')
        policy_b = data.get('policy_b')
        
        if not policy_a or not policy_b:
            return jsonify({
                'error': 'Both policy_a and policy_b are required'
            }), 400
        
        # Run comparison
        comparison_results = simulation_engine.compare_policies(policy_a, policy_b)
        
        # Generate explanation
        explanation = explain_comparison(comparison_results)
        
        return jsonify({
            'success': True,
            'data': comparison_results,
            'explanation': explanation
        }), 200
        
    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'error': f'Comparison failed: {str(e)}'
        }), 500


@comparison_bp.route('/api/download-report', methods=['POST'])
def download_report():
    """
    Generate and download PDF report for simulation
    
    Expected JSON body:
    {
        "simulation_results": { ... },
        "explanation": "..."
    }
    """
    try:
        data = request.get_json()
        
        simulation_results = data.get('simulation_results')
        explanation = data.get('explanation', '')
        
        if not simulation_results:
            return jsonify({
                'error': 'Missing simulation_results'
            }), 400
        
        # Generate PDF
        pdf_bytes = pdf_generator.generate_simulation_report(
            simulation_results,
            explanation
        )
        
        # Create file-like object
        pdf_buffer = io.BytesIO(pdf_bytes)
        pdf_buffer.seek(0)
        
        # Generate filename
        policy_name = simulation_results['policy']['name'].replace(' ', '_')
        filename = f"PolicySim_{policy_name}_Report.pdf"
        
        return send_file(
            pdf_buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )
        
    except Exception as e:
        return jsonify({
            'error': f'PDF generation failed: {str(e)}'
        }), 500