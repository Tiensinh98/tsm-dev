import React from 'react';
import { Grid } from '@mui/material';
import { useParams } from 'react-router-dom';

import { ResponsiveAppBar } from '../appbar/AppBar';
import { IssueLeftPane } from './IssueLeftPane';
import { TaskTable } from './task-components/TaskTable';


export const ProjectDetailPage: React.FC = () => {
  const { id } = useParams();

  React.useEffect(() => {
    console.log(id)
  }, [])

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
          <TaskTable
            rows={[]}
          />
        </Grid>
    </ResponsiveAppBar>
  );;
}