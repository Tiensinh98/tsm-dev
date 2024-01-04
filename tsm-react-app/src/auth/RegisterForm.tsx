import React from "react";
import { TextInput } from "../components/TextInput";
import { Box } from "@mui/material";
import { Button } from "@mui/material";


export interface RegisterCredsProps {
  email: string;
  username: string;
  password: string;
  password2: string;
}

interface RegisterFormProps {
  onCredsChange?: (info: RegisterCredsProps) => void;
}


export const RegisterForm: React.FC<RegisterFormProps> = (props) => {
  const { onCredsChange } = props;

  const [ submitDisabled, setSubmitDisabled ] = React.useState<boolean>(true);
  const [ currentCreds, setCurrentInfo ] = React.useState<RegisterCredsProps>({
    email: '',
    username: '', 
    password: '',
    password2: ''
  })

  const handleChangeCreds = (name: string, value: string) => {
    if (name === "password") {
      // TODO: validate the strength of password
    }
    else if (name === "password2") {
        if (currentCreds.password.length > 0) {
            if (value !== currentCreds.password) {
                setSubmitDisabled(false);
            }
            else {
                setSubmitDisabled(true);
            }
        }
    }
    let newCreds: any = {};
    newCreds[name] = value;
    setCurrentInfo({...currentCreds, ...newCreds});
    if (onCredsChange) onCredsChange({...currentCreds, ...newCreds});
  }

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column'}}>
    <TextInput
      value={currentCreds.email}
      label="Email"
      name="email"
      type="email"
      onChange={handleChangeCreds}/>
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
    <TextInput
      value={currentCreds.password2}
      label="Confirmed password"
      name="password2"
      type="password"
      onChange={handleChangeCreds}/>
    <Button variant="contained" type="submit" disabled={submitDisabled}>
      Register
    </Button>
    </Box>
  );
};