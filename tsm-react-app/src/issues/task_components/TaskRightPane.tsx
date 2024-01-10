import React from 'react';
import Typography from '@mui/material/Typography';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemAvatar from '@mui/material/ListItemAvatar';
import ListItemText from '@mui/material/ListItemText';
import ListSubheader from '@mui/material/ListSubheader'
import Avatar from '@mui/material/Avatar';
import { Box, ListItemIcon } from '@mui/material';
import { Cloud, Create } from '@mui/icons-material';


export const TaskRightPane: React.FC = () => {
  return (
    <Box>
      <Typography variant="h5" gutterBottom component="div" sx={{ p: 2, pb: 0 }}>
        Details
      </Typography>
      <List sx={{ mb: 2 }}>
        <React.Fragment key={1}>
          <ListSubheader sx={{ bgcolor: 'background.paper' }}>
              Project Lead
          </ListSubheader>
          <ListItem>
            <ListItemAvatar>
            <Avatar alt="Profile Picture" src='/reporter.png' />
            </ListItemAvatar>
            <ListItemText primary='Brian Sabbey' secondary='' />
          </ListItem>
        </React.Fragment>
        <React.Fragment key={2}>
          <ListSubheader sx={{ bgcolor: 'background.paper' }}>
            Assignee
          </ListSubheader>
          <ListItem>
            <ListItemAvatar>
            <Avatar alt="Profile Picture" src='/assignee.png' />
            </ListItemAvatar>
            <ListItemText primary='Sinh Pham' secondary='' />
          </ListItem>
        </React.Fragment>
        <React.Fragment key={3}>
          <ListSubheader sx={{ bgcolor: 'background.paper' }}>
            Priority
          </ListSubheader>
          <ListItem>
            <ListItemIcon>
              <Create />
            </ListItemIcon>
            <ListItemText primary='Low' secondary='' />
          </ListItem>
        </React.Fragment>
        <React.Fragment key={4}>
          <ListSubheader sx={{ bgcolor: 'background.paper' }}>
            Story point
          </ListSubheader>
          <ListItem>
            <ListItemIcon>
              <Cloud />
            </ListItemIcon>
            <ListItemText primary='5' secondary='' />
          </ListItem>
        </React.Fragment>
      </List>
    </Box>
  );
}