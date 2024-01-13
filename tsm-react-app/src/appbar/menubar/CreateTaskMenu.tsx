import React from 'react';
import { Button, Grid } from '@mui/material';
import { useSelector, useDispatch } from "react-redux";
import axios from 'axios';

import { EmptyDialog } from '../../components/Dialog';
import { ComboBox } from '../../components/ComboBox';
import { CustomDatePicker } from '../../components/DatePicker';
import { AppState } from '../../redux/reducers';
import { ProjectState } from '../../redux/reducers/issues/projectListReducer';
import { projectListLoad } from '../../redux/actions/issues/projectListAction';
import { TextInput } from '../../components/TextInput';


const users = [
  {
    text: "User 1",
    value: "2",
  },
  {
    text: "User 2",
    value: "4",
  }
];

const PRIORITIES = [
  {
    text: "Highest",
    value: "highest",
  },
  {
    text: "High",
    value: "high",
  },
  {
    text: "Medium",
    value: "medium",
  }
  ,
  {
    text: "Low",
    value: "low",
  }
];

export const CreateTaskMenu: React.FC = () => {
  const dispatch = useDispatch();
  const csrfToken: any = useSelector((state: AppState) => state.csrfToken);
  const projectData: ProjectState[] = useSelector((state: AppState) => state.projectListState);

  const [ targetProjectId, setTargetProjectId ] = React.useState<string | null>(null);
  const [ assigneeId, setAssigneeId ] = React.useState<string | null>(null);
  const [ summary, setSummary ] = React.useState<string>('');
  const [ startDate, setStartDate ] = React.useState<string | null>(null);
  const [ dueDate, setDueDate ] = React.useState<string | null>(null);
  const [ priority, setPriority ] = React.useState<string>('medium');
  const [ open, setOpen ] = React.useState<boolean>(false);

  const handleCreateTask = async () => {
    try {
      const response = await axios.post("/api/tasks/add/", {
        lineProject: targetProjectId ? parseInt(targetProjectId) : null,
        assignee: assigneeId ? parseInt(assigneeId) : null,
        name: summary,
        startDate,
        dueDate,
        priority,
        headers: {
          'X-CSRFToken': csrfToken.data.csrfToken
        }
      });
      setOpen(false);
    }
    catch {
      console.error("Errors while creating task!");
    }
  }

  React.useEffect(() => {
    (async ()=> {
      const response = await axios.get("/api/projects/");
      dispatch(projectListLoad(response.data));
    })();
  }, [])

  return (
    <React.Fragment>
      <Button
        sx={{ my: 2, color: 'white', display: 'block' }}
        onClick={ () => setOpen(true) }>
        Create
      </Button>
      <EmptyDialog
        open={open}
        title='Create task'
        onAccepted={handleCreateTask}
        onClose={ () => setOpen(false) }
      >
        <Grid container rowSpacing={1}>
          <Grid item xs={12} lg={12}>
            <TextInput value={summary}
              label="Summary" onChange={ (name, value) => setSummary(value) }
            />
          </Grid>
          <Grid item xs={12} lg={12}>
            <ComboBox title="Project"
              options={projectData.map(({ id, name }) => {
                return { text: name, value: id.toString(), icon: 'https://picsum.photos/200' }
              })}
              value={targetProjectId}
              onChange={ (value) => setTargetProjectId(value) }
            />
          </Grid>
          <Grid item xs={12} lg={12}>
            <ComboBox title="Asignee" 
              options={users}
              value={assigneeId}
              onChange={ (value) => setAssigneeId(value) }
            />
          </Grid>
          <Grid item xs={12} lg={12}>
            <CustomDatePicker label='Start date'
              onChange={ (year, month, date) => setStartDate(`${year}-${month}-${date}`) }
            />
          </Grid>
          <Grid item xs={12} lg={12}>
            <CustomDatePicker label='Due date'
              onChange={ (year, month, date) => setDueDate(`${year}-${month}-${date}`) }
            />
          </Grid>
          <Grid item xs={12} lg={12}>
            <ComboBox title="Priority" options={PRIORITIES} 
              value={priority}
              onChange={ (value) => setPriority(value) }
            />
          </Grid>
        </Grid>
      </EmptyDialog>
    </React.Fragment>
  );
};