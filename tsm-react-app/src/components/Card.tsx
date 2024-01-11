import React from 'react';
import { styled } from '@mui/material/styles';
import {
  Card,
  CardHeader,
  CardMedia,
  CardContent,
  CardActions,
  Collapse,
  Typography,
} from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import Delete from '@mui/icons-material/Delete';
import IconButton, { IconButtonProps } from '@mui/material/IconButton';

import { CustomMenu } from './Menu';


interface ExpandMoreProps extends IconButtonProps {
  expand: boolean;
}


interface ReviewCardProps {
  primaryKey: number;
  avatar: React.ReactNode;
  title: React.ReactNode;
  subHeader: string;
  image?: string;
  description?: string;
  children?: React.ReactNode;
  onDelete?: (id: number) => void;
}
  

const ExpandMore = styled((props: ExpandMoreProps) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? 'rotate(0deg)' : 'rotate(180deg)',
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
}));


export const ReviewCard: React.FC<ReviewCardProps> = (props) => {
  const { 
    primaryKey, 
    avatar, 
    title, 
    subHeader,
    image, 
    description, 
    children,
    onDelete
  } = props;

  const [expanded, setExpanded] = React.useState(false);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const showSettingsMenu = Boolean(anchorEl);

  const handleExpandClick = () => {
    setExpanded(!expanded);
  };

  const handleShowSettingsMenu = (event: any) => {
    setAnchorEl(event.currentTarget);
  };

  const handleDelete = () => {
    setAnchorEl(null);
    if (onDelete) onDelete(primaryKey)
  }

  return (
    <Card sx={{ width: 345 }} key={primaryKey}>
      <CardHeader
        avatar={avatar}
        action={
          <IconButton aria-label="settings" onClick={handleShowSettingsMenu}>
            <MoreVertIcon />
            <CustomMenu
              anchorEl={anchorEl}
              keepMounted
              open={showSettingsMenu}
              onClose={() => {setAnchorEl(null)}}
              items={
                [{
              text: "Delete",
              icon: <Delete fontSize="small" />,
              onClick: handleDelete
            }]}/>
          </IconButton>
        }
        title={title}
        subheader={subHeader}
      />
      {image? <CardMedia
        component="img"
        height="194"
        image={image}/> : null
      }
      <CardContent>
        <Typography variant="body2" color="text.secondary">
          {description}
        </Typography>
      </CardContent>
      <CardActions disableSpacing>
        <ExpandMore
          expand={expanded}
          onClick={handleExpandClick}
          aria-expanded={expanded}
          aria-label="show more"
        >
          <ExpandMoreIcon />
        </ExpandMore>
      </CardActions>
      <Collapse in={expanded} timeout="auto" unmountOnExit>
        <CardContent>
          {children}
        </CardContent>
      </Collapse>
    </Card>
  );
}