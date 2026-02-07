"""
AI-powered explanation service for simulation results
Converts technical data into human-readable insights
"""

def explain_simulation_results(simulation_results):
    """
    Generate a simple, human-readable explanation of simulation results
    
    Args:
        simulation_results: Dictionary containing simulation data
    
    Returns:
        Human-friendly explanation text
    """
    policy = simulation_results["policy"]
    final = simulation_results["final_metrics"]
    risk = simulation_results["risk"]
    
    # Build explanation
    explanation_parts = []
    
    # Introduction
    intro = f"Your {policy['type_name']} simulation shows "
    
    # Pay gap impact
    pay_gap_reduction = final["pay_gap_reduction"]
    if pay_gap_reduction > 15:
        pay_impact = f"**strong progress** in reducing the gender pay gap by {pay_gap_reduction:.1f} percentage points over {policy['duration']} years. "
    elif pay_gap_reduction > 8:
        pay_impact = f"**moderate progress** in reducing the gender pay gap by {pay_gap_reduction:.1f} percentage points over {policy['duration']} years. "
    else:
        pay_impact = f"**limited progress** in reducing the gender pay gap by {pay_gap_reduction:.1f} percentage points over {policy['duration']} years. "
    
    explanation_parts.append(intro + pay_impact)
    
    # What this means in practice
    if final["final_pay_gap"] < 10:
        practical = "This means women would earn nearly the same as men for similar work - a major achievement for workplace equality."
    elif final["final_pay_gap"] < 15:
        practical = "This means the pay gap would narrow significantly, though some inequality would remain."
    else:
        practical = "This means progress is being made, but substantial pay inequality would still exist."
    
    explanation_parts.append(practical)
    
    # Employment impact
    employment_change = final["employment_improvement"]
    if employment_change > 8:
        employment_text = f"\n\nThe policy would also **boost women's employment** by {employment_change:.1f}%, helping more women participate in the workforce."
    elif employment_change > 3:
        employment_text = f"\n\nThe policy would **moderately increase women's employment** by {employment_change:.1f}%."
    else:
        employment_text = f"\n\nThe policy would have a **small effect on employment** ({employment_change:.1f}% increase)."
    
    explanation_parts.append(employment_text)
    
    # Leadership impact
    female_leadership = final["final_leadership"]["female"]
    if female_leadership > 45:
        leadership_text = f" Women would hold {female_leadership:.0f}% of leadership positions, achieving near-parity in organizational leadership."
    elif female_leadership > 38:
        leadership_text = f" Women would hold {female_leadership:.0f}% of leadership positions, a significant improvement from today's 30%."
    else:
        leadership_text = f" Women would hold {female_leadership:.0f}% of leadership positions, showing modest gains in leadership representation."
    
    explanation_parts.append(leadership_text)
    
    # Budget consideration
    budget_spent = final["total_budget_spent"]
    budget_per_year = budget_spent / policy["duration"]
    
    if budget_per_year > 1000000:
        budget_text = f"\n\n**Budget Impact:** This policy costs ${budget_spent:,.0f} total (${budget_per_year:,.0f} per year) - a substantial investment that requires secure funding."
    elif budget_per_year > 500000:
        budget_text = f"\n\n**Budget Impact:** This policy costs ${budget_spent:,.0f} total (${budget_per_year:,.0f} per year) - a moderate investment with manageable costs."
    else:
        budget_text = f"\n\n**Budget Impact:** This policy costs ${budget_spent:,.0f} total (${budget_per_year:,.0f} per year) - a relatively affordable intervention."
    
    explanation_parts.append(budget_text)
    
    # Risk assessment
    if risk["level"] == "low":
        risk_text = f"\n\n**Risk Level: {risk['level'].upper()} ({risk['score']:.0f}/100)** - This policy has strong chances of success with minimal implementation challenges."
    elif risk["level"] == "medium":
        risk_text = f"\n\n**Risk Level: {risk['level'].upper()} ({risk['score']:.0f}/100)** - This policy has reasonable chances of success but may face some implementation challenges."
    else:
        risk_text = f"\n\n**Risk Level: {risk['level'].upper()} ({risk['score']:.0f}/100)** - This policy is ambitious and may face significant political or practical challenges."
    
    explanation_parts.append(risk_text)
    
    # Bottom line
    if pay_gap_reduction > 12 and risk["level"] != "high":
        bottom_line = "\n\n**Bottom Line:** This policy offers strong potential for meaningful change with acceptable risks and costs."
    elif pay_gap_reduction > 8:
        bottom_line = "\n\n**Bottom Line:** This policy would make steady progress toward gender equality, though results take time."
    else:
        bottom_line = "\n\n**Bottom Line:** This policy would contribute to gender equality but may need to be combined with other interventions for major impact."
    
    explanation_parts.append(bottom_line)
    
    return "".join(explanation_parts)


def explain_comparison(comparison_results):
    """
    Generate explanation for policy comparison
    
    Args:
        comparison_results: Dictionary with comparison data
    
    Returns:
        Human-friendly comparison explanation
    """
    analysis = comparison_results["analysis"]
    
    explanation = "**Comparing Your Two Policy Options:**\n\n"
    
    # Add recommendations
    for rec in analysis["recommendations"]:
        explanation += f"• {rec}\n"
    
    explanation += f"\n{analysis['overall_recommendation']}"
    
    # Add specific guidance
    metrics = analysis["metrics_comparison"]
    
    if metrics["pay_gap_reduction_diff"] > 5:
        explanation += "\n\n💡 **Key Insight:** The pay gap reduction difference is significant - prioritize the policy with stronger impact if equality is the primary goal."
    
    if metrics["budget_diff"] > 1000000:
        explanation += "\n\n💰 **Budget Note:** There's a major cost difference between these policies. Consider whether the additional spending justifies the extra benefits."
    
    return explanation


def get_policy_insights(policy_type):
    """
    Get general insights about a policy type
    
    Args:
        policy_type: Type of policy
    
    Returns:
        Dictionary with policy insights
    """
    insights = {
        "equal_pay": {
            "quick_summary": "Direct approach to closing wage gaps by mandating equal pay for equal work",
            "strengths": ["Fast impact on pay equity", "Clear measurable outcomes", "Strong public support"],
            "challenges": ["Enforcement complexity", "Defining 'equal work'", "Employer resistance"],
            "best_for": "Organizations ready for immediate pay equity changes"
        },
        "leadership_quota": {
            "quick_summary": "Ensures minimum representation of women in leadership positions",
            "strengths": ["Increases role models", "Systemic culture change", "Long-term structural impact"],
            "challenges": ["Political controversy", "Slow to show results", "Implementation resistance"],
            "best_for": "Long-term organizational transformation"
        },
        "parental_leave": {
            "quick_summary": "Extended paid leave for all parents to support work-life balance",
            "strengths": ["Proven effectiveness", "Supports retention", "Low political risk"],
            "challenges": ["High cost", "Slower impact", "Requires cultural shift"],
            "best_for": "Organizations focused on family support and retention"
        }
    }
    
    return insights.get(policy_type, {})