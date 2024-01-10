import { CounterAction } from "../actions/counterAction";
import { CounterActionTypes } from "../actions/counterTypes";

export interface CounterState {
  counter: number;
}

export const counterState: CounterState = {
  counter: 0
}

export const counterReducer = (counterState: CounterState, action: CounterAction) => {
  switch (action.type) {
    case CounterActionTypes.INCREMENT:
      return { ...counterState, counter: action.payload + 1 };
      case CounterActionTypes.DECREMENT:
        return { ...counterState, counter: action.payload - 1};
    default:
      return counterState;
  }
}

