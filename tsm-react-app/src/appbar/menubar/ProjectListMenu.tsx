import React from "react";
import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { Avatar, Button, Menu, MenuItem } from "@mui/material";

import { AppState } from '../../redux/reducers';
import { ProjectState } from '../../redux/reducers/issues/projectListReducer';
import { projectListLoad } from '../../redux/actions/issues/projectListAction';



export const ProjectListMenu: React.FC = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const projectData: ProjectState[] = useSelector((state: AppState) => state.projectListState);
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);

  const handleShowMenu = (event: any) => {
    setAnchorEl(event.currentTarget);
  }

  const handleCloseMenu = () => {
    setAnchorEl(null);
  }

  const handleClickMenuItem = (id: number) => {
    handleCloseMenu();
    navigate(`/tsm-app/projects/${id}`)
  }

  React.useEffect(() => {
    (async ()=> {
      const response = await axios.get("/api/projects/");
      dispatch(projectListLoad(response.data));
    })();
  }, [])

  return (
    <React.Fragment>
      <Button sx={{ my: 2, color: 'white', display: 'block' }}
        onClick={handleShowMenu}>
        Projects
      </Button>
      <Menu 
        anchorEl={anchorEl}
        open={open}
        onClose={handleCloseMenu}
        onClick={handleCloseMenu}
        >
        { projectData.map(({ id, name }) => 
          <MenuItem
            onClick={() => handleClickMenuItem(id)}>
            <Avatar sx={{mr: 2}} src='https://picsum.photos/200'></Avatar>
            {name}
          </MenuItem>)
        }
      </Menu>
    </React.Fragment>
  );
}