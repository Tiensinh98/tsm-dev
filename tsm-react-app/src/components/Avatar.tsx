import React from 'react';
import Avatar from '@mui/material/Avatar';
import { deepOrange } from '@mui/material/colors';

interface AvartarModel {
    src?: string
    alt?: string
    backGroundColor?: string
};

export const ImageAvatars: React.FC<AvartarModel> = (props) => {
  return (
    props.src ? <Avatar alt={props.alt} src={props.src} /> : 
      <Avatar sx={{ bgcolor: deepOrange[200] }}>{props.alt?.split(' ').map(v => v[0]).join('')}</Avatar>
  );
}