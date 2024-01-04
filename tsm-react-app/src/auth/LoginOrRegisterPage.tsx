import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { GroupTab } from '../components/GroupTab';
import { LoginForm, LoginCredsProps } from './LoginForm';
import { RegisterForm, RegisterCredsProps } from './RegisterForm';


export const AuthenticationPage: React.FC = () => {
  const navigate = useNavigate();  // Use the useNavigate hook

  const [ registerCredentials, setRegisterCredentials ] = React.useState<RegisterCredsProps | null>(null);
  const [ loginCredentials, setLoginCredentials ] = React.useState<LoginCredsProps | null>(null);

  const handleLogin = async () => {
    if (!loginCredentials) return;
    const { username, password } = loginCredentials;
    try {
      const response = await axios.post("/api/login/", {
        username, password
      });
      if (!response.data.success) navigate("/login/");
      else navigate("/tsm-app/");
    }
    catch {
      navigate("/login/");
    }
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
      <form onSubmit={handleLogin} style={{ marginTop: '10px' }}>
        <LoginForm 
          onCredsChange={(creds: LoginCredsProps) => setLoginCredentials(creds)}/>
      </form>
      <form onSubmit={handleRegister} style={{ marginTop: '10px' }}>
        <RegisterForm 
          onCredsChange={(creds: RegisterCredsProps) => setRegisterCredentials(creds)}/>
      </form>
    </GroupTab>
  );
};