import React from 'react';
import DialogTitle from '@mui/material/DialogTitle';
import Dialog from '@mui/material/Dialog';

const emails = ['username@gmail.com', 'user02@gmail.com'];

interface EmptyDialogProps {
    title: string;
    open: boolean;
    content?: React.ReactNode;
    onClose: () => void;
    onAcepted: () => void;
};

export const EmptyDialogProps: React.FC<EmptyDialogProps> = (props) => {
    const { onClose, onAcepted, open } = props;

    const handleClose = () => {
        onClose();
        console.log("onClose")
    };

    const handleAcepted = () => {
        onAcepted();
    };

    return (
        <Dialog onClose={handleClose} open={open} sx={{width: 640, height: 320}}>
            <DialogTitle>{props.title}</DialogTitle>
            {props.content}
        </Dialog>
    );
};