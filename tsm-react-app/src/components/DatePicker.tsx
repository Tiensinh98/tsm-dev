import React from 'react';
import { Dayjs } from 'dayjs';
import { DemoContainer } from '@mui/x-date-pickers/internals/demo';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';


interface CustomDatePickerProps {
  label: string;
  onChange?: (
    year: number | undefined, 
    month: number | undefined, 
    date: number | undefined
  ) => void;
}


export const CustomDatePicker: React.FC<CustomDatePickerProps> = (props) => {
  const { label, onChange } = props;

  const [currentDate, setCurrentDate] = React.useState<Dayjs | null>(null);

  const handleOnDatechange = (value: Dayjs | null) => {
    setCurrentDate(value);
    if (onChange) onChange(value?.year(), value?.month(), value?.date());
  }

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <DemoContainer components={['DatePicker']}>
        <DatePicker
          label={label}
          value={currentDate}
          onChange={(value) => handleOnDatechange(value)}
         />
      </DemoContainer>
    </LocalizationProvider>
  );
}