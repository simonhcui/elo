import React from "react";
import HomeIcon from "@mui/icons-material/Home";
import DoubleMasters from "./2x2.svg";
import MH1 from "./mh1.svg";
import MH2 from "./mh2.svg";
import SeasonOne from "./seasonone.svg";
import Lifetime from "./lifetime.svg";

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
    title: "MH1",
    icon: <img width="40px" src={MH1} />,
    link: "/mh1",
  },
  {
    title: "MH2",
    icon: <img width="40px" src={MH2} />,
    link: "/mh2",
  },
  {
    title: "Season 1",
    icon: <img width="40px" src={SeasonOne} />,
    link: "/seasonone",
  },
  {
    title: "Lifetime Stats",
    icon: <img width="40px" src={Lifetime} />,
    link: "/lifetime",
  },
];
