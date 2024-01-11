import { UserRegisterAction, UserRegisterTypes } from "../../actions/auth/registerAction";
import { UserRegisterCredentials } from "../../actions/auth/registerAction";

export interface UserRegisterState {
  email: string;
  username: string;
  password: string;
  password2: string;
  isValid: boolean;
}

export const registerReducer = (state: UserRegisterState, action: UserRegisterAction) => {
  switch (action.type) {
    case UserRegisterTypes.USER_REGISTER_CREDS_CHANGED:
      const payload: UserRegisterCredentials = action.payload;
      let isValid: boolean = true;
      isValid &&= (payload.password === payload.password2 
        && payload.password.length > 0); // check password's identity
        isValid &&= (payload.email.length > 0 
        && payload.username.length > 0) // more secure check here.
      return { ...state, ... action.payload, isValid: isValid};
    default:
      return state;
  }
}

