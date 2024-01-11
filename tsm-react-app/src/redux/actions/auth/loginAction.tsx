import { UnknownAction } from "redux";

export enum UserLoginTypes {
  USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS',
  USER_LOGIN_REQUEST = 'USER_LOGIN_REQUEST',
  USER_LOGIN_CREDS_CHANGED = 'USER_LOGIN_CREDS_CHANGED',
  USER_LOGIN_FAILED = 'USER_LOGIN_FAILED'
};

export interface UserLoginAction extends UnknownAction {
  type: UserLoginTypes;
  payload: { name: string, value: string }; // Customize this payload type based on your needs
}

export const userLoginCredChange = (name: string, value: string): UserLoginAction => ({
  type: UserLoginTypes.USER_LOGIN_CREDS_CHANGED,
  payload: { name, value }
});