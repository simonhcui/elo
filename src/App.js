import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Sidebar from "./Components/Sidebar";
import Home from "./Pages/home";
import DoubleMasters from "./Pages/doublemasters";
import ModernHorizonsOne from "./Pages/modernhorizonsone";
import ModernHorizonsTwo from "./Pages/modernhorizonstwo";
import SeasonOne from "./Pages/seasonone";
import SeasonTwo from "./Pages/seasontwo";
import SeasonThree from "./Pages/seasonthree";
import SeasonFour from "./Pages/seasonfour";
import SeasonFive from "./Pages/seasonfive";
import Lifetime from "./Pages/lifetime";
import Chaos from "./Pages/chaos";

function App() {
  return (
    <Router>
      <Sidebar />
      <Routes>
        <Route exact path="/" element={<Navigate replace to="/home" />} />
        <Route path="/home" element={<Home />} />
        <Route path="/2x2" element={<DoubleMasters />} />
        <Route path="/mh1" element={<ModernHorizonsOne />} />
        <Route path="/mh2" element={<ModernHorizonsTwo />} />
        <Route path="/seasonone" element={<SeasonOne />} />
        <Route path="/seasontwo" element={<SeasonTwo />} />
        <Route path="/seasonthree" element={<SeasonThree />} />
        <Route path="/seasonfour" element={<SeasonFour />} />
        <Route path="/seasonfive" element={<SeasonFive />} />
        <Route path="/lifetime" element={<Lifetime />} />
        <Route path="/chaos" element={<Chaos />} />
      </Routes>
    </Router>
  );
}

export default App;
