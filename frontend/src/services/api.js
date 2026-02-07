/**
 * API Service - Handles all backend communication
 */
import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * Run a policy simulation
 */
export const runSimulation = async (policyData) => {
  try {
    const response = await api.post('/api/simulate', policyData);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Simulation failed');
  }
};

/**
 * Get AI explanation for simulation results
 */
export const getExplanation = async (simulationResults) => {
  try {
    const response = await api.post('/api/explain', {
      simulation_results: simulationResults,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Failed to generate explanation');
  }
};

/**
 * Compare two policies
 */
export const comparepolicies = async (policyA, policyB) => {
  try {
    const response = await api.post('/api/compare', {
      policy_a: policyA,
      policy_b: policyB,
    });
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Comparison failed');
  }
};

/**
 * Download PDF report
 */
export const downloadReport = async (simulationResults, explanation) => {
  try {
    const response = await api.post('/api/download-report', {
      simulation_results: simulationResults,
      explanation: explanation,
    }, {
      responseType: 'blob', // Important for file download
    });
    
    // Create download link
    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', `PolicySim_Report_${Date.now()}.pdf`);
    document.body.appendChild(link);
    link.click();
    link.remove();
    window.URL.revokeObjectURL(url);
    
    return { success: true };
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Failed to download report');
  }
};

/**
 * Get insights about a policy type
 */
export const getPolicyInsights = async (policyType) => {
  try {
    const response = await api.get(`/api/policy-insights/${policyType}`);
    return response.data;
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Failed to get insights');
  }
};

/**
 * Health check
 */
export const checkHealth = async () => {
  try {
    const response = await api.get('/api/health');
    return response.data;
  } catch (error) {
    return { status: 'error' };
  }
};

export default api;