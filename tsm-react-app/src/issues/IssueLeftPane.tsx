import React from "react";
import { 
  List, 
  ListItem, 
  ListItemButton, 
  ListItemText,
  Box,
  Toolbar,
  Divider,
  Typography
} from "@mui/material";


interface FilterProps {
  text: string;
  href: string;
};


const projectFilters: FilterProps[] = [
  {
    text: "All tasks",
    href: '/tsm-app/tasks/',
  },
  {
    text: "My open tasks",
    href: "/tsm-app/tasks?status=to_do"
  }
];


export const IssueLeftPane: React.FC = () => {
  return (
    <Box>
      <Toolbar>
        <Typography variant="h6" component="div">
          Akselos Modeler Developement 
        </Typography>
      </Toolbar>
      <Divider />
      <List sx={{ bgcolor: 'background.paper' }}>
        {projectFilters.map(({ text, href }) => {
          return (
            <ListItem
              key={href}
              disablePadding
            >
              <ListItemButton>
                <ListItemText primary={text} />
              </ListItemButton>
            </ListItem>
          );
        })}
      </List>
  </Box>
 );
}