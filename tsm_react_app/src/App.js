import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';
import PreHome from './components/PreHome';
import Login from './components/Login';
import Home from './components/Home';

function App() {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<PreHome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/home" element={<Home />} />
      </Routes>
    </Router>
  );
}

export default App;