import React from 'react';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import { Avatar,  InputLabel, MenuItem,  FormControl } from '@mui/material';


interface OptionProps {
  text: string
  value: string
  icon?: string;
}

interface ComboBoxProps {
  options: OptionProps[];
  value?: string | null;
  title?: string | null;
  onChange?: (value: string) => void;
}


export const ComboBox: React.FC<ComboBoxProps> = (props) => {
  const { options, title, value, onChange} = props;
  const [currentValue, setCurrentValue] = React.useState<string | undefined>(value ? value : options[0]?.value);

  const handleChange = (event: SelectChangeEvent) => {
    let value: string = event.target.value;
    setCurrentValue(value);
    if (onChange) {
      onChange(value);
    }
  };

  return (
    <React.Fragment>
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
                {option.icon ? <Avatar sx={{mr: 2}} src={option.icon}></Avatar> : null}
                {option.text}
              </MenuItem>
            ))
          }
        </Select>
      </FormControl>
    </React.Fragment>
  );
} 
