/**
 * Main App Component
 */
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/navbar';
import LandingPage from './Pages/landingpage';
import CreateSimulation from './Pages/createsimulation';
import ResultsPage from './Pages/resultpage';
import ComparePolicies from './Pages/comparepolicies';
import './styles/app.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/create" element={<CreateSimulation />} />
            <Route path="/results" element={<ResultsPage />} />
            <Route path="/compare" element={<ComparePolicies />} />
          </Routes>
        </main>
        <footer className="app-footer">
          <div className="container">
            <p>PolicySim - Gender Policy Impact Simulator © 2024</p>
            <p className="footer-note">
              Simulations are based on statistical models and should be used as guidance alongside expert consultation.
            </p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;