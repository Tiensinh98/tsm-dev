import React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Typography from '@mui/material/Typography';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import InboxIcon from '@mui/icons-material/MoveToInbox';
import MailIcon from '@mui/icons-material/Mail';

import { ProjectDetailTable } from './ProjectDetalTable';
import { ResponsiveAppBar } from '../appbar/AppBar';


const projectFilters = [
  {
    text: "All tasks",
    value: null,
    icon: <InboxIcon />
  },
  {
    text: "My open tasks",
    value: null,
    icon: <MailIcon />
  },
  {
    text: "Open tasks",
    value: null,
    icon: <MailIcon />
  }
];

interface ProjectDetailProps {
  title?: string;
}

export const ProjectDetailPage: React.FC<ProjectDetailProps> = (props) => {
  const { title } = props;

  return (
    <ResponsiveAppBar>
      <Box sx={{ display: 'flex', flexDirection: 'row'}}>
        <Box 
          sx={{ p: 1, height: '100vh'}}>
          <Toolbar>
            <Typography variant="h6" component="div">
              {title}
            </Typography>
          </Toolbar>
          <Divider />
          <List>
            {projectFilters.map(filter => (
              <ListItem key={filter.text} disablePadding>
                <ListItemButton>
                  <ListItemIcon>
                    {filter.icon}
                  </ListItemIcon>
                  <ListItemText primary={filter.text} />
                </ListItemButton>
              </ListItem>
            ))}
          </List>
        </Box>
        <Box
          sx={{ flexGrow: 1, p: 1 , height: '100vh'}}
        >
          <ProjectDetailTable />
        </Box>
      </Box>
    </ResponsiveAppBar>
  );
}