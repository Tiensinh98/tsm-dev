import React from "react";
import { useSelector, useDispatch } from 'react-redux';
import { 
  Button, Box 
} from "@mui/material";

import { TextInput } from "../components/TextInput";
import { AppState } from "../redux/reducers";
import { userRegisterCredChange } from "../redux/actions/auth/registerAction";


export const RegisterForm: React.FC = () => {
  const dispatch = useDispatch();
  const { 
    email, username, password, 
    password2, isValid 
  } = useSelector((state: AppState) => state.userRegisterState);

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column'}}>
    <TextInput
      value={email}
      label="Email"
      name="email"
      type="email"
      onChange={(...args) => {
        dispatch(userRegisterCredChange({
          email: args[1], username, password, password2
        }));
      }}/>
    <TextInput
      value={username}
      label="Username"
      name="username"
      onChange={(...args) => {
        debugger;
        dispatch(userRegisterCredChange({
          email, username: args[1], password, password2
        }));
      }}/>
    <TextInput
      value={password}
      label="Password"
      name="password"
      type="password"
      onChange={(...args) => {
        dispatch(userRegisterCredChange({
          email, username, password: args[1], password2
        }));
      }}/>
    <TextInput
      value={password2}
      label="Confirmed password"
      name="password2"
      type="password"
      onChange={(...args) => {
        dispatch(userRegisterCredChange({
          email, username, password, password2: args[1]
        }));
      }}/>
    <Button 
      sx={{mt: 1}} 
      variant="contained" 
      type="submit"
      disabled={!isValid}>
      Register
    </Button>
    </Box>
  );
};