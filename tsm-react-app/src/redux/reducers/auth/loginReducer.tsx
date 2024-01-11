import { UserLoginAction, UserLoginTypes } from "../../actions/auth/loginAction";

export interface UserLoginState {
  username: string;
  password: string;
}

export const loginReducer = (loginCredState: UserLoginState, action: UserLoginAction) => {
  switch (action.type) {
    case UserLoginTypes.USER_LOGIN_CREDS_CHANGED:
      const payload: any = action.payload;
      return { ...loginCredState, [ payload.name ]: payload.value };
    default:
      return loginCredState;
  }
}

