import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import BasicTable from './Table';
import axios from 'axios';

const PROJECT_FIELD_TO_GUI_NAME = {
  name: "Project Name",
  leader: "Leader",
  start_date: "Start Date",
  due_date: "Due Date",
  status: "Status",
  priority: "Priority"
}

const ProjectDetails = () => {
  const [rows, setRows] = useState([]);
  const { id } = useParams();
  const [columns, setColumns] = useState(PROJECT_FIELD_TO_GUI_NAME);

  useEffect(() => {
    const fetchTableData = async () => {
      debugger;
      const response = await axios.get(`/api/projects/${id}/`);
      let rows = [];
      const tableData = response.data;
      for (const data of tableData) {
        let row = {};
        for (const field of Object.keys(PROJECT_FIELD_TO_GUI_NAME)) {
          row[field] = data[field];
        }
        row["id"] = data.id;
        rows.push(row);
      }
      setRows(rows);
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

export default ProjectDetails;