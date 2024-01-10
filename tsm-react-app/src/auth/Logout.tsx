import React from 'react';
import {
  Grid,
  Button,
  Typography
} from '@mui/material';

export const LogoutPage: React.FC = () => {
  return (
    <Grid container>
      <Grid 
        item 
        sx={{ 
          display: 'flex',
          flexDirection: "column",
          alignItems: "center", 
          justifyContent: "center", 
          height: "100vh"
          }} 
        lg={12}>
        <Typography>You've just logged out!</Typography>
        <Button href='/login/'>Login</Button>
      </Grid>
    </Grid>
  );
};