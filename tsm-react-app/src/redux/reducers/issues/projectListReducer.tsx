import { ProjectListLoadAction, ProjectListTypes } from "../../actions/issues/projectListAction";

interface leaderState {
  id: string;
  firstName: string;
  lastName: string;
}

export interface ProjectState {
  id: number;
  name: string;
  startDate: string;
  dueDate: string;
  priority: string;
  status: string;
  description: string;
  leader: leaderState;
}

export const projectListReducer = (state: ProjectState[], action: ProjectListLoadAction) => {
  switch (action.type) {
    case ProjectListTypes.PROJECT_LIST_LOADED:
      return action.payload;
    default:
      return state;
  }
}

