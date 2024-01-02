import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Form, Button, Container } from 'react-bootstrap';
import axios from 'axios';
import { GroupTab } from '../components/GroupTab';

export const AuthenticationPage: React.FC = () => {
  const navigate = useNavigate();  // Use the useNavigate hook

  const [ username, setUsername ] = React.useState<string>('');
  const [ email, setEmail ] = React.useState<string>('');
  const [ password, setPassword ] = React.useState<string>('');
  const [ password2, setpassword2 ] = React.useState<string>('');

  const handleChange = (event: any) => {
    const target: any = event.target;
    const value: string = target.value;
    const name: string = target.name;
    const info: string = name.charAt(0).toUpperCase() + name.slice(1);
    eval(`set${info}("${value}")`);
  }

  const handleLogin = async (event: React.SyntheticEvent) => {
    event.preventDefault();
    const response = await axios.post("/api/login/", {
      username, password
    });
    if (!response.data.success) navigate("/login/");
    else navigate("/tsm-app/");
  };

  const handleRegister = async (event: React.SyntheticEvent) => {
    event.preventDefault();
    const response = await axios.post("/api/register/", {
      username, email, password
    });
    if (!response.data.success) navigate("/login/");
    else navigate("/tsm-app/");
  };

  return (
    <GroupTab labels={["Login", "Register"]}>
      <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
          <div className="w-100" style={{ maxWidth: "400px" }}>
            <Form onSubmit={handleLogin}>
              <Form.Group className="mb-3" controlId="l-formBasicUserName">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  placeholder="Enter username"
                  value={username}
                  name="username"
                  onChange={handleChange} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="l-formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  value={password}
                  name="password"
                  onChange={handleChange} />
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
        <Container className="d-flex align-items-center justify-content-center" style={{ minHeight: "100vh" }}>
          <div className="w-100" style={{ maxWidth: "400px" }}>
            <Form onSubmit={handleRegister}>
              <Form.Group className="mb-3" controlId="r-formBasicUsername">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  placeholder="Enter username"
                  value={username}
                  name="username"
                  onChange={handleChange} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="r-formBasicEmail">
                <Form.Label>Email</Form.Label>
                <Form.Control
                  type="email"
                  placeholder="Enter email"
                  value={email}
                  name="email"
                  onChange={handleChange} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="r-formBasicPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Password"
                  value={password}
                  name="password"
                  onChange={handleChange} />
              </Form.Group>
              <Form.Group className="mb-3" controlId="r-formBasicConfirmedPassword">
                <Form.Label>Confirmed Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Confirmed Password"
                  value={password2}
                  name="confirmedPassword"
                  onChange={handleChange} />
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
    </GroupTab>
  );
};