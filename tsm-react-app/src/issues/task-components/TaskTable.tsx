import React from 'react';
import { CustomTable } from '../../components/Table';


const COLUMNS = [
  { key: "id", label: "Key" },
  { key: "name", label: "Summary" },
  { key: "startDate", label: "Start date" },
  { key: "dueDate", label: "Due date" },
  { key: "asignee", label: "Asignee" },
  { key: "status", label: "Status" }
];

interface RowProps {
  id: React.ReactNode;
  name: React.ReactNode;
  startDate: React.ReactNode;
  dueDate: React.ReactNode;
  asignee: React.ReactNode;
  status: React.ReactNode;
}

interface TaskTableProps {
  rows: RowProps[]
}

export const TaskTable: React.FC<TaskTableProps> = (props) => {
  const { rows } = props;

  return (
    <CustomTable
      page={0}
      rowsPerPage={10}
      columns={ COLUMNS }
      rows={ rows }
      rowsPerPageOptions={[10, 20, 30]}
    />
  );
}