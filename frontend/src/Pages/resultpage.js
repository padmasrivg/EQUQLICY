/**
 * ResultsPage - Display simulation results
 */
import React from 'react';
import { useLocation, useNavigate, Link } from 'react-router-dom';
import ResultsDashboard from '../components/resultsdashboard';
import '../styles/resultpage.css';

const ResultsPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const results = location.state?.results;

  // Redirect if no results data
  if (!results) {
    return (
      <div className="no-results-page">
        <div className="no-results-content">
          <h2>No Simulation Results</h2>
          <p>Please run a simulation first</p>
          <Link to="/create" className="btn btn-primary">
            Create Simulation
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="results-page">
      <div className="results-nav">
        <button 
          className="btn btn-outline-secondary back-btn"
          onClick={() => navigate('/create')}
        >
          ← New Simulation
        </button>
      </div>

      <ResultsDashboard results={results} />
    </div>
  );
};

export default ResultsPage;