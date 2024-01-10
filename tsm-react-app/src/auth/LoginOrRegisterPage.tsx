import React from 'react';
import axios from 'axios';

import { useNavigate } from 'react-router-dom';
import { GroupTab } from '../components/GroupTab';
import { LoginForm, LoginCredsProps } from './LoginForm';
import { RegisterForm, RegisterCredsProps } from './RegisterForm';
import { Container } from '@mui/material';


export const AuthenticationPage: React.FC = () => {
  const navigate = useNavigate();  // Use the useNavigate hook

  const [ registerCredentials, setRegisterCredentials ] = React.useState<RegisterCredsProps | null>(null);
  const [ loginCredentials, setLoginCredentials ] = React.useState<LoginCredsProps | null>(null);
  const [ csrfToken, setCsrfToken] = React.useState('');

  React.useEffect(() => {
    // use fetch instead of axios since useEffect doesn't allow async mechanism
    fetch('/api/csrf-token/')
      .then(res => res.json())
      .then(data => setCsrfToken(data.csrfToken))
      .catch(err => console.error('Error fetching CSRF token', err));
  }, []);

  const handleLogin = async (event: React.SyntheticEvent) => {
    // prevent the default behavior of <form> that automatically checks the CSRF token 
    // instead of manually checking by calling API
    event.preventDefault();
    if (!loginCredentials) return;
    const { username, password } = loginCredentials;
    try {
      const response = await axios.post("/api/login/", {
        username, password, headers: {
          'X-CSRFToken': csrfToken
        }
      });
      if (!response.data.success) navigate("/login/");
      else navigate("/tsm-app/");
    }
    catch {
      navigate("/login/");
    }
  };

  const handleRegister = async (event: React.SyntheticEvent) => {
    event.preventDefault();
    if (!registerCredentials) return;
    const { email, username, password } = registerCredentials;
    const response = await axios.post("/api/register/", {
      username, email, password, headers: {
        'X-CSRFToken': csrfToken
      }
    });
    if (!response.data.success) navigate("/login/");
    else navigate("/tsm-app/");
  };

  return (
    <GroupTab labels={["Login", "Register"]}>
      <Container>
        <form 
          method="POST" 
          onSubmit={handleLogin} 
          style={{ marginTop: '10px' }}>
          <LoginForm 
            onCredsChange={(creds: LoginCredsProps) => setLoginCredentials(creds)}/>
        </form>
      </Container>
      <Container>
        <form 
          method="POST" 
          onSubmit={handleRegister} 
          style={{ marginTop: '10px' }}>
            <RegisterForm
              onCredsChange={(creds: RegisterCredsProps) => setRegisterCredentials(creds)}/>
        </form>
      </Container>
    </GroupTab>
  );
};