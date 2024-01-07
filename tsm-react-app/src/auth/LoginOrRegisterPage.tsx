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

  const handleLogin = () => {
    if (!loginCredentials) return;
    const { username, password } = loginCredentials;
    debugger;
    const f = async () => {
      try {
        debugger;
        const response = await axios.post("/api/login/", {
          username, password
        });
        console.log("Log: ")
        console.log(response)
        if (!response.data.success) navigate("/login/");
        else navigate("/tsm-app/");
      }
      catch {
        navigate("/login/");
      }
    }
    f();
  };

  const handleRegister = async () => {
    if (!registerCredentials) return;
    const { email, username, password } = registerCredentials;
    const response = await axios.post("/api/register/", {
      username, email, password
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