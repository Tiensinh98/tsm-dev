import React from 'react';
import {
  Box,
  Avatar,
  Menu,
  MenuItem
} from '@mui/material';
import { deepOrange } from '@mui/material/colors';
import { Link } from './Link';

interface AvatarProps {
  alt: string;
  link: string;
  src?: string;
};

export const ImageAvatar: React.FC<AvatarProps> = (props) => {
  const { alt, src, link } = props;

  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  const togglePopup = (event: any, state: boolean) => {
    if (state) setAnchorEl(event.currentTarget);
    else setAnchorEl(null);
  }

  return (
    <Box /*<div style={{ width: "45px"}}*/
      onMouseEnter={e => togglePopup(e, true)}
    >
      {src ? 
        <Avatar
          alt={alt} 
          src={src} 
        /> : 
        <Avatar
          sx={{ bgcolor: deepOrange[200] }}
        >
          {alt?.split(' ').map(v => v[0]).join('')}
        </Avatar>
      }
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={open}
      >
        <MenuItem>
          <Link href={link} text={alt}/>
        </MenuItem>
      </Menu>
    </Box>
  );
}