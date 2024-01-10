import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import { AuthenticationPage } from './auth/LoginOrRegisterPage';
import { LogoutPage } from './auth/Logout';
import { WelcomePage } from './WelcomePage';
import { HomePage } from './home/MainPage';

export const App: React.FC = (props) => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/login" element={<AuthenticationPage />} />
        <Route path="/logout" element={<LogoutPage />} />
        <Route path="/tsm-app" element={<HomePage />} />
        {/* <Route path="/tsm-app/projects/:id" element={<ProjectDetailPage title="Akselos Modeler Development" />} /> */}
      </Routes>
    </Router>
  );
}