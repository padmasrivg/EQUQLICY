/**
 * LandingPage Component - Application home page
 */
/**import React from 'react';*/
import { Link } from 'react-router-dom';
import '../styles/landingpage.css';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <div className="hero-section">
        <div className="hero-content">
          <div className="hero-badge">Policy Simulation Platform</div>
          <h1 className="hero-title">
            PolicySim
          </h1>
          <p className="hero-subtitle">
            Gender Policy Impact Simulator
          </p>
          <p className="hero-description">
            Test policies before implementing them in real life. 
            Simulate gender equality initiatives and visualize their impact over time.
          </p>
          
          <div className="hero-actions">
            <Link to="/create" className="btn btn-primary btn-lg action-btn">
              <span className="btn-icon">+</span>
              Create New Simulation
            </Link>
            <Link to="/compare" className="btn btn-outline-primary btn-lg action-btn">
              <span className="btn-icon">⚖</span>
              Compare Policies
            </Link>
          </div>
        </div>

        <div className="hero-visual">
          <div className="visual-grid">
            <div className="visual-card card-1">
              <div className="card-icon">📊</div>
              <h3>Data-Driven</h3>
              <p>Realistic projections based on statistical models</p>
            </div>
            <div className="visual-card card-2">
              <div className="card-icon">⚡</div>
              <h3>Fast Results</h3>
              <p>Instant simulations with visual insights</p>
            </div>
            <div className="visual-card card-3">
              <div className="card-icon">🎯</div>
              <h3>Policy Testing</h3>
              <p>Compare multiple approaches side-by-side</p>
            </div>
          </div>
        </div>
      </div>

      {/* Features Section */}
      <div className="features-section">
        <h2 className="section-title">How It Works</h2>
        
        <div className="features-grid">
          <div className="feature-item">
            <div className="feature-number">01</div>
            <h3>Configure Policy</h3>
            <p>Choose policy type, set parameters like strength percentage, duration, and budget allocation</p>
          </div>
          
          <div className="feature-item">
            <div className="feature-number">02</div>
            <h3>Run Simulation</h3>
            <p>Our AI-powered engine calculates projected impact on pay gap, employment, and leadership</p>
          </div>
          
          <div className="feature-item">
            <div className="feature-number">03</div>
            <h3>Analyze Results</h3>
            <p>View interactive charts, risk assessments, and AI-generated explanations</p>
          </div>
          
          <div className="feature-item">
            <div className="feature-number">04</div>
            <h3>Download Report</h3>
            <p>Export comprehensive PDF reports with all data and visualizations</p>
          </div>
        </div>
      </div>

      {/* Policy Types Section */}
      <div className="policy-types-section">
        <h2 className="section-title">Policy Types Available</h2>
        
        <div className="policy-cards">
          <div className="policy-card">
            <div className="policy-icon">💰</div>
            <h3>Equal Pay Policy</h3>
            <p>Mandate equal pay for equal work across gender lines. Direct and fast-acting approach to wage equity.</p>
            <div className="policy-stats">
              <span className="stat">High Impact</span>
              <span className="stat">Medium Speed</span>
            </div>
          </div>
          
          <div className="policy-card">
            <div className="policy-icon">👔</div>
            <h3>Leadership Quota</h3>
            <p>Require minimum percentage of women in leadership positions. Systemic cultural transformation.</p>
            <div className="policy-stats">
              <span className="stat">Medium Impact</span>
              <span className="stat">Slow Speed</span>
            </div>
          </div>
          
          <div className="policy-card">
            <div className="policy-icon">👶</div>
            <h3>Parental Leave</h3>
            <p>Extended paid parental leave for all parents. Supports work-life balance and retention.</p>
            <div className="policy-stats">
              <span className="stat">Medium Impact</span>
              <span className="stat">Slow Speed</span>
            </div>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="cta-section">
        <h2>Ready to simulate your policy?</h2>
        <p>Start creating evidence-based gender equality policies today</p>
        <Link to="/create" className="btn btn-primary btn-lg">
          Get Started Now →
        </Link>
      </div>
    </div>
  );
};

export default LandingPage;