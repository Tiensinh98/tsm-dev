import React from 'react';
import axios from 'axios';
import { Container } from '@mui/material';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';

import { GroupTab } from '../components/GroupTab';
import { LoginForm } from './LoginForm';
import { RegisterForm } from './RegisterForm';
import { AppState } from '../redux/reducers';


export const AuthenticationPage: React.FC = () => {
  const navigate = useNavigate();  // Use the useNavigate hook

  const { email, username: username2, password: password2 } = useSelector((state: AppState) => state.userRegisterState);
  const { username, password } = useSelector((state: AppState) => state.userLoginState);
  const csrfToken: string = useSelector((state: AppState) => state.csrfToken);

  const handleLogin = async (event: React.SyntheticEvent) => {
    // prevent the default behavior of <form> that automatically checks the CSRF token 
    // instead of manually checking by calling API
    event.preventDefault();
    try {
      const response = await axios.post("/api/login/", {
        username, password, headers: {
          'X-CSRFToken': csrfToken
        }
      });
      if (!response.data.success) navigate("/login");
      else navigate("/tsm-app");
    }
    catch {
      navigate("/login");
    }
  };

  const handleRegister = async (event: React.SyntheticEvent) => {
    event.preventDefault();
    const response = await axios.post("/api/register/", {
      email,
      username: username2,
      password: password2,
      headers: {
        'X-CSRFToken': csrfToken
      }
    });
    if (!response.data.success) navigate("/login");
    else navigate("/tsm-app");
  };

  return (
    <GroupTab labels={["Login", "Register"]}>
      <Container>
        <form
          method="POST"
          onSubmit={handleLogin} 
          style={{ marginTop: '10px' }}>
          <LoginForm />
        </form>
      </Container>
      <Container>
        <form 
          method="POST" 
          onSubmit={handleRegister} 
          style={{ marginTop: '10px' }}>
            <RegisterForm />
        </form>
      </Container>
    </GroupTab>
  );
};