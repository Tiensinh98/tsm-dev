import { UnknownAction } from "redux";

export enum UserRegisterTypes {
  USER_REGISTER_SUCCESS = 'USER_REGISTER_SUCCESS',
  USER_REGISTER_REQUEST = 'USER_REGISTER_REQUEST',
  USER_REGISTER_CREDS_CHANGED = 'USER_REGISTER_CREDS_CHANGED',
  USER_REGISTER_FAILED = 'USER_REGISTER_FAILED'
};

export interface UserRegisterCredentials {
  email: string;
  username: string;
  password: string;
  password2: string;
}

export interface UserRegisterAction extends UnknownAction {
  type: UserRegisterTypes;
  payload: UserRegisterCredentials; // Customize this payload type based on your needs
}

export const userRegisterCredChange = (creds: UserRegisterCredentials): UserRegisterAction => ({
  type: UserRegisterTypes.USER_REGISTER_CREDS_CHANGED,
  payload: creds
});
