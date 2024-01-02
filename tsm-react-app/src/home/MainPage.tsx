import React from 'react';
import { useNavigate } from 'react-router-dom';
import { ResponsiveAppBar } from '../components/AppBar';
import axios from 'axios';
import { Box } from '@mui/material';
import { ReviewCard } from '../components/Card';
import { ImageAvatar } from '../components/Avatar';
import { Link } from '../components/Link';
import { Notification } from '../components/Notification';

const projectInfos = [
  "name",
  "leader",
  "start_date",
  "due_date",
  "status",
  "priority" 
];


export const HomePage: React.FC = () => {
  const navigate = useNavigate();  // Use the useNavigate hook

  const [projectData, setProjectData] = React.useState<any[]>([]);
  const [ errorDelete, setErrorDelete ] = React.useState<boolean>(false);

  React.useEffect(() => {
    const fetchProjects = async () => {
      const response = await axios.get("/api/projects/");
      const data: any[] = response.data;
      let rows = [];
      for (const d of data) {
        let row: any = {};
        for (const field of projectInfos) {
            row[field] = d[field];
        }
        row["id"] = d.id;
        rows.push(row);
      }
      setProjectData(rows);
    }
    fetchProjects();
  }, []);

  const handleDeleteProject = async (projectId: number) => {
    try {
        const response = await axios.delete(`/api/projects/${projectId}/`);
        if (response.data.success) {
            navigate("/tsm-app/");
        }
    }
    catch {
        setErrorDelete(true);
    }
  }


  return (
    <Box>
      <ResponsiveAppBar appName="TSM" />
      {projectData.map(project =>
        <ReviewCard
            primaryKey={project["id"]}
            avatar={ <ImageAvatar alt={project["leader"]} link={`/people/${project["leader"]}/`}/> }
            title={ <Link href={`/projects/${project["id"]}/`} text={project["name"]} />}
            subHeader={ project["start_date"]}
            description={project["description"]}
            image="https://picsum.photos/200/300"
            onDelete={handleDeleteProject}
        />)
      }
      <Notification
        severity="error" 
        message="Error while deleting Project!"
        open={errorDelete}
      />
    </Box>
  );
};