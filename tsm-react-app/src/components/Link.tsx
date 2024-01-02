import React from 'react';

interface LinkProps {
  href: string
  text: string
};

export const Link: React.FC<LinkProps> = (props) => {

  return (
    <a href={props.href}>{props.text}</a>
  );
} 
