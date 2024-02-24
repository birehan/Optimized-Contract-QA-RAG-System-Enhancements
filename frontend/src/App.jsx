
import "./App.css";
import ContractQAPage from "./pages/ContractQAPage";
import { BrowserRouter, Route, Routes, } from 'react-router-dom'
import HomePage from "./pages/HomePage";
import RagEvaluationPage from "./pages/RagEvaluationPage";

function App() {
  return (
    <BrowserRouter>

      <Routes>
        <Route path="/contract-assistant" element={<ContractQAPage />} />
        <Route path="/" element={<HomePage />} />
        <Route path="/rag-evaluation" element={<RagEvaluationPage />} />



      </Routes>
  </BrowserRouter>
  );
}

export default App;
