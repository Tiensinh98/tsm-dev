import React from 'react';

interface LinkModel {
  href: string
  text: string
};

export const Link: React.FC<LinkModel> = (props) => {

  return (
    <a href={props.href}>{props.text}</a>
  );
} 
