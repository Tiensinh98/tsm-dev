import React from 'react';
import Box from '@mui/material/Box';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';

interface ComboBoxOption {
  text: string
  value: any
}

interface ComboBoxModel {
  options: ComboBoxOption[]
  title?: string | null
  onChange?: (value: any) => void
}


export const ComboBox: React.FC<ComboBoxModel> = (props) => {
  const [value, setValue] = React.useState('');

  const handleChange = (event: any) => {
    setValue(event.target.value);
    if (props.onChange) {
      props.onChange(event.target.value);
    }
  };

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">{props.title}</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={value}
          label={props.title}
          onChange={handleChange}
        >
          {
            props.options.map(option => (
              <MenuItem value={option.value}>{option.text}</MenuItem>
            ))
          }
        </Select>
      </FormControl>
    </Box>
  );
} 
