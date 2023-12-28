import React, { useEffect, useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import BasicTable from './Table';
import axios from 'axios';


const createData = ( name, calories, fat, carbs, protein) => {
  return { name, calories, fat, carbs, protein };
}

const PROJECT_FIELD_TO_GUI_NAME = {
  issue_name: "Project Name",
  project_leader: "Leader",
  start_date: "Start Date",
  due_date: "Due Date",
  status: "Status",
  priority: "Priority"
}

const Project = () => {

  const [rows, setRows] = useState([
  ]);
  const [columns, setColumns] = useState(PROJECT_FIELD_TO_GUI_NAME);

  useEffect(() => {
    const fetchTableData = async () => {
      const response = await axios.get("/api/projects/");
      let data = [];
      response.data.forEach(d => {
        const sd = Object.fromEntries(
          Object.entries(d).filter(([key, _]) => (Object.keys(PROJECT_FIELD_TO_GUI_NAME).concat(["id"])).includes(key))
        );
        data.push(sd);

      });
      setRows(data);
    }
    fetchTableData();
  }, []); // run useEffect when variables in squared bracket changed

  return (
    <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
      <Col className="d-flex flex-column align-items-center">
        <Row>Welcome!</Row>
        <Row>Welcome To Task Management System!</Row>
        <Row>This is the project page where shows all projects!</Row>
        <BasicTable rows={rows} columns={columns}/>
        <Row>
          <Button href='/tasks'>Show Tasks</Button>
        </Row>
      </Col>
    </Container>
  );
};

export default Project;