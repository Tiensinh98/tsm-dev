import React from 'react';
import Button from '@mui/material/Button';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import Checkbox from '@mui/material/Checkbox';
import Box from '@mui/material/Box';

interface DropDownItemProps {
  text: string;
  value: string;
};


interface DropDownButtonProps {
  name: string;
  icon?: React.ReactNode;
  variant?: any;
  items: DropDownItemProps[];
  onChange?: (values: string[], selected?: string, state?: boolean) => void;
};

export const DropdownButton: React.FC<DropDownButtonProps> = (props) => {
  const { onChange } = props;

  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const [ selections, setSelections ] = React.useState<string[]>([]);

  const handleClick = (event: any) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleSelectItem = (event: any) => {
    const value: string = event.target.id;
    let state: boolean;
    let currentSelections: string[];
    if (!selections.includes(value)) {
      state = true;
      currentSelections = [...selections, value];
      setSelections([...selections, value]);
    }
    else {
      state = false;
      currentSelections = selections.filter(sel => sel !== value);
      setSelections(selections.filter(sel => sel !== value));
    }
    if (onChange) {
      onChange(currentSelections, value, state);
    }
  };

  return (
    <Box>
      <Button 
        aria-controls="simple-menu" 
        aria-haspopup="true"
        variant={props.variant}
        startIcon={props.icon}
        onClick={handleClick}>
        {props.name}
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={open}
        onClose={handleClose}
      >
        {
          props.items.map(item => (
            <MenuItem id={item.value} onClick={handleSelectItem}>
              <Checkbox
                id={item.value} checked={selections.indexOf(item.value) > -1}
              />
              {item.text}
            </MenuItem>
          ))
        }
      </Menu>
    </Box>
  );
}

export default DropdownButton;
