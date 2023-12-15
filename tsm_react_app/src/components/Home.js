// src/components/Home.js

import React, { useEffect } from 'react';

const Home = () => {
    useEffect(async () => {
        const data = await fetch('/projects/');
        console.log(data.json())
    });

  return (
    <div>
      <h2>Welcome to the Home Page!</h2>
    </div>
  );
};

export default Home;