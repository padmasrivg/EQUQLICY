/**
 * ResultsDashboard Component - Display simulation results with charts
 */
import React, { useState } from 'react';
import LineChart from './charts/linechart';
import BarChart from './charts/barchart';
import PieChart from './charts/piechart';
import RiskMeter from './riskmeter';
import { getExplanation, downloadReport } from '../services/api';
import '../styles/resultsdashboard.css';

const ResultsDashboard = ({ results }) => {
  const [explanation, setExplanation] = useState(null);
  const [loadingExplanation, setLoadingExplanation] = useState(false);
  const [downloadingReport, setDownloadingReport] = useState(false);

  const { policy, timeline, final_metrics, risk } = results;

  // Prepare data for charts
  const payGapData = {
    labels: timeline.years.map(y => `Year ${y}`),
    values: timeline.pay_gap,
  };

  const employmentData = {
    labels: ['Baseline', 'Final'],
    values: [0.82, final_metrics.final_employment_ratio],
  };

  const leadershipData = {
    labels: ['Female Leadership', 'Male Leadership'],
    values: [
      final_metrics.final_leadership.female,
      final_metrics.final_leadership.male,
    ],
  };

  const handleExplainResults = async () => {
    setLoadingExplanation(true);
    try {
      const response = await getExplanation(results);
      setExplanation(response.explanation);
    } catch (error) {
      alert('Failed to generate explanation: ' + error.message);
    } finally {
      setLoadingExplanation(false);
    }
  };

  const handleDownloadReport = async () => {
    setDownloadingReport(true);
    try {
      await downloadReport(results, explanation || '');
      alert('Report downloaded successfully!');
    } catch (error) {
      alert('Failed to download report: ' + error.message);
    } finally {
      setDownloadingReport(false);
    }
  };

  return (
    <div className="results-dashboard">
      {/* Header */}
      <div className="results-header">
        <h2>{policy.name}</h2>
        <p className="policy-type-badge">{policy.type_name}</p>
      </div>

      {/* Key Metrics Summary */}
      <div className="metrics-summary">
        <div className="metric-card">
          <div className="metric-value">{final_metrics.pay_gap_reduction.toFixed(1)}%</div>
          <div className="metric-label">Pay Gap Reduced</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{final_metrics.employment_improvement.toFixed(1)}%</div>
          <div className="metric-label">Employment Boost</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">{final_metrics.final_leadership.female.toFixed(0)}%</div>
          <div className="metric-label">Female Leadership</div>
        </div>
        <div className="metric-card">
          <div className="metric-value">${(final_metrics.total_budget_spent / 1000000).toFixed(1)}M</div>
          <div className="metric-label">Total Budget</div>
        </div>
      </div>

      {/* Charts Grid */}
      <div className="charts-grid">
        <div className="chart-container">
          <LineChart
            data={payGapData}
            title="Gender Pay Gap Over Time"
            yAxisLabel="Pay Gap (%)"
            color="#6366F1"
          />
        </div>

        <div className="chart-container">
          <BarChart
            data={employmentData}
            title="Employment Ratio (Women/Men)"
            yAxisLabel="Ratio"
            color="#8B5CF6"
          />
        </div>

        <div className="chart-container">
          <PieChart
            data={leadershipData}
            title="Leadership Distribution"
          />
        </div>

        <div className="chart-container">
          <RiskMeter riskData={risk} />
        </div>
      </div>

      {/* AI Explanation Section */}
      <div className="explanation-section">
        {!explanation ? (
          <button
            className="btn btn-outline-primary btn-lg explain-btn"
            onClick={handleExplainResults}
            disabled={loadingExplanation}
          >
            {loadingExplanation ? (
              <>
                <span className="spinner-border spinner-border-sm me-2" />
                Generating explanation...
              </>
            ) : (
              <>
                <span className="btn-icon">✨</span>
                Explain Results in Simple Words
              </>
            )}
          </button>
        ) : (
          <div className="explanation-content">
            <h4>AI Analysis</h4>
            <div className="explanation-text">
              {explanation.split('\n').map((line, index) => (
                <p key={index}>{line}</p>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Download Report Button */}
      <div className="actions-section">
        <button
          className="btn btn-success btn-lg download-btn"
          onClick={handleDownloadReport}
          disabled={downloadingReport}
        >
          {downloadingReport ? (
            <>
              <span className="spinner-border spinner-border-sm me-2" />
              Generating PDF...
            </>
          ) : (
            <>
              <span className="btn-icon">📄</span>
              Download Full Report (PDF)
            </>
          )}
        </button>
      </div>
    </div>
  );
};

export default ResultsDashboard;