"""
Generate realistic simulation data
"""
from utilities.calculations import (
    calculate_pay_gap_reduction,
    calculate_employment_ratio,
    calculate_leadership_distribution,
    calculate_budget_impact
)

def generate_simulation_data(policy_type, percentage, duration, budget):
    """
    Generate complete simulation data over time
    
    Returns:
        Dictionary with timeline data for all metrics
    """
    years = list(range(duration + 1))
    
    # Initialize data structures
    pay_gap_data = []
    employment_data = []
    leadership_data = []
    budget_data = []
    
    base_pay_gap = 23.0
    
    for year in years:
        # Calculate pay gap
        reduction = calculate_pay_gap_reduction(policy_type, percentage, year, duration)
        current_gap = base_pay_gap - reduction
        pay_gap_data.append(round(current_gap, 2))
        
        # Calculate employment ratio
        ratio = calculate_employment_ratio(policy_type, percentage, year, duration)
        employment_data.append(round(ratio, 3))
        
        # Calculate leadership distribution
        leadership = calculate_leadership_distribution(policy_type, percentage, year, duration)
        leadership_data.append(leadership)
        
        # Calculate budget impact
        spent = calculate_budget_impact(policy_type, percentage, budget, year, duration)
        budget_data.append(round(spent, 2))
    
    return {
        "years": years,
        "pay_gap": pay_gap_data,
        "employment_ratio": employment_data,
        "leadership": leadership_data,
        "budget_spent": budget_data,
        "duration": duration
    }


def get_final_metrics(simulation_data):
    """
    Extract final year metrics from simulation data
    
    Returns:
        Dictionary with end-state metrics
    """
    final_index = -1
    
    return {
        "final_pay_gap": simulation_data["pay_gap"][final_index],
        "pay_gap_reduction": round(23.0 - simulation_data["pay_gap"][final_index], 2),
        "final_employment_ratio": simulation_data["employment_ratio"][final_index],
        "employment_improvement": round(
            (simulation_data["employment_ratio"][final_index] - 0.82) * 100, 2
        ),
        "final_leadership": simulation_data["leadership"][final_index],
        "total_budget_spent": simulation_data["budget_spent"][final_index]
    }