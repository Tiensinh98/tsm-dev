import React from 'react';
import { 
  Grid,
  TextField
} from '@mui/material';
import { Dayjs } from 'dayjs';
import { Delete, Create } from '@mui/icons-material';

import { EmptyDialog } from '../components/Dialog';
import { ComboBox } from '../components/ComboBox';
import { CustomDatePicker } from '../components/DatePicker';

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
  const setStartDate = React.useState<Dayjs | null>(null)[1];
  const setEndDate = React.useState<Dayjs | null>(null)[1];
  const [ description, setDescription ] = React.useState('');

  React.useEffect(() => {
    setProject(projects[0]); // fetch projects
    setAssignee(users[0]); // fetch users
  }, []);

  const handleOnAccepted = () => {
    onAccepted(project.value, assignee.value);
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
      <Grid item>
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
      </Grid>
    </EmptyDialog>
  );
};