import { UnknownAction } from "redux";
import { CounterActionTypes } from "./counterTypes";

export interface CounterAction extends UnknownAction {
  type: CounterActionTypes;
  payload: number; // Customize this payload type based on your needs
}

export const increment = (counter: number): CounterAction => ({
  type: CounterActionTypes.INCREMENT,
  payload: counter
});

export const decrement = (counter: number): CounterAction => ({
  type: CounterActionTypes.DECREMENT,
  payload: counter
})
