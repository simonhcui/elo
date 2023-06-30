import React, { useMemo } from "react";
import { useTable, useSortBy } from "react-table";
import { Scrollbars } from "react-custom-scrollbars";
import WINRATE_DATA from "./WINRATE_ELO_DATA.json";
import { COLUMNS } from "./WinrateEloColumns";
import "./table.css";

export const WinrateEloTable = () => {
  const columns = useMemo(() => COLUMNS, []);
  const data = useMemo(() => WINRATE_DATA, []);

  const tableInstance = useTable(
    {
      columns,
      data,
    },
    useSortBy
  );

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    tableInstance;

  return (
    <Scrollbars style={{ justifyContent: "right", width: 900, height: 1200 }}>
      <table {...getTableProps()}>
        <thead>
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th {...column.getHeaderProps(column.getSortByToggleProps())}>
                  {column.render("Header")}
                  <span>
                    {column.isSorted
                      ? column.isSortedDesc
                        ? " 🔽"
                        : " 🔼"
                      : ""}
                  </span>
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {rows.map((row) => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()}>
                {row.cells.map((cell) => {
                  return (
                    <td {...cell.getCellProps()}>{cell.render("Cell")}</td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
    </Scrollbars>
  );
};
