import React from 'react';
import { Grid } from '@mui/material';
import { useSelector, useDispatch } from 'react-redux';
import axios from 'axios';

import { ReviewCard } from '../components/Card';
import { ImageAvatar } from '../components/Avatar';
import { Link } from '../components/Link';
import { ResponsiveAppBar } from '../appbar/AppBar';
import { AppState } from '../redux/reducers';
import { ProjectState } from '../redux/reducers/issues/projectListReducer';
import { projectListLoad } from '../redux/actions/issues/projectListAction';


export const ProjectListPage: React.FC = () => {
  const dispatch = useDispatch();
  const projectData: ProjectState[] = useSelector((state: AppState) => state.projectListState);

  React.useEffect(() => {
    (async ()=> {
      const response = await axios.get("/api/projects/");
      dispatch(projectListLoad(response.data));
    })();
  }, [])

  return (
      <ResponsiveAppBar>
        <Grid container 
          sx={{
            display: 'flex',
            flexDirection: "column",
            alignItems: "center", 
            justifyContent: "center"
          }} 
          lg={12} 
          rowSpacing={10} 
          padding={5}>
          {projectData.map(project =>
            <Grid item>
              <ReviewCard
                primaryKey={project.id} 
                avatar={<ImageAvatar
                  alt={project.leader ? `${project.leader.firstName} ${project.leader.lastName}`: ''} 
                  link={`/users/${project.id}/`} />}
                title={<Link text={project.name} href={`/tsm-app/projects/${project.id}/`} />}
                subHeader={`${project.startDate} to ${project.dueDate}`}
                description={project.description}
                image='https://picsum.photos/200'
              />
            </Grid>
          )}
        </Grid>
      </ResponsiveAppBar>
  );
};