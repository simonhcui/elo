import React, { useMemo } from "react";
import { useTable } from "react-table";
import { Scrollbars } from "react-custom-scrollbars";
import TROPHIES_DATA from "./CHAMPIONS_DATA.json";
import { COLUMNS } from "./ChampionsColumns";
import "./table.css";

export const AchievementsTable = () => {
  const columns = useMemo(() => COLUMNS, []);
  const data = useMemo(() => TROPHIES_DATA, []);

  const tableInstance = useTable({
    columns,
    data,
  });

  const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    tableInstance;

  return (
    <Scrollbars style={{ justifyContent: "right", width: 500, height: 800 }}>
      <table {...getTableProps()}>
        <thead>
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th {...column.getHeaderProps()}>{column.render("Header")}</th>
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
