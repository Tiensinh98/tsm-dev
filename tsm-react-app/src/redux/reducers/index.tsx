import axios from 'axios';
import { loginReducer, UserLoginState } from './auth/loginReducer';
import { registerReducer, UserRegisterState } from './auth/registerReducer';
import { projectListReducer, ProjectState } from './issues/projectListReducer';


export interface AppState {
  csrfToken: string;
  userLoginState: UserLoginState;
  userRegisterState: UserRegisterState;
  projectListState: ProjectState[]
}

// get csrf token
var csrfToken = '';
try {
  csrfToken = await axios.get("/api/csrf-token/");
}
catch (err) {
  console.error('Error fetching CSRF token', err)
}

const preLoadedState: AppState = {
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
  },
  projectListState: []
};
  
export const rootReducer = (state: AppState = preLoadedState, action: any): AppState => {
  return {
    ...state,
    userLoginState: loginReducer(state.userLoginState, action),
    userRegisterState: registerReducer(state.userRegisterState, action),
    projectListState: projectListReducer(state.projectListState, action)
  };
};