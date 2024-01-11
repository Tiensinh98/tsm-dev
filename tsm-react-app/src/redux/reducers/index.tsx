import axios from 'axios';
import { loginReducer, UserLoginState } from './auth/loginReducer';
import { registerReducer, UserRegisterState } from './auth/registerReducer';


export interface AppState {
  csrfToken: string;
  userLoginState: UserLoginState;
  userRegisterState: UserRegisterState;
}

// get csrf token
var csrfToken = '';
try {
  csrfToken = await axios.get("/api/csrf-token/");
}
catch (err) {
  console.error('Error fetching CSRF token', err)
}

const initialState: AppState = {
  csrfToken: csrfToken,
  userLoginState: { 
    username: '', 
    password: ''
  },
  userRegisterState: {
    email: '',
    username: '',
    password: '',
    password2: '',
    isValid: true
  }
};
  
export const rootReducer = (state: AppState = initialState, action: any): AppState => {
  return {
    ...state,
    userLoginState: loginReducer(state.userLoginState, action),
    userRegisterState: registerReducer(state.userRegisterState, action)
  };
};