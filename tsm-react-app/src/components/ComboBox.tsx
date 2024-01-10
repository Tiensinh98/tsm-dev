import React from 'react';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import { 
  Box, 
  Button, 
  InputLabel,
  MenuItem, 
  FormControl 
} from '@mui/material';

interface OptionProps {
  text: string
  value: string
  icon?: React.ReactNode;
}

interface ComboBoxProps {
  options: OptionProps[];
  value: string;
  title?: string | null;
  onChange?: (value: string) => void;
}


export const ComboBox: React.FC<ComboBoxProps> = (props) => {
  const { options, title, onChange, value } = props;
  const [currentValue, setCurrentValue] = React.useState<string>(value);

  const handleChange = (event: SelectChangeEvent) => {
    let value: string = event.target.value;
    setCurrentValue(value);
    if (onChange) {
      onChange(value);
    }
  };

  return (
    <Box sx={{mt: 1}}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">{props.title}</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={currentValue}
          label={title}
          onChange={handleChange}
        >
          {
            options.map(option => (
              <MenuItem key={option.value} value={option.value}>
                {option.icon ? <Button startIcon={option.icon}></Button> : null}
                {option.text}
              </MenuItem>
            ))
          }
        </Select>
      </FormControl>
    </Box>
  );
} 
