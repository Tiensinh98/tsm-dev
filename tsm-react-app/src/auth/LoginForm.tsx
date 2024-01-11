import React from "react";
import { useSelector, useDispatch } from 'react-redux';
import { 
  Box, 
  Button 
} from "@mui/material";

import { TextInput } from "../components/TextInput";
import { AppState } from '../redux/reducers';
import { userLoginCredChange } from "../redux/actions/auth/loginAction";


export const LoginForm: React.FC = () => {
  const dispatch = useDispatch();
  const { username, password } = useSelector((state: AppState) => state.userLoginState);

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column'}}>
      <TextInput 
        value={username}
        label="Username"
        name="username"
        onChange={(name: string, value: string) => {
          dispatch(userLoginCredChange(name, value));
        }}/>
      <TextInput 
        value={password}
        label="Password"
        name="password"
        type="password"
        onChange={(name: string, value: string) => {
          dispatch(userLoginCredChange(name, value));
        }}/>
      <Button  
        sx={{mt: 1}}
        variant="contained"
        type="submit">
        Login
    </Button>
    </Box>
  );
};