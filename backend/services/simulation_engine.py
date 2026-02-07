"""
Core simulation engine for policy impact modeling
"""
from utilities.data_generator import generate_simulation_data, get_final_metrics
from utilities.calculations import calculate_risk_level
from services.policy_models import get_policy_info, validate_policy_parameters


class SimulationEngine:
    """Main simulation engine for policy impact analysis"""
    
    def __init__(self):
        self.current_simulation = None
    
    def run_simulation(self, policy_type, percentage, duration, budget, policy_name="Unnamed Policy"):
        """
        Run a complete policy simulation
        
        Args:
            policy_type: Type of policy (equal_pay, leadership_quota, parental_leave)
            percentage: Policy strength (0-100)
            duration: Simulation duration in years (1-10)
            budget: Total budget allocated
            policy_name: Custom name for the policy
        
        Returns:
            Complete simulation results dictionary
        """
        # Validate parameters
        is_valid, error = validate_policy_parameters(policy_type, percentage, duration, budget)
        if not is_valid:
            raise ValueError(error)
        
        # Get policy information
        policy_info = get_policy_info(policy_type)
        
        # Generate simulation data
        simulation_data = generate_simulation_data(policy_type, percentage, duration, budget)
        
        # Calculate risk
        risk = calculate_risk_level(policy_type, percentage, budget, duration)
        
        # Get final metrics
        final_metrics = get_final_metrics(simulation_data)
        
        # Compile results
        results = {
            "policy": {
                "name": policy_name,
                "type": policy_type,
                "type_name": policy_info["name"],
                "description": policy_info["description"],
                "percentage": percentage,
                "duration": duration,
                "budget": budget
            },
            "timeline": simulation_data,
            "final_metrics": final_metrics,
            "risk": risk,
            "timestamp": self._get_timestamp()
        }
        
        self.current_simulation = results
        return results
    
    def compare_policies(self, policy_a_params, policy_b_params):
        """
        Compare two policy configurations
        
        Args:
            policy_a_params: Dictionary with policy A parameters
            policy_b_params: Dictionary with policy B parameters
        
        Returns:
            Comparison results with recommendations
        """
        # Run both simulations
        sim_a = self.run_simulation(**policy_a_params)
        sim_b = self.run_simulation(**policy_b_params)
        
        # Compare key metrics
        comparison = {
            "policy_a": sim_a,
            "policy_b": sim_b,
            "analysis": self._analyze_comparison(sim_a, sim_b)
        }
        
        return comparison
    
    def _analyze_comparison(self, sim_a, sim_b):
        """Analyze differences between two simulations"""
        
        # Compare pay gap reduction
        pay_gap_a = sim_a["final_metrics"]["pay_gap_reduction"]
        pay_gap_b = sim_b["final_metrics"]["pay_gap_reduction"]
        
        # Compare budget
        budget_a = sim_a["final_metrics"]["total_budget_spent"]
        budget_b = sim_b["final_metrics"]["total_budget_spent"]
        
        # Compare risk
        risk_a = sim_a["risk"]["score"]
        risk_b = sim_b["risk"]["score"]
        
        # Compare employment
        employment_a = sim_a["final_metrics"]["employment_improvement"]
        employment_b = sim_b["final_metrics"]["employment_improvement"]
        
        # Generate recommendations
        recommendations = []
        
        if pay_gap_a > pay_gap_b:
            recommendations.append(
                f"Policy A reduces pay gap by {pay_gap_a:.1f}% vs {pay_gap_b:.1f}% for Policy B"
            )
            better_pay_gap = "a"
        else:
            recommendations.append(
                f"Policy B reduces pay gap by {pay_gap_b:.1f}% vs {pay_gap_a:.1f}% for Policy A"
            )
            better_pay_gap = "b"
        
        if budget_a < budget_b:
            recommendations.append(
                f"Policy A is more budget-efficient (${budget_a:,.0f} vs ${budget_b:,.0f})"
            )
            better_budget = "a"
        else:
            recommendations.append(
                f"Policy B is more budget-efficient (${budget_b:,.0f} vs ${budget_a:,.0f})"
            )
            better_budget = "b"
        
        if risk_a < risk_b:
            recommendations.append(
                f"Policy A has lower risk ({sim_a['risk']['level']} vs {sim_b['risk']['level']})"
            )
            better_risk = "a"
        else:
            recommendations.append(
                f"Policy B has lower risk ({sim_b['risk']['level']} vs {sim_a['risk']['level']})"
            )
            better_risk = "b"
        
        # Overall recommendation
        scores = {"a": 0, "b": 0}
        scores[better_pay_gap] += 3  # Pay gap reduction is most important
        scores[better_budget] += 2
        scores[better_risk] += 1
        
        if scores["a"] > scores["b"]:
            overall = "Policy A is recommended overall - better pay gap reduction outweighs other factors"
        elif scores["b"] > scores["a"]:
            overall = "Policy B is recommended overall - superior combination of metrics"
        else:
            overall = "Both policies have similar overall impact - choose based on budget and risk tolerance"
        
        return {
            "recommendations": recommendations,
            "overall_recommendation": overall,
            "metrics_comparison": {
                "pay_gap_reduction_diff": round(abs(pay_gap_a - pay_gap_b), 2),
                "budget_diff": round(abs(budget_a - budget_b), 2),
                "risk_diff": round(abs(risk_a - risk_b), 2),
                "employment_diff": round(abs(employment_a - employment_b), 2)
            }
        }
    
    def _get_timestamp(self):
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()


# Create singleton instance
simulation_engine = SimulationEngine()