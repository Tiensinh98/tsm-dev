import React from 'react';
import { ResponsiveAppBar } from '../appbar/AppBar';
import { IssueLeftPane } from './IssueLeftPane';
import { TaskRightPane } from './task_components/TaskRightPane';
import { TaskContentArea } from './task_components/TaskContentArea';
import { Grid } from '@mui/material';


interface TaskDetailProps {
  title?: string;
}

export const TaskDetailPage: React.FC<TaskDetailProps> = (props) => {
  const { title } = props;

  return (
    <ResponsiveAppBar>
        <Grid 
          item 
          lg={2} 
          padding={1}>
          <IssueLeftPane />
        </Grid>
        <Grid 
          item lg={8} 
          borderLeft={2} 
          borderRight={2}
          padding={1}
          borderColor="lightgrey">
          <TaskContentArea />
        </Grid>
        <Grid 
          item 
          lg={2} 
          padding={1}>
          <TaskRightPane />
        </Grid>
    </ResponsiveAppBar>
  );
}