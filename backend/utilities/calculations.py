"""
Utility functions for policy impact calculations
"""
import math

def calculate_pay_gap_reduction(policy_type, percentage, year, duration):
    """
    Calculate pay gap reduction over time
    
    Args:
        policy_type: Type of policy (equal_pay, leadership_quota, parental_leave)
        percentage: Policy strength (0-100)
        year: Current year in simulation (0-duration)
        duration: Total simulation duration
    
    Returns:
        Pay gap reduction percentage
    """
    base_gap = 23.0  # Starting gender pay gap percentage
    
    # Different policies have different effectiveness curves
    if policy_type == "equal_pay":
        # Direct impact, faster reduction
        reduction_rate = (percentage / 100) * 0.35
        reduction = base_gap * (1 - math.exp(-reduction_rate * year))
    elif policy_type == "leadership_quota":
        # Gradual impact through representation
        reduction_rate = (percentage / 100) * 0.25
        reduction = base_gap * (1 - math.exp(-reduction_rate * year * 0.8))
    elif policy_type == "parental_leave":
        # Slower but steady impact
        reduction_rate = (percentage / 100) * 0.20
        reduction = base_gap * (1 - math.exp(-reduction_rate * year * 0.6))
    else:
        reduction = 0
    
    # Cap reduction at 90% of original gap
    return min(reduction, base_gap * 0.9)


def calculate_employment_ratio(policy_type, percentage, year, duration):
    """
    Calculate employment ratio change (women/men)
    
    Returns:
        Employment ratio (baseline is 0.82)
    """
    base_ratio = 0.82
    target_ratio = 0.95  # Near parity
    
    if policy_type == "equal_pay":
        improvement_rate = (percentage / 100) * 0.15
    elif policy_type == "leadership_quota":
        improvement_rate = (percentage / 100) * 0.18
    elif policy_type == "parental_leave":
        improvement_rate = (percentage / 100) * 0.22
    else:
        improvement_rate = 0.1
    
    # Sigmoid curve for realistic growth
    improvement = (target_ratio - base_ratio) * (1 / (1 + math.exp(-0.5 * (year - duration/2))))
    return base_ratio + (improvement * improvement_rate)


def calculate_leadership_distribution(policy_type, percentage, year, duration):
    """
    Calculate leadership gender distribution
    
    Returns:
        Dictionary with male and female percentages
    """
    base_female = 30.0  # Starting percentage of female leaders
    
    if policy_type == "leadership_quota":
        # Direct quota impact
        target_increase = percentage * 0.6
        current_increase = target_increase * (year / duration)
    elif policy_type == "equal_pay":
        # Indirect impact
        target_increase = percentage * 0.3
        current_increase = target_increase * (year / duration) * 0.7
    elif policy_type == "parental_leave":
        # Moderate indirect impact
        target_increase = percentage * 0.25
        current_increase = target_increase * (year / duration) * 0.6
    else:
        current_increase = 0
    
    female_percentage = min(base_female + current_increase, 65.0)  # Cap at 65%
    male_percentage = 100 - female_percentage
    
    return {
        "female": round(female_percentage, 1),
        "male": round(male_percentage, 1)
    }


def calculate_budget_impact(policy_type, percentage, budget, year, duration):
    """
    Calculate cumulative budget spending
    
    Returns:
        Budget spent up to current year
    """
    yearly_cost_rate = {
        "equal_pay": 1.2,
        "leadership_quota": 0.8,
        "parental_leave": 1.5
    }
    
    rate = yearly_cost_rate.get(policy_type, 1.0)
    intensity_factor = percentage / 100
    
    # Spending ramps up in early years, stabilizes later
    if year <= duration * 0.3:
        yearly_spend = (budget / duration) * rate * intensity_factor * 1.3
    else:
        yearly_spend = (budget / duration) * rate * intensity_factor
    
    return yearly_spend * year


def calculate_risk_level(policy_type, percentage, budget, duration):
    """
    Calculate overall risk level of policy
    
    Returns:
        Risk score (0-100) and level (low/medium/high)
    """
    # Risk factors
    budget_risk = min((budget / 10000000) * 20, 30)  # Budget over 10M increases risk
    intensity_risk = (percentage / 100) * 25  # Higher percentage = higher risk
    duration_risk = max(0, (duration - 5) * 5)  # Longer duration = higher uncertainty
    
    # Policy-specific risk modifiers
    policy_risk_modifier = {
        "equal_pay": 1.0,  # Moderate risk
        "leadership_quota": 1.2,  # Higher political risk
        "parental_leave": 0.9   # Lower risk, proven policy
    }
    
    modifier = policy_risk_modifier.get(policy_type, 1.0)
    total_risk = (budget_risk + intensity_risk + duration_risk) * modifier
    
    # Normalize to 0-100
    risk_score = min(total_risk, 100)
    
    if risk_score < 30:
        level = "low"
    elif risk_score < 60:
        level = "medium"
    else:
        level = "high"
    
    return {
        "score": round(risk_score, 1),
        "level": level
    }


def format_currency(amount):
    """Format currency for display"""
    if amount >= 1000000:
        return f"${amount/1000000:.1f}M"
    elif amount >= 1000:
        return f"${amount/1000:.0f}K"
    else:
        return f"${amount:.0f}"