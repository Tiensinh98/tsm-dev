import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import { AuthenticationPage } from './auth/LoginOrRegisterPage';
import { LogoutPage } from './auth/Logout';
import { WelcomePage } from './WelcomePage';
import { HomePage } from './home/HomePage';
import { ProjectDetailPage } from './issues/ProjectDetailPage';
import { ProjectListPage } from './issues/ProjectListPage';

export const App: React.FC = (props) => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/user/login" element={<AuthenticationPage />} />
        <Route path="/tsm-app" element={<HomePage />} />
        <Route path="/tsm-app/projects" element={<ProjectListPage />} />
        <Route path="/tsm-app/projects/:id" element={<ProjectDetailPage />} />
        <Route path="/user/logout" element={<LogoutPage />} />
      </Routes>
    </Router>
  );
}