import React from 'react';
import TextField from '@mui/material/TextField';

interface TextInputProps {
  value: string;
  label?: string;
  name?: string;
  type?: string;
  onChange?: (name: string, value: string) => void;
};

export const TextInput: React.FC<TextInputProps> = (props) => {
  const { value, label, name, type, onChange } = props;

  const handleOnChange = (event: React.ChangeEvent) => {
    const target: any = event.target;
    if (onChange) onChange(target.name, target.value);
  }

  return (
    <TextField
      sx={{mt: 1}}
      fullWidth
      id="outlined-basic"
      name={name}
      label={label}
      value={value}
      type={type}
      variant="outlined"
      onChange={handleOnChange}
    />
  );
};