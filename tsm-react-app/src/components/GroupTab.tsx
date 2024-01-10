import React from 'react';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';

const a11yProps = (index: number) => {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}


interface TabContentProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}


interface GroupTabProps {
  children?: any;
  labels: string[];
}


const TabContent: React.FC<TabContentProps> = (props) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}


export const GroupTab: React.FC<GroupTabProps> = (props) => {
  const { labels, children } = props;

  const [tabIndex, setTabIndex] = React.useState(0);

  const handleChangeTab = (event: React.SyntheticEvent, tabIndex: number) => {
    setTabIndex(tabIndex);
  };

  return (
    <Box sx={{ width: '100%' }}>
      <Box 
        sx={{ borderBottom: 1, borderColor: 'divider' }}>
        <Tabs 
          value={tabIndex} 
          onChange={handleChangeTab} 
          aria-label="basic tabs example" 
          textColor="secondary">
          {labels.map(
            (label, index) => <Tab 
              label={label} {...a11yProps(index)} />
            )
          }
        </Tabs>
      </Box>
      {children?.map(
          (child: React.ReactNode, index: number) => <TabContent 
            value={tabIndex} 
            index={index}>
            {child}
          </TabContent>
        )
      }
    </Box>
  );
};