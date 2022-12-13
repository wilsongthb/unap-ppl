import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route  } from 'react-router-dom';
import Home from "./pages/Home.js";
import Store from "./pages/Store.js";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route index element={<Home />} />
          <Route path="store" element={<Store />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
