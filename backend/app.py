"""
Main Flask application for PolicySim backend
"""
from flask import Flask, jsonify
from flask_cors import CORS
from routes.simulation_routes import simulation_bp
from routes.comparison_routes import comparison_bp


def create_app():
    """Application factory function"""
    app = Flask(__name__)
    
    # Enable CORS for frontend communication
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://localhost:3000", "http://localhost:5000"],
            "methods": ["GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Content-Type"]
        }
    })
    
    # Configuration
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max request size
    app.config['JSON_SORT_KEYS'] = False
    
    # Register blueprints
    app.register_blueprint(simulation_bp)
    app.register_blueprint(comparison_bp)
    
    # Health check endpoint
    @app.route('/api/health', methods=['GET'])
    def health_check():
        """Health check endpoint"""
        return jsonify({
            'status': 'healthy',
            'service': 'PolicySim Backend',
            'version': '1.0.0'
        }), 200
    
    # Root endpoint
    @app.route('/', methods=['GET'])
    def root():
        """Root endpoint with API information"""
        return jsonify({
            'service': 'PolicySim - Gender Policy Impact Simulator',
            'version': '1.0.0',
            'endpoints': {
                'simulation': '/api/simulate',
                'comparison': '/api/compare',
                'explain': '/api/explain',
                'download_report': '/api/download-report',
                'policy_types': '/api/policy-types',
                'health': '/api/health'
            },
            'documentation': 'See README.md for detailed API documentation'
        }), 200
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        """Handle 404 errors"""
        return jsonify({
            'error': 'Endpoint not found',
            'status': 404
        }), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """Handle 500 errors"""
        return jsonify({
            'error': 'Internal server error',
            'status': 500
        }), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        """Handle 400 errors"""
        return jsonify({
            'error': 'Bad request',
            'status': 400
        }), 400
    
    return app


if __name__ == '__main__':
    app = create_app()
    
    # Run development server
    print("🚀 Starting PolicySim Backend Server...")
    print("📍 Server running at: http://localhost:5000")
    print("📚 API Documentation available at root endpoint")
    print("\nAvailable endpoints:")
    print("  POST /api/simulate - Run policy simulation")
    print("  POST /api/compare - Compare two policies")
    print("  POST /api/explain - Get AI explanation")
    print("  POST /api/download-report - Download PDF report")
    print("  GET  /api/policy-types - Get available policy types")
    print("  GET  /api/health - Health check")
    print("\n✨ Ready to simulate policies!")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )