import React from 'react';
import { Button, Typography, Grid } from '@mui/material';

import { ResponsiveAppBar } from '../appbar/AppBar';


export const HomePage: React.FC = () => {

  return (
      <ResponsiveAppBar>
        <Grid
        item 
        sx={{ 
          display: 'flex',
          flexDirection: "column",
          alignItems: "center", 
          justifyContent: "center", 
          height: "100vh"
          }} 
        xs={12}
        sm={12}
        md={12}
        lg={12}>
        <Typography>Recent projects Region</Typography>
        <Button href="/tsm-app/projects">
          Show all projects
        </Button>
      </Grid>
      </ResponsiveAppBar>
  );
};