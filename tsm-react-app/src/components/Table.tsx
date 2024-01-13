import React from 'react';
import {
  Paper, Table, TableBody, TableCell, TableContainer,  
  TableHead, TablePagination, TableRow
} from '@mui/material';


interface TableColumnProps {
  key: string
  label: string
  minWidth?: number
  align?: any
  format?: any
};

interface TableProps {
  page: number
  rowsPerPage: number
  columns: TableColumnProps[]
  rows: any[]
  rowsPerPageOptions?: number[] | null
};

export const CustomTable: React.FC<TableProps> = (props) => {
  const [page, setPage] = React.useState(props.page);
  const [rowsPerPage, setRowsPerPage] = React.useState(props.rowsPerPage);

  const handleChangePage = (event: any, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: any) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };

  return (
    <Paper sx={{ overflow: 'hidden' }}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead>
            <TableRow>
              {props.columns.map((column) => (
                <TableCell
                  key={column.key}
                  align={column.align}
                  style={{ backgroundColor: "lightgrey" }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {props.rows
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.code}>
                    {props.columns.map((column) => {
                      const value = row[column.key];
                      return (
                        <TableCell key={column.key} align={column.align}>
                          {value}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={props.rowsPerPageOptions ? props.rowsPerPageOptions: [10, 15, 20]}
        component="div"
        count={props.rows.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  );
};