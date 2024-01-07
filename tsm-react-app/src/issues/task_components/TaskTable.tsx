import React from 'react';
import { CustomTable } from '../../components/Table';
import { Box } from '@mui/material';
import { ComboBox } from '../../components/ComboBox';
import { ImageAvatar } from '../../components/Avatar';

const columns = [
  {
    key: "id",
    label: "Key",
    minWidth: 40,
    align: "left"
  },
  {
    key: "name",
    label: "Summary",
    minWidth: 200,
    align: "center"
  },
  {
    key: "start_date",
    label: "Start date",
    minWidth: 60,
    align: "center"
  },
  {
    key: "asignee",
    label: "Asignee",
    minWidth: 60,
    align: "center",
    format: ImageAvatar
  },
  {
    key: "status",
    label: "Status",
    minWidth: 60,
    align: "center",
    format: ComboBox
  }
]

export const TaskTable: React.FC = () => {

  const [ rows, setRows ] = React.useState<any[]>([]);

  React.useEffect(() => {
    let currentRows = [
      {
        id: 0,
        name: "Task 1",
        start_date: "2023-10-01",
        end_date: "2023-12-01",
        asignee: {
          alt: "Sinh Pham",
          link: "https://youtube.com/"
        },
        status: {
          options: [
            {
              text: "To Do",
              value: "to_do"
            },
            {
              text: "Done",
              value: "done"
            }
          ],
          value: "to_do",
          onChange: () => console.log("Changing")
        }
      },
      {
        id: 1,
        name: "Task 2",
        start_date: "2023-10-01",
        end_date: "2023-12-01",
        asignee: {
          alt: "Sac Pham",
          link: "https://youtube.com/"
        },
        status: {
          options: [
            {
              text: "To Do",
              value: "to_do"
            },
            {
              text: "Done",
              value: "done"
            }
          ],
          value: "done",
          onChange: () => console.log("Changing")
        }
      }
    ];
    setRows(currentRows);
  }, []);

  return (
    <CustomTable
      page={0} 
      rowsPerPage={10} 
      columns={columns}
      rows={rows}
      rowsPerPageOptions={[10, 20, 30]}
    />
  );
}