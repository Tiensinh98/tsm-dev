import React, { useEffect } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

const Home = () => {

  return (
    <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
      <Col className="d-flex flex-column align-items-center">
        <Row>Welcome!</Row>
        <Row>Welcome To Task Management System!</Row>
        <Row>
          <Button href='/login'>Login</Button>
        </Row>
      </Col>
    </Container>
  );
};

export default Home;