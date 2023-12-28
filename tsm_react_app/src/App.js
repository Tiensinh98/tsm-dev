import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';
import Login from './components/Login';
import Welcome from './components/Welcome';
import TsmApp from './components/TsmApp';
import Project from './components/Project';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/tsm-app" element={<TsmApp />} />
        <Route path="/tsm-app/projects" element={<Project />} />
      </Routes>
    </Router>
  );
}

export default App;