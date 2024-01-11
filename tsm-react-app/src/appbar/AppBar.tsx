import React from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import MenuIcon from '@mui/icons-material/Menu';
import AdbIcon from '@mui/icons-material/Adb';
import {
  AppBar,
  Box,
  Toolbar,
  IconButton,
  Typography,
  Container,
  Avatar,
  Button,
  Tooltip,
  MenuItem,
  Menu,
  Grid
} from '@mui/material';

import { CreateTaskDialog } from './CreateTaskDialog';
import { ProjectDropDownButton } from './dropdown/ProjectDropDownButton';
import { CustomMenu } from '../components/Menu';


const pages = ['Project'];
const settings = ['Profile', 'Account', 'Dashboard', 'Logout'];

interface AppBarProps {
  children?: React.ReactNode;
}

export const ResponsiveAppBar: React.FC<AppBarProps> = (props) => {
  const { children } = props;
  const navigate = useNavigate();  // Use the useNavigate hook

  const settingModels = [
    { text: "Logout", value: "", onClick: async () => {
      try {
        const response = await axios.post("/api/logout");
        if (!response.data.success) navigate("/tsm-app");
        else navigate("/logout");
      }
      catch {
        navigate("/tsm-app");
      }
    }}
  ]

  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);
  const [ openCreateDialog, setOpenCreateDialog ] = React.useState(false);

  const handleOpenNavMenu = (event: any) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event: any) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleShowCreateDialog = () => {
    setOpenCreateDialog(true);
  }

  const handleHideCreateDialog = () => {
    setOpenCreateDialog(false);
  }

  const createTask = (project: string, assignee: string) => {
    console.log(project);
    setOpenCreateDialog(false);
  }

  return (
    <Box>
      <AppBar position="static">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <AdbIcon sx={{ display: { xs: 'none', md: 'flex' }, mr: 1 }} />
            <Typography
              variant="h6"
              noWrap
              component="a"
              href="/tsm-app/"
              sx={{
                mr: 2,
                display: { xs: 'none', md: 'flex' },
                fontFamily: 'monospace',
                fontWeight: 700,
                letterSpacing: '.3rem',
                color: 'inherit',
                textDecoration: 'none',
              }}
            >
              TSM
            </Typography>

            <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleOpenNavMenu}
                color="inherit"
              >
                <MenuIcon />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorElNav}
                anchorOrigin={{
                  vertical: 'bottom',
                  horizontal: 'left',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'left',
                }}
                open={Boolean(anchorElNav)}
                onClose={handleCloseNavMenu}
                sx={{
                  display: { xs: 'block', md: 'none' },
                }}
              >
                {pages.map((page) => (
                  <MenuItem key={page} onClick={handleCloseNavMenu}>
                    <Typography textAlign="center">{page}</Typography>
                  </MenuItem>
                ))}
                <MenuItem key='create' onClick={handleShowCreateDialog}>
                    <Typography textAlign="center">Create</Typography>
                </MenuItem>
              </Menu>
            </Box>
            <AdbIcon sx={{ display: { xs: 'flex', md: 'none' }, mr: 1 }} />
            <Typography
              variant="h5"
              noWrap
              component="a"
              href="/tsm-app/"
              sx={{
                mr: 2,
                display: { xs: 'flex', md: 'none' },
                flexGrow: 1,
                fontFamily: 'monospace',
                fontWeight: 700,
                letterSpacing: '.3rem',
                color: 'inherit',
                textDecoration: 'none',
              }}
            >
              TSM
            </Typography>
            <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
             <ProjectDropDownButton
                key='project' 
                onClick={handleCloseNavMenu}
              /> 
              <Button
                  key='create'
                  onClick={handleShowCreateDialog}
                  sx={{ my: 2, color: 'white', display: 'block' }}
                >
                Create
              </Button>
            </Box>

            <Box sx={{ flexGrow: 0 }}>
              <Tooltip title="Open settings">
                <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                  <Avatar alt="Remy Sharp" src="#" />
                </IconButton>
              </Tooltip>
              <CustomMenu
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
                items={settingModels}
              />
              {/* <Menu
                sx={{ mt: '45px' }}
                id="menu-appbar"
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
              >
                {settings.map((setting) => (
                  <MenuItem key={setting} onClick={handleCloseUserMenu}>
                    <Typography textAlign="center">{setting}</Typography>
                  </MenuItem>
                ))}
              </Menu> */}
            </Box>
          </Toolbar>
        </Container>
      </AppBar>
      <Grid container>
        {children}
      </Grid>
      {openCreateDialog ? 
        <CreateTaskDialog 
          onAccepted={createTask} 
          onClose={handleHideCreateDialog}/> 
        : null
      }
    </Box>
  );
};