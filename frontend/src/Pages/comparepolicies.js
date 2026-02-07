/**
 * ComparePolicies Page - Compare two policy configurations
 */
import React, { useState } from 'react';
import PolicyForm from '../components/policyform';
import ComparisonPage from '../components/comparisonpage';
import { comparepolicies } from '../services/api';
import '../styles/comparepolicies.css';

const ComparePolicies = () => {
  const [policyA, setPolicyA] = useState(null);
  const [policyB, setPolicyB] = useState(null);
  const [comparisonResults, setComparisonResults] = useState(null);
  const [isComparing, setIsComparing] = useState(false);

  const handlePolicyASubmit = (formData) => {
    setPolicyA(formData);
  };

  const handlePolicyBSubmit = (formData) => {
    setPolicyB(formData);
  };

  const handleCompare = async () => {
    if (!policyA || !policyB) {
      alert('Please configure both policies first');
      return;
    }

    setIsComparing(true);
    try {
      const response = await comparepolicies(policyA, policyB);
      
      if (response.success) {
        setComparisonResults(response.data);
      } else {
        alert('Comparison failed. Please try again.');
      }
    } catch (error) {
      alert('Error comparing policies: ' + error.message);
    } finally {
      setIsComparing(false);
    }
  };

  const handleReset = () => {
    setPolicyA(null);
    setPolicyB(null);
    setComparisonResults(null);
  };

  if (comparisonResults) {
    return (
      <div className="comparison-results-page">
        <div className="results-header">
          <button 
            className="btn btn-outline-secondary"
            onClick={handleReset}
          >
            ← New Comparison
          </button>
        </div>
        <ComparisonPage comparisonData={comparisonResults} />
      </div>
    );
  }

  return (
    <div className="compare-policies-page">
      <div className="page-header">
        <h1>Compare Policies</h1>
        <p className="subtitle">Test two policy configurations side-by-side</p>
      </div>

      <div className="comparison-forms">
        {/* Policy A Form */}
        <div className="policy-form-panel policy-a-panel">
          <div className="panel-header">
            <h3>Policy A</h3>
            {policyA && <span className="configured-badge">✓ Configured</span>}
          </div>
          <PolicyForm 
            onSubmit={handlePolicyASubmit}
            initialValues={policyA}
          />
        </div>

        {/* VS Divider */}
        <div className="vs-divider-column">
          <div className="vs-circle">VS</div>
        </div>

        {/* Policy B Form */}
        <div className="policy-form-panel policy-b-panel">
          <div className="panel-header">
            <h3>Policy B</h3>
            {policyB && <span className="configured-badge">✓ Configured</span>}
          </div>
          <PolicyForm 
            onSubmit={handlePolicyBSubmit}
            initialValues={policyB}
          />
        </div>
      </div>

      {/* Compare Button */}
      <div className="compare-action">
        <button
          className="btn btn-primary btn-lg compare-btn"
          onClick={handleCompare}
          disabled={!policyA || !policyB || isComparing}
        >
          {isComparing ? (
            <>
              <span className="spinner-border spinner-border-sm me-2" />
              Comparing Policies...
            </>
          ) : (
            <>
              <span className="btn-icon">⚖</span>
              Compare Policies
            </>
          )}
        </button>
      </div>
    </div>
  );
};

export default ComparePolicies;