import React from "react";
import HomeIcon from "@mui/icons-material/Home";
import DoubleMasters from "./2x2.svg";

export const SidebarData = [
  {
    title: "Home",
    icon: <HomeIcon />,
    link: "/home",
  },
  {
    title: "2X2",
    icon: <img width="40px" src={DoubleMasters} />,
    link: "/2x2",
  },
  {
    title: "MH2",
    icon: <img width="40px" src={DoubleMasters} />,
    link: "/mh2",
  },
];
