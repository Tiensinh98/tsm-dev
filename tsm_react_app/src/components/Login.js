import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Button, Container, Tab, Tabs } from 'react-bootstrap';
import axios from 'axios';

const Login = () => {

  const [loginInfo, setLoginInfo] = useState({
    username: "",
    password: ""
  });
  const [registerInfo, setRegisterInfo] = useState({
    username: "",
    email: "",
    password: "",
    confirmedPassword: ""
  });

  const handleChangeLoginInfo = (event) => {
    debugger;
    setLoginInfo({
      ...loginInfo,
      [event.target.name]: event.target.value
    });
  };

  const handleChangeRegisterInfo = (event) => {
    setRegisterInfo({
      ...registerInfo,
      [event.target.name]: event.target.value
    });
  };


  const navigate = useNavigate();  // Use the useNavigate hook

  const handleLoginSubmit = async (event) => {
    event.preventDefault();
    const response = await axios.post("/api/login/", loginInfo);
    if (!response.data.success) navigate("/login/");
    else navigate("/tsm-app/");
  };

  const handleRegistrationSubmit = async (event) => {
    event.preventDefault();
    const response = await axios.post("/api/register/", registerInfo);
    if (!response.data.success) navigate("/login/");
    else navigate("/tsm-app/");
  };

  return (
    <Tabs defaultActiveKey="profile" id="uncontrolled-tab-example" className="mb-3">
      <Tab eventKey="home" title="Login">
        <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
          <div className="w-100" style={{ maxWidth: "400px" }}>
            <Form onSubmit={handleLoginSubmit}>
              <Form.Group className="mb-3" controlId="l-formBasicUserName">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  placeholder="Enter username"
                  value={loginInfo.username}
                  name="username"
                  onChange={handleChangeLoginInfo} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="l-formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  value={loginInfo.password}
                  name="password"
                  onChange={handleChangeLoginInfo} />
                <Form.Text className="text-muted">
                  We'll never share your password with anyone else.
                </Form.Text>
              </Form.Group>
              <Button variant="link" href="/password-reset">Forget password?</Button>
              <Button variant="primary" type="submit">
                Login
              </Button>
            </Form>
          </div>
        </Container>
      </Tab>
      <Tab eventKey="profile" title="Registration">
        <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
          <div className="w-100" style={{ maxWidth: "400px" }}>
            <Form onSubmit={handleRegistrationSubmit}>
              <Form.Group className="mb-3" controlId="r-formBasicUsername">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  placeholder="Enter username"
                  value={registerInfo.username}
                  name="username"
                  onChange={handleChangeRegisterInfo} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="r-formBasicEmail">
                <Form.Label>Email</Form.Label>
                <Form.Control
                  type="email"
                  placeholder="Enter email"
                  value={registerInfo.email}
                  name="email"
                  onChange={handleChangeRegisterInfo} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="r-formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  value={registerInfo.password}
                  name="password"
                  onChange={handleChangeRegisterInfo} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="r-formBasicConfirmedPassword">
                <Form.Label>Confirmed Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Confirmed Password"
                  value={registerInfo.confirmedPassword}
                  name="confirmedPassword"
                  onChange={handleChangeRegisterInfo} />
                <Form.Text className="text-muted">
                  We'll never share your password with anyone else.
                </Form.Text>
              </Form.Group>
              <Button variant="primary" type="submit">
                Register
              </Button>
            </Form>
          </div>
        </Container>
      </Tab>
    </Tabs>
  );
};

export default Login;