
import "./App.css";
import Home from "./pages/Home";
import { BrowserRouter, Route, Routes, } from 'react-router-dom'
import HomePage from "./pages/HomePage";

function App() {
  return (
    <BrowserRouter>
  
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<HomePage />} />


      </Routes>
  </BrowserRouter>
  );
}

export default App;
