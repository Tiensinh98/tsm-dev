import React from 'react';
import {
  Box,
  Avatar,
  Menu,
  MenuItem
} from '@mui/material';
import { Link } from './Link';

interface AvatarProps {
  alt: string;
  link?: string;
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
    <div onMouseDown={ e => togglePopup(e, true) }>
      <Box sx={{ width: 32 }}>
        { <Avatar>{alt?.split(' ').map(v => v[0]).join('')}</Avatar> }
        { alt? <Menu
            anchorEl={anchorEl}
            keepMounted
            open={open}
            onClose={ e => togglePopup(e, false) }>
            <MenuItem>
              <Link href={link? link : ''} text={alt}/>
            </MenuItem>
          </Menu> : null
        }
      </Box>
    </div>
  );
}