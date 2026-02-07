/**
 * PolicyForm Component - Interactive form for creating policy simulations
 */
import React, { useState } from 'react';
import '../styles/policyform.css';

const PolicyForm = ({ onSubmit, isLoading = false, initialValues = null }) => {
  const [formData, setFormData] = useState({
    policy_name: initialValues?.policy_name || '',
    policy_type: initialValues?.policy_type || 'equal_pay',
    percentage: initialValues?.percentage || 75,
    duration: initialValues?.duration || 5,
    budget: initialValues?.budget || 2000000,
  });

  const policyTypes = {
    equal_pay: {
      name: 'Equal Pay Policy',
      description: 'Mandate equal pay for equal work',
      minPercent: 50,
      maxPercent: 100,
    },
    leadership_quota: {
      name: 'Leadership Quota',
      description: 'Require minimum % of women in leadership',
      minPercent: 30,
      maxPercent: 50,
    },
    parental_leave: {
      name: 'Parental Leave Expansion',
      description: 'Extended paid leave for all parents',
      minPercent: 50,
      maxPercent: 100,
    },
  };

  const handleChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const currentPolicy = policyTypes[formData.policy_type];

  return (
    <form onSubmit={handleSubmit} className="policy-form">
      {/* Policy Name */}
      <div className="form-group mb-4">
        <label htmlFor="policy_name" className="form-label">
          Policy Name
        </label>
        <input
          type="text"
          id="policy_name"
          className="form-control"
          value={formData.policy_name}
          onChange={(e) => handleChange('policy_name', e.target.value)}
          placeholder="e.g., Equal Pay Initiative 2024"
          required
        />
      </div>

      {/* Policy Type Dropdown */}
      <div className="form-group mb-4">
        <label htmlFor="policy_type" className="form-label">
          Policy Type
        </label>
        <select
          id="policy_type"
          className="form-select"
          value={formData.policy_type}
          onChange={(e) => handleChange('policy_type', e.target.value)}
        >
          {Object.entries(policyTypes).map(([key, policy]) => (
            <option key={key} value={key}>
              {policy.name}
            </option>
          ))}
        </select>
        <small className="form-text text-muted">
          {currentPolicy.description}
        </small>
      </div>

      {/* Percentage Slider */}
      <div className="form-group mb-4">
        <label htmlFor="percentage" className="form-label">
          Policy Strength: <span className="value-badge">{formData.percentage}%</span>
        </label>
        <input
          type="range"
          id="percentage"
          className="form-range"
          min={currentPolicy.minPercent}
          max={currentPolicy.maxPercent}
          value={formData.percentage}
          onChange={(e) => handleChange('percentage', parseInt(e.target.value))}
        />
        <div className="range-labels">
          <span>{currentPolicy.minPercent}%</span>
          <span>{currentPolicy.maxPercent}%</span>
        </div>
      </div>

      {/* Duration Slider */}
      <div className="form-group mb-4">
        <label htmlFor="duration" className="form-label">
          Duration: <span className="value-badge">{formData.duration} years</span>
        </label>
        <input
          type="range"
          id="duration"
          className="form-range"
          min="1"
          max="10"
          value={formData.duration}
          onChange={(e) => handleChange('duration', parseInt(e.target.value))}
        />
        <div className="range-labels">
          <span>1 year</span>
          <span>10 years</span>
        </div>
      </div>

      {/* Budget Input */}
      <div className="form-group mb-4">
        <label htmlFor="budget" className="form-label">
          Total Budget
        </label>
        <div className="input-group">
          <span className="input-group-text">$</span>
          <input
            type="number"
            id="budget"
            className="form-control"
            value={formData.budget}
            onChange={(e) => handleChange('budget', parseInt(e.target.value))}
            min="100000"
            step="100000"
            required
          />
        </div>
        <small className="form-text text-muted">
          ${(formData.budget / 1000000).toFixed(1)}M total / 
          ${((formData.budget / formData.duration) / 1000000).toFixed(2)}M per year
        </small>
      </div>

      {/* Submit Button */}
      <button 
        type="submit" 
        className="btn btn-primary w-100 btn-lg submit-btn"
        disabled={isLoading}
      >
        {isLoading ? (
          <>
            <span className="spinner-border spinner-border-sm me-2" />
            Running Simulation...
          </>
        ) : (
          <>
            <span className="btn-icon">▶</span>
            Run Simulation
          </>
        )}
      </button>
    </form>
  );
};

export default PolicyForm;