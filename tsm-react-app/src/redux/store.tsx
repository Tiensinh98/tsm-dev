import { legacy_createStore as createStore, Store} from 'redux';
import { rootReducer, AppState } from './reducers'; // Import your root reducer


// const initialState = localStorage.getItem('userInfo')
//   ? JSON.parse(localStorage.getItem('userInfo'))
//   : null

export const store: Store<AppState> = createStore(rootReducer);