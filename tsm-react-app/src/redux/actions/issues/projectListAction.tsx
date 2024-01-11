import { UnknownAction } from "redux";
import { ProjectState } from "../../reducers/issues/projectListReducer";

export enum ProjectListTypes {
    PROJECT_LIST_CHANGED = 'PROJECT_LIST_CHANGED',
    PROJECT_LIST_LOADED = 'PROJECT_LIST_LOADED'
};

export interface ProjectListAction extends UnknownAction {
  type: ProjectListTypes;
  payload: ProjectState;
}

export interface ProjectListLoadAction extends UnknownAction {
  type: ProjectListTypes;
  payload: ProjectState[];
}

export const projectListChange = (data: ProjectState): ProjectListAction => ({
  type: ProjectListTypes.PROJECT_LIST_CHANGED,
  payload: data
});

export const projectListLoad = (data: ProjectState[]): ProjectListLoadAction => ({
  type: ProjectListTypes.PROJECT_LIST_LOADED,
  payload: data
});

