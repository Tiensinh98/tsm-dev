import React from 'react';
import {
  Grid, 
  Button, 
  styled, 
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  IconButton
} from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';


const BootstrapDialog = styled(Dialog)(({ theme }) => ({
  '& .MuiDialogContent-root': {
    padding: theme.spacing(2),
  },
  '& .MuiDialogActions-root': {
    padding: theme.spacing(1),
  },
}));

interface EmptyDialogProps {
    title: string;
    children?: React.ReactNode;
    onAccepted?: () => void;
    onClose?: () => void;
};

export const EmptyDialog: React.FC<EmptyDialogProps> = (props) => {
  const { title, children, onAccepted, onClose} = props;
  const [open, setOpen] = React.useState(true);

  const handleClose = () => {
    setOpen(false);
    if (onClose) onClose();
  };

  const handleAccepted = () => {
    if (onAccepted) onAccepted();
  }

  return (
    <React.Fragment>
      <BootstrapDialog
        onClose={handleClose}
        aria-labelledby="customized-dialog-title"
        open={open}
      >
        <DialogTitle sx={{ m: 0, p: 2 }} id="customized-dialog-title">
          {title}
        </DialogTitle>
        <IconButton
          aria-label="close"
          onClick={handleClose}
          sx={{
            position: 'absolute',
            right: 8,
            top: 8,
            color: (theme) => theme.palette.grey[500],
          }}
        >
          <CloseIcon />
        </IconButton>
        <DialogContent dividers>
          <Grid container>
            {children}
          </Grid>
        </DialogContent>
        <DialogActions>
          <Button variant='contained' autoFocus onClick={handleAccepted}>
            OK
          </Button>
        </DialogActions>
      </BootstrapDialog>
    </React.Fragment>
  );
}