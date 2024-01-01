import React from 'react';
import MenuItem from '@mui/material/MenuItem';
import Stack from '@mui/material/Stack';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import { Menu } from '@mui/material';

interface CustomMenuItemProps {
    text: string;
    icon?: React.ReactNode;
    onClick?: () => void;
}

interface CustomMenuProps {
  items: CustomMenuItemProps[];
  open: boolean;
  anchorEl?: any;
  keepMounted?: any
  onClose?: () => void;
}


export const CustomMenu: React.FC<CustomMenuProps> = (props) => {
  const { items, open, ...other } = props;
  return (
    <Menu open={open} id="simple-menu" {...other}>
      {items.map(item => 
        <MenuItem onClick={item.onClick}>
          <Stack direction="row" spacing={5}>
            <ListItemText>{item.text}</ListItemText>
            <ListItemIcon>
              {item.icon}
            </ListItemIcon>
          </Stack>
        </MenuItem>
      )}
    </Menu>
  );
}