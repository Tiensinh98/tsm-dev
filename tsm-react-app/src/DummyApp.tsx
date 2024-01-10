import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { AppState } from './redux/reducers/index';
import { increment, decrement } from './redux/actions/counterAction';

export const DummyApp: React.FC = () => {
  const dispatch = useDispatch();
  const { counter } = useSelector((state: AppState) => state.counterState);

  return (
    <div>
        <button onClick={() => dispatch(increment(counter))}>Increment</button>
        <button onClick={() => dispatch(decrement(counter))}>Decrement</button>
        <p>{counter}</p>
    </div>
  )
};