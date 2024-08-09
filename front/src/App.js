import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import ImageComponent from './components/Image';
import FormComponent from './components/Form'; // Login
import RegisterComponent from './components/Register'; // Register

function App() {
  return (
    <Router>
      <div className="app">
        <ImageComponent />
        <div className="form-section">
          <Routes>
            <Route path="/" element={<FormComponent />} />
            <Route path="/register" element={<RegisterComponent />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
