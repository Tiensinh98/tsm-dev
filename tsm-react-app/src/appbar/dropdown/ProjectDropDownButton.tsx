import React from "react";
import { Button } from "@mui/material";
import { Box } from "@mui/material";
import { CustomMenu } from "../../components/Menu";
import { Create, Delete } from "@mui/icons-material";

const MenuItems = [
  {
    text: "Project 1",
    value: "project_1",
    icon: <Delete />
  },
  {
    text: "Project 2",
    value: "project_2",
    icon: <Create />
  }
];

interface ProjectDropDownProps {
  key: string;
  onClick?: () => void;
}


export const ProjectDropDownButton: React.FC<ProjectDropDownProps> = (props) => {
  const { key, onClick } = props;

  const [anchorEl, setAnchorEl] = React.useState(null);
  const showMenu = Boolean(anchorEl);

  const handleShowMenu = (event: any) => {
    if (onClick) onClick();
    setAnchorEl(event.currentTarget);
  }

  const handleCloseMenu = () => {
    setAnchorEl(null);
  }

  return (
    <Box>
      <Button 
        aria-haspopup="true"
        key={key}
        onClick={handleShowMenu}
        sx={{ my: 2, color: 'white', display: 'block' }}
      >
        Projects
      </Button>
      <CustomMenu 
        anchorEl={anchorEl}
        keepMounted
        items={MenuItems} 
        open={showMenu} 
        onClose={handleCloseMenu}
      />
    </Box>
      );
}