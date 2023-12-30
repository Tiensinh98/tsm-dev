import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';
import Login from './components/Login';
import Welcome from './components/Welcome';
import TsmApp from './components/TsmApp';
import Project from './components/Project';
import ProjectDetails from './components/ProjectDetails';

interface Props {
  field: string
}

export const App: React.FC<Props> = (props) => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/tsm-app" element={<TsmApp />} />
        <Route path="/tsm-app/projects" element={<Project />} />
        <Route path="/tsm-app/projects/:id" element={<ProjectDetails />} />
      </Routes>
    </Router>
  );
}