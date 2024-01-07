import React from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';

interface DirectoryProps {
  dir: string;
  href: string;
};


interface DirectoryNavigatorProps {
  directories: DirectoryProps[];
};


export const DirectoryNavigator: React.FC<DirectoryNavigatorProps> = (props) => {
  const { directories } = props;

  return (
    <div role="presentation">
      <Breadcrumbs aria-label="breadcrumb">
        {directories.map((directory, index) => 
          <Link 
            underline="hover" 
            color={index === directories.length - 1 ? "text.primary" : "inherit"}
            href={directory.href}
            aria-current={index === directories.length - 1 ? "page" : undefined}
            fontSize={13}
          >
          {directory.dir}
          </Link>)
        }
      </Breadcrumbs>
    </div>
  );
}