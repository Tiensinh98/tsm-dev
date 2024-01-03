import React from 'react';
import { Box } from '@mui/material';
import { Dayjs } from 'dayjs';
import TextField from '@mui/material/TextField';
import { EmptyDialog } from '../components/Dialog';
import { ComboBox } from '../components/ComboBox';
import { CustomDatePicker } from '../components/DatePicker';
import { Delete, Create } from '@mui/icons-material';

const projects = [
  {
    text: "Task 1",
    value: "task_1"
  },
  {
    text: "Task 2",
    value: "task_2"
  }
];

const users = [
  {
    text: "User 1",
    value: "user_1",
    icon: <Delete />
  },
  {
    text: "User 2",
    value: "user_2",
    icon: <Create />
  }
];

interface CreateTaskDialogProps {
  onAccepted: (project: string, assignee: string) => void;
  onClose: () => void;
}

export const CreateTaskDialog: React.FC<CreateTaskDialogProps> = (props) => {
  const { onAccepted, onClose } = props;
  const [ project, setProject ] = React.useState<any>([]);
  const [ assignee, setAssignee ] = React.useState<any>([]);
  const [ startDate, setStartDate ] = React.useState<Dayjs | null>(null);
  const [ endDate, setEndDate ] = React.useState<Dayjs | null>(null);
  const [ description, setDescription ] = React.useState('');

  React.useEffect(() => {
    setProject(projects[0]); // fetch projects
    setAssignee(users[0]); // fetch users
  }, []);

  const handleOnAccepted = () => {
    onAccepted(project.value, asignee.value);
  }

  const handleOnChange = (event: React.ChangeEvent) => {
    const target: any = event.target;
    setDescription(target.value);
  }

  return (
    <EmptyDialog
      title='Create task'
      onAccepted={handleOnAccepted}
      onClose={onClose}
    >
      <Box sx={{ display: 'flex', flexDirection: 'column'}}>
        <ComboBox
          title="Task"
          options={projects}
          value={projects[0].value}
          onChange={value => setProject(value)}
        />
        <ComboBox
          title="Asignee"
          options={users}
          value={users[0].value}
          onChange={value => setAssignee(value)}
        />
        <CustomDatePicker 
          label='Start date'
          onChange={date => setStartDate(date)}
        />
        <CustomDatePicker 
          label='Due date'
          onChange={date => setEndDate(date)}
        />
        <TextField
          sx={{mt: 1}}
          fullWidth
          id="outlined-basic" 
          label="Description"
          value={description}
          variant="outlined"
          onChange={handleOnChange}
        />
      </Box >
    </EmptyDialog>
  );
};