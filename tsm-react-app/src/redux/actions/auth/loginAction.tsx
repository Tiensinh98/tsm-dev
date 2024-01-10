import { UnknownAction } from "redux";

export enum LoginActionTypes {
  USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS',
  USER_LOGIN_REQUEST = 'USER_LOGIN_REQUEST',
  USER_LOGIN_FAILED = 'USER_LOGIN_FAILED'
};

export interface LoginAction extends UnknownAction {
  type: LoginActionTypes;
  payload: number; // Customize this payload type based on your needs
}

export const loginRequest = (counter: number): LoginAction => ({
  type: LoginActionTypes.USER_LOGIN_SUCCESS,
  payload: counter
});

export const decrement = (counter: number): LoginAction => ({
  type: LoginActionTypes.USER_LOGIN_FAILED,
  payload: counter
})
