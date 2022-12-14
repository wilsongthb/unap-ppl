// import logo from './logo.svg';
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home.js";
import Store from "./pages/Store.js";
import Navbar from "./components/Navbar.js";

function App() {
  return (
    <div className="App">
      <Navbar></Navbar>
      <div className="container">
        <BrowserRouter>
          <Routes>
            <Route index element={<Home />} />
            <Route path="store" element={<Store />} />
          </Routes>
        </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
