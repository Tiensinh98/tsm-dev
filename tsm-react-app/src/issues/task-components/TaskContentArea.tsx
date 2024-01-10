import React from "react";
import { 
  Box, 
  Typography, 
  Button 
} from "@mui/material";

import { DirectoryNavigator } from "../../components/DirectoryNavigator";
import { InputFileUpload } from "../../components/UploadFileButton";


const directories = [
  {dir: "Projects", href: "/tsm-app/projects/"},
  {dir: "Akselos Modeler Development", href: "/tsm-app/projects/1/"},
  {dir: "AKS-1", href: "/tsm-app/tasks/1/"}
];

export const TaskContentArea: React.FC = () => {
  return (
    <Box>
      <DirectoryNavigator 
        directories={directories} />
      <Typography variant="h6">Task 1</Typography>
      <Typography variant="inherit">Description</Typography>
      <Typography variant="inherit">
        Hi Brian,
          This is the ticket for you!
        Best,
        Sinh
      </Typography>
      <InputFileUpload />
      <Button variant="contained">Sinh</Button>
    </Box>
  );
}