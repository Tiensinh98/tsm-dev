import React from 'react';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert, { AlertProps, AlertColor } from '@mui/material/Alert';


interface NotificationProps {
    severity?: AlertColor | undefined;
    message: string;
    open: boolean;
};


const Alert = React.forwardRef<HTMLDivElement, AlertProps>(function Alert(
  props,
  ref,
) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});


export const Notification: React.FC<NotificationProps> = (props) => {
  const [open, setOpen] = React.useState(props.open);

  const handleClose = (event?: React.SyntheticEvent | Event, reason?: string) => {
    if (reason === 'clickaway') return;
    setOpen(false);
  };

  return (
    <Snackbar 
      open={open} 
      autoHideDuration={6000} 
      onClose={handleClose}
    >
      <Alert 
        onClose={handleClose} 
        severity={props.severity} 
        sx={{ width: '100%' }}>
        {props.message}
      </Alert>
    </Snackbar>
  );
};