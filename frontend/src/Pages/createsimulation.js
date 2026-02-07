/**
 * CreateSimulation Page - Policy creation interface
 */
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PolicyForm from '../components/policyform';
import LineChart from '../components/charts/linechart';
import { runSimulation } from '../services/api';
import '../styles/createsimulation.css';

const CreateSimulation = () => {
  const navigate = useNavigate();
  const [isLoading, setIsLoading] = useState(false);
  const [previewData, setPreviewData] = useState(null);

  // Generate preview data for quick visualization
  const generatePreview = (formData) => {
    const years = [];
    const values = [];
    const baseGap = 23.0;
    
    for (let i = 0; i <= formData.duration; i++) {
      years.push(`Y${i}`);
      // Simple preview calculation
      const reduction = (formData.percentage / 100) * 0.3 * i;
      values.push(baseGap - reduction);
    }
    
    setPreviewData({ labels: years, values });
  };

  const handleFormChange = (formData) => {
    // Update preview when form changes
    generatePreview(formData);
  };

  const handleSubmit = async (formData) => {
    setIsLoading(true);
    try {
      const response = await runSimulation(formData);
      
      if (response.success) {
        // Navigate to results page with data
        navigate('/results', { state: { results: response.data } });
      } else {
        alert('Simulation failed. Please try again.');
      }
    } catch (error) {
      alert('Error running simulation: ' + error.message);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="create-simulation-page">
      <div className="page-header">
        <h1>Create New Simulation</h1>
        <p className="subtitle">Configure your gender policy parameters</p>
      </div>

      <div className="simulation-layout">
        {/* Left Panel - Form */}
        <div className="left-panel">
          <div className="form-card">
            <h3 className="panel-title">Policy Configuration</h3>
            <PolicyForm
              onSubmit={handleSubmit}
              onChange={handleFormChange}
              isLoading={isLoading}
            />
          </div>
        </div>

        {/* Right Panel - Preview */}
        <div className="right-panel">
          <div className="preview-card">
            <h3 className="panel-title">Impact Preview</h3>
            
            {previewData ? (
              <div className="preview-chart">
                <LineChart
                  data={previewData}
                  title="Projected Pay Gap Reduction"
                  yAxisLabel="Pay Gap (%)"
                  color="#6366F1"
                />
                <p className="preview-note">
                  This is a quick preview. Run the simulation for detailed analysis.
                </p>
              </div>
            ) : (
              <div className="preview-placeholder">
                <div className="placeholder-icon">📊</div>
                <p>Adjust parameters to see preview</p>
              </div>
            )}

            <div className="info-box">
              <h4>💡 Quick Tips</h4>
              <ul>
                <li>Higher percentages typically show stronger impact</li>
                <li>Longer durations allow more time for change</li>
                <li>Different policy types have different effectiveness curves</li>
                <li>Budget affects implementation feasibility</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreateSimulation;