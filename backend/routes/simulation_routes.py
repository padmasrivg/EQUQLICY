"""
Routes for policy simulation operations
"""
from flask import Blueprint, request, jsonify
from services.simulation_engine import simulation_engine
from services.ai_explainer import explain_simulation_results, get_policy_insights

simulation_bp = Blueprint('simulation', __name__)


@simulation_bp.route('/api/simulate', methods=['POST'])
def run_simulation():
    """
    Run a policy simulation
    
    Expected JSON body:
    {
        "policy_type": "equal_pay",
        "percentage": 75,
        "duration": 5,
        "budget": 2000000,
        "policy_name": "Equal Pay Initiative 2024"
    }
    """
    try:
        data = request.get_json()
        
        # Extract parameters
        policy_type = data.get('policy_type')
        percentage = data.get('percentage')
        duration = data.get('duration')
        budget = data.get('budget')
        policy_name = data.get('policy_name', 'Unnamed Policy')
        
        # Validate required fields
        if not all([policy_type, percentage is not None, duration, budget is not None]):
            return jsonify({
                'error': 'Missing required fields',
                'required': ['policy_type', 'percentage', 'duration', 'budget']
            }), 400
        
        # Run simulation
        results = simulation_engine.run_simulation(
            policy_type=policy_type,
            percentage=float(percentage),
            duration=int(duration),
            budget=float(budget),
            policy_name=policy_name
        )
        
        return jsonify({
            'success': True,
            'data': results
        }), 200
        
    except ValueError as e:
        return jsonify({
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'error': f'Simulation failed: {str(e)}'
        }), 500


@simulation_bp.route('/api/explain', methods=['POST'])
def explain_results():
    """
    Get AI explanation for simulation results
    
    Expected JSON body:
    {
        "simulation_results": { ... }
    }
    """
    try:
        data = request.get_json()
        simulation_results = data.get('simulation_results')
        
        if not simulation_results:
            return jsonify({
                'error': 'Missing simulation_results'
            }), 400
        
        # Generate explanation
        explanation = explain_simulation_results(simulation_results)
        
        return jsonify({
            'success': True,
            'explanation': explanation
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': f'Explanation generation failed: {str(e)}'
        }), 500


@simulation_bp.route('/api/policy-insights/<policy_type>', methods=['GET'])
def get_insights(policy_type):
    """
    Get insights about a specific policy type
    """
    try:
        insights = get_policy_insights(policy_type)
        
        if not insights:
            return jsonify({
                'error': f'Unknown policy type: {policy_type}'
            }), 404
        
        return jsonify({
            'success': True,
            'insights': insights
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500