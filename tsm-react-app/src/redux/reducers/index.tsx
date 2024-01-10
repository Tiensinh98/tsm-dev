import { CounterAction } from '../actions/counterAction';
import { CounterActionTypes } from '../actions/counterTypes';
import { CounterState, counterReducer, counterState } from './counterReducer';


export interface AppState {
  counterState: CounterState;
}

const initialState: AppState = {
  counterState: counterState
};
  
export const rootReducer = (
  state: AppState = initialState,
  action: CounterAction
): AppState => {
  if (action.type in CounterActionTypes) {
    return { ...state, counterState: counterReducer(state.counterState, action) };
  }
  return state;
};