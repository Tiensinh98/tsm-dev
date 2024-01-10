import React from 'react';
import { 
  Menu, 
  MenuItem, 
  Stack, 
  ListItemText, 
  ListItemIcon 
} from '@mui/material';

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
  sx?: any
  id?: string;
  anchorOrigin?: any
  transformOrigin?: any
  onClose?: () => void;
}


export const CustomMenu: React.FC<CustomMenuProps> = (props) => {
  const { items, open, ...other } = props;

  return (
    <Menu open={open} {...other}>
      {items.map(item => 
        <MenuItem key={item.text} onClick={item.onClick}>
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