import React from "react";
import HomeIcon from "@mui/icons-material/Home";
import DoubleMasters from "./2x2.svg";
import MH1 from "./mh1.svg";
import MH2 from "./mh2.svg";
import SeasonOne from "./seasonone.svg";
import SeasonTwo from "./seasontwo.svg";
import SeasonThree from "./seasonthree.svg";
import SeasonFour from "./seasonfour.svg";
import SeasonFive from "./seasonfive.svg";
import SeasonSix from "./seasonsix.svg"
import Lifetime from "./lifetime.svg";
import Chaos from "./chaos.svg";
import DMR from"./dmr.svg";

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
    title: "Chaos",
    icon: <img width="40px" src={Chaos} />,
    link: "/chaos",
  },
  {
    title: "DMR",
    icon: <img width="40px" src={DMR} />,
    link: "/dmr",
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
    title: "Season 2",
    icon: <img width="40px" src={SeasonTwo} />,
    link: "/seasontwo",
  },
  {
    title: "Season 3",
    icon: <img width="40px" src={SeasonThree} />,
    link: "/seasonthree",
  },
  {
    title: "Season 4",
    icon: <img width="40px" src={SeasonFour} />,
    link: "/seasonfour",
  },
  {
    title: "Season 5",
    icon: <img width="40px" src={SeasonFive} />,
    link: "/seasonfive",
  },
  {
    title: "Season 6",
    icon: <img width="40px" src={SeasonSix} />,
    link: "/seasonsix",
  },
  {
    title: "Lifetime Stats",
    icon: <img width="40px" src={Lifetime} />,
    link: "/lifetime",
  },
];
