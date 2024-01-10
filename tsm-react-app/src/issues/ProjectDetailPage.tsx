import React from 'react';
import { Grid } from '@mui/material';

import { ResponsiveAppBar } from '../appbar/AppBar';
import { IssueLeftPane } from './IssueLeftPane';
import { TaskTable } from './task_components/TaskTable';


interface ProjectDetailProps {
  title?: string;
}

export const ProjectDetailPage: React.FC<ProjectDetailProps> = (props) => {
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
          item lg={10} 
          padding={1}>
          <TaskTable />
        </Grid>
    </ResponsiveAppBar>
  );;
}