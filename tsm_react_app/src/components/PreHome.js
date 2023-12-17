import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const PreHome = () => {

  const navigate = useNavigate();

  const navigateLogin = () => {
    try {
      navigate('/login/');
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
        <button onClick={navigateLogin}>Login</button>
    </div>
  );
};

export default PreHome;