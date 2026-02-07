/**
 * RiskMeter Component - Visual risk indicator
 */
import React from 'react';
import '../styles/riskmeter.css';

const RiskMeter = ({ riskData }) => {
  const { score, level } = riskData;

  const getRiskColor = () => {
    if (level === 'low') return '#10B981'; // Green
    if (level === 'medium') return '#F59E0B'; // Yellow
    return '#EF4444'; // Red
  };

  const getRiskIcon = () => {
    if (level === 'low') return '✓';
    if (level === 'medium') return '⚠';
    return '⚠';
  };

  const getRiskLabel = () => {
    if (level === 'low') return 'Low Risk';
    if (level === 'medium') return 'Medium Risk';
    return 'High Risk';
  };

  const getDescription = () => {
    if (level === 'low') {
      return 'Strong chances of success with minimal implementation challenges';
    } else if (level === 'medium') {
      return 'Reasonable success probability with some expected challenges';
    } else {
      return 'Ambitious policy that may face significant political or practical obstacles';
    }
  };

  return (
    <div className="risk-meter">
      <div className="risk-header">
        <h4>Risk Assessment</h4>
      </div>
      
      <div className="risk-visual">
        <div className="risk-circle" style={{ borderColor: getRiskColor() }}>
          <div className="risk-icon" style={{ color: getRiskColor() }}>
            {getRiskIcon()}
          </div>
          <div className="risk-score" style={{ color: getRiskColor() }}>
            {Math.round(score)}
          </div>
          <div className="risk-max">/100</div>
        </div>
      </div>

      <div className="risk-label" style={{ color: getRiskColor() }}>
        {getRiskLabel()}
      </div>

      <div className="risk-description">
        {getDescription()}
      </div>

      {/* Risk bar */}
      <div className="risk-bar-container">
        <div 
          className="risk-bar-fill" 
          style={{ 
            width: `${score}%`,
            backgroundColor: getRiskColor() 
          }}
        />
      </div>

      <div className="risk-scale">
        <span className="scale-label">Low</span>
        <span className="scale-label">Medium</span>
        <span className="scale-label">High</span>
      </div>
    </div>
  );
};

export default RiskMeter;