import React from "react";
import { TextInput } from "../components/TextInput";
import { Box } from "@mui/material";
import { Button } from "@mui/material";

export interface LoginCredsProps {
  username: string;
  password: string;
}

interface LoginFormProps {
  onCredsChange?: (creds: LoginCredsProps) => void;
}


export const LoginForm: React.FC<LoginFormProps> = (props) => {
  const { onCredsChange } = props;
  const [ currentCreds, setCurrentInfo ] = React.useState<LoginCredsProps>({
    username: '', 
    password: ''
  })

  const handleChangeCreds = (name: string, value: string) => {
    setCurrentInfo({...currentCreds, [ name ]: value});
    if (onCredsChange) onCredsChange({...currentCreds, [ name ]: value});
  }

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column'}}>
      <TextInput 
        value={currentCreds.username}
        label="Username"
        name="username"
        onChange={handleChangeCreds}/>
      <TextInput 
        value={currentCreds.password}
        label="Password"
        name="password"
        type="password"
        onChange={handleChangeCreds}/>
      <Button  
        sx={{mt: 1}}
        variant="contained"
        type="submit">
        Login
    </Button>
    </Box>
  );
};