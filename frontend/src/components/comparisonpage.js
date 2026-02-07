/**
 * ComparisonPage Component - Side-by-side policy comparison
 */
import React from 'react';
import LineChart from './charts/linechart';
import RiskMeter from './riskmeter';
import '../styles/comparisonpage.css';

const ComparisonPage = ({ comparisonData }) => {
  const { policy_a, policy_b, analysis } = comparisonData;

  // Prepare chart data for both policies
  const prepareChartData = (simulation) => ({
    labels: simulation.timeline.years.map(y => `Y${y}`),
    values: simulation.timeline.pay_gap,
  });

  return (
    <div className="comparison-page">
      {/* Header */}
      <div className="comparison-header">
        <h2>Policy Comparison</h2>
        <p className="subtitle">Side-by-side analysis of two policy options</p>
      </div>

      {/* Policy Names */}
      <div className="policy-names">
        <div className="policy-name-card policy-a">
          <h3>Policy A</h3>
          <p>{policy_a.policy.name}</p>
          <span className="policy-badge">{policy_a.policy.type_name}</span>
        </div>
        <div className="vs-divider">VS</div>
        <div className="policy-name-card policy-b">
          <h3>Policy B</h3>
          <p>{policy_b.policy.name}</p>
          <span className="policy-badge">{policy_b.policy.type_name}</span>
        </div>
      </div>

      {/* Comparison Panels */}
      <div className="comparison-panels">
        {/* Policy A Panel */}
        <div className="policy-panel policy-a-panel">
          <h4>Policy A Details</h4>
          
          <div className="policy-metrics">
            <div className="metric-row">
              <span className="metric-label">Policy Type:</span>
              <span className="metric-value">{policy_a.policy.type_name}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Strength:</span>
              <span className="metric-value">{policy_a.policy.percentage}%</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Duration:</span>
              <span className="metric-value">{policy_a.policy.duration} years</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Budget:</span>
              <span className="metric-value">${(policy_a.policy.budget / 1000000).toFixed(1)}M</span>
            </div>
          </div>

          <div className="chart-wrapper">
            <LineChart
              data={prepareChartData(policy_a)}
              title="Pay Gap Reduction"
              yAxisLabel="Pay Gap (%)"
              color="#6366F1"
            />
          </div>

          <div className="results-summary">
            <h5>Key Results</h5>
            <div className="result-item">
              <span>Pay Gap Reduction:</span>
              <strong>{policy_a.final_metrics.pay_gap_reduction.toFixed(1)}%</strong>
            </div>
            <div className="result-item">
              <span>Employment Improvement:</span>
              <strong>{policy_a.final_metrics.employment_improvement.toFixed(1)}%</strong>
            </div>
            <div className="result-item">
              <span>Budget Spent:</span>
              <strong>${(policy_a.final_metrics.total_budget_spent / 1000000).toFixed(1)}M</strong>
            </div>
          </div>

          <div className="risk-wrapper">
            <RiskMeter riskData={policy_a.risk} />
          </div>
        </div>

        {/* Policy B Panel */}
        <div className="policy-panel policy-b-panel">
          <h4>Policy B Details</h4>
          
          <div className="policy-metrics">
            <div className="metric-row">
              <span className="metric-label">Policy Type:</span>
              <span className="metric-value">{policy_b.policy.type_name}</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Strength:</span>
              <span className="metric-value">{policy_b.policy.percentage}%</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Duration:</span>
              <span className="metric-value">{policy_b.policy.duration} years</span>
            </div>
            <div className="metric-row">
              <span className="metric-label">Budget:</span>
              <span className="metric-value">${(policy_b.policy.budget / 1000000).toFixed(1)}M</span>
            </div>
          </div>

          <div className="chart-wrapper">
            <LineChart
              data={prepareChartData(policy_b)}
              title="Pay Gap Reduction"
              yAxisLabel="Pay Gap (%)"
              color="#8B5CF6"
            />
          </div>

          <div className="results-summary">
            <h5>Key Results</h5>
            <div className="result-item">
              <span>Pay Gap Reduction:</span>
              <strong>{policy_b.final_metrics.pay_gap_reduction.toFixed(1)}%</strong>
            </div>
            <div className="result-item">
              <span>Employment Improvement:</span>
              <strong>{policy_b.final_metrics.employment_improvement.toFixed(1)}%</strong>
            </div>
            <div className="result-item">
              <span>Budget Spent:</span>
              <strong>${(policy_b.final_metrics.total_budget_spent / 1000000).toFixed(1)}M</strong>
            </div>
          </div>

          <div className="risk-wrapper">
            <RiskMeter riskData={policy_b.risk} />
          </div>
        </div>
      </div>

      {/* Analysis Section */}
      <div className="analysis-section">
        <h3>Comparative Analysis</h3>
        
        <div className="recommendations">
          {analysis.recommendations.map((rec, index) => (
            <div key={index} className="recommendation-item">
              <span className="rec-icon">•</span>
              <span>{rec}</span>
            </div>
          ))}
        </div>

        <div className="overall-recommendation">
          <h4>Overall Recommendation</h4>
          <p>{analysis.overall_recommendation}</p>
        </div>

        <div className="metrics-diff">
          <h5>Key Differences</h5>
          <div className="diff-grid">
            <div className="diff-item">
              <span className="diff-label">Pay Gap Reduction Difference:</span>
              <span className="diff-value">{analysis.metrics_comparison.pay_gap_reduction_diff.toFixed(2)}%</span>
            </div>
            <div className="diff-item">
              <span className="diff-label">Budget Difference:</span>
              <span className="diff-value">${(analysis.metrics_comparison.budget_diff / 1000000).toFixed(2)}M</span>
            </div>
            <div className="diff-item">
              <span className="diff-label">Risk Difference:</span>
              <span className="diff-value">{analysis.metrics_comparison.risk_diff.toFixed(1)} points</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ComparisonPage;