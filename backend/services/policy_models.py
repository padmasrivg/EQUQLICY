"""
Policy models and configurations
"""

POLICY_TYPES = {
    "equal_pay": {
        "name": "Equal Pay Policy",
        "description": "Mandates equal pay for equal work across gender lines",
        "min_percentage": 50,
        "max_percentage": 100,
        "typical_budget_range": [500000, 5000000],
        "effectiveness": "high",
        "time_to_impact": "medium",
        "political_difficulty": "medium"
    },
    "leadership_quota": {
        "name": "Leadership Quota",
        "description": "Requires minimum percentage of women in leadership positions",
        "min_percentage": 30,
        "max_percentage": 50,
        "typical_budget_range": [300000, 3000000],
        "effectiveness": "medium",
        "time_to_impact": "long",
        "political_difficulty": "high"
    },
    "parental_leave": {
        "name": "Parental Leave Expansion",
        "description": "Extended paid parental leave for both parents",
        "min_percentage": 50,
        "max_percentage": 100,
        "typical_budget_range": [1000000, 10000000],
        "effectiveness": "medium",
        "time_to_impact": "long",
        "political_difficulty": "low"
    }
}


def get_policy_info(policy_type):
    """Get information about a policy type"""
    return POLICY_TYPES.get(policy_type, None)


def validate_policy_parameters(policy_type, percentage, duration, budget):
    """
    Validate policy parameters
    
    Returns:
        Tuple of (is_valid, error_message)
    """
    if policy_type not in POLICY_TYPES:
        return False, f"Invalid policy type: {policy_type}"
    
    policy_info = POLICY_TYPES[policy_type]
    
    if percentage < policy_info["min_percentage"] or percentage > policy_info["max_percentage"]:
        return False, f"Percentage must be between {policy_info['min_percentage']} and {policy_info['max_percentage']}"
    
    if duration < 1 or duration > 10:
        return False, "Duration must be between 1 and 10 years"
    
    if budget < 0:
        return False, "Budget must be positive"
    
    return True, None


def get_policy_recommendations(policy_type, percentage, budget):
    """
    Get recommendations for policy implementation
    
    Returns:
        List of recommendation strings
    """
    recommendations = []
    policy_info = POLICY_TYPES[policy_type]
    
    # Budget recommendations
    min_budget, max_budget = policy_info["typical_budget_range"]
    if budget < min_budget:
        recommendations.append(
            f"⚠️ Budget is below typical range. Consider increasing to at least ${min_budget:,}"
        )
    elif budget > max_budget:
        recommendations.append(
            "💡 Budget is generous. Ensure proper allocation mechanisms are in place"
        )
    
    # Percentage recommendations
    if percentage < 70 and policy_type == "equal_pay":
        recommendations.append(
            "📊 For equal pay policies, higher percentages (70-100%) show stronger impact"
        )
    
    if percentage > 40 and policy_type == "leadership_quota":
        recommendations.append(
            "⚖️ High quotas may face political resistance. Consider phased implementation"
        )
    
    # General recommendations
    if policy_info["political_difficulty"] == "high":
        recommendations.append(
            "🤝 This policy typically faces political challenges. Build coalition support early"
        )
    
    return recommendations