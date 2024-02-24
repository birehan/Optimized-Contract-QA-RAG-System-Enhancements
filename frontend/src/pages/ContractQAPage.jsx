import { useState } from "react";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import LizzyAIChips from "../components/LizzyAIChips";
import Sidebar from "../components/Sidebar";
import ChatContainer from "../components/ChatContainer";

const ContractQAPage = () => {
  const [isContractCreated, setIsContractCreated] = useState(false);

  return (
    <div className="flex h-screen">
      <Sidebar setIsContractCreated={setIsContractCreated}/>
      
      {
        isContractCreated ?  <ChatContainer /> : <LizzyAIChips />
      }
    </div>
  );
};

export default ContractQAPage;