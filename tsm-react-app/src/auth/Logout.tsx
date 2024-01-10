import React from 'react';
import {
  Container,
  Button,
  Typography
} from '@mui/material';

export const LogoutPage: React.FC = () => {

  return (
    <Container>
      <Typography>You've just logged out!</Typography>
      <Button href='/login'>Login</Button>
    </Container>
  );
};