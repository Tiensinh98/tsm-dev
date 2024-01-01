import React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import { Button } from '@mui/material';

interface OptionProps {
  text: string
  value: string
  icon?: React.ReactNode;
}

interface ComboBoxProps {
  options: OptionProps[]
  title?: string | null
  onChange?: (value: string) => void
}


export const ComboBox: React.FC<ComboBoxProps> = (props) => {
  const { options, title, onChange } = props;
  const [currentValue, setCurrentValue] = React.useState<string>(options[0].value);

  const handleChange = (event: SelectChangeEvent) => {
    let value: string = event.target.value;
    setCurrentValue(value);
    if (onChange) {
      onChange(value);
    }
  };

  return (
    <div>
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
            props.options.map(option => (
              <MenuItem value={option.value}>
                {option.icon ? <Button startIcon={option.icon}></Button> : null}
                {option.text}
              </MenuItem>
            ))
          }
        </Select>
      </FormControl>
    </div>
  );
} 
