import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate} from 'react-router-dom';
import { AuthenticationPage } from './auth/LoginOrRegisterPage';
import { WelcomePage } from './WelcomePage';
import { HomePage } from './home/MainPage';
import { LogoutPage } from './auth/Logout';
import { ProjectDetailPage } from './issues/ProjectDetailPage';

export const App: React.FC = (props) => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/login" element={<AuthenticationPage />} />
        <Route path="/tsm-app" element={<LogoutPage />} />
        {/* <Route path="/tsm-app/projects/:id" element={<ProjectDetailPage title="Akselos Modeler Development" />} /> */}
      </Routes>
    </Router>
  );
}