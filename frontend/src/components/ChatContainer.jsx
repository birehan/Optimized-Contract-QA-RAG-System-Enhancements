

import { useEffect, useState } from "react";
import { TypingIndicator } from "@chatscope/chat-ui-kit-react";
import { postChat } from "../api/chat_api";
import UploadFile from "./UploadFile";

const ChatContainer = () => {
  const [isTyping, setIsTyping] = useState(false);

  const [messages, setMessages] = useState([
    {
      role: "system",
      message:
        "Hello! I'm Lizzy AI, your Legal Contract Question and Answer Assistant. How can I assist you with your contract-related queries today?",
    },
  ]);
  const [inputMessage, setInputMessage] = useState("");

  const onSubmit = async (e) => {
    e.preventDefault();
    if (inputMessage.trim() === "") return; // Ignore empty messages

    const newMessage = { role: "user", message: inputMessage };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInputMessage("");

    try {
      setIsTyping(true)
      const response =  await postChat({ message: inputMessage });
      setIsTyping(false)
      const newMessage = {role: "system", message: response !== null ? response: "Some Error occured! please try again."}
    setMessages((prevMessages) => [...prevMessages, newMessage]);

    } catch (error) {
      const newMessage = {role: "system", message: "Some Error occured! please try again."}
    setMessages((prevMessages) => [...prevMessages, newMessage]);
      console.error("Error posting data:", error);
    }
  };

  useEffect(() => {
    const handleKeyPress = (e) => {
      if (e.key === "Enter" && inputMessage.trim() !== "") {
        onSubmit(e);
      }
    };

    document.addEventListener("keypress", handleKeyPress);

    return () => {
      document.removeEventListener("keypress", handleKeyPress);
    };
  }, [inputMessage]);

  return (
    <div className="flex flex-col items-center content-center flex-1 mx-64 mb-4 justify-center">
      <div className="relative w-full  p-6  overflow-y-autospace-y-4  flex-1">
        <ul className="space-y-4">
          {messages.map((message, index) => {
            return (
              <li
                key={index}
                className={`flex justify-${message.role === "system" ? "start" : "end"} gap-3`}
              >
                {message.role === "system" ? (
                  <svg
                    width="30"
                    height="40"
                    viewBox="0 0 30 40"
                    fill="none"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      d="M6.82862 27.4869C3.37929 27.4869 0.583008 24.0207 0.583008 19.7458C0.583008 15.4708 3.37929 12.0046 6.82862 12.0046V27.4869Z"
                      fill="#8A21C4"
                    ></path>
                    <path
                      d="M10.8403 39.2787V0.212769C10.8403 0.212769 24.985 1.05892 29.6049 6.61501C29.6049 16.0281 30.0878 30.7118 10.8403 39.2787Z"
                      fill="#25A7FF"
                    ></path>
                  </svg>
                ) : null}

                <div
                  className={`relative max-w-2xl px-4 py-2 text-gray-700 rounded shadow ${
                    message.role === "system" ? "bg-white" : "bg-gray-100"
                  }`}
                >
                  <span className="block">{message.message}</span>
                </div>

                {message.role === "user" ? (
                  <span className="inline-flex h-10 w-10 items-center justify-center rounded-full bg-[#ac62d5] text-lg font-semibold">
                    <span className="font-medium leading-none text-white">U</span>
                  </span>
                ) : null}
              </li>
            );
          })}

          {isTyping ? (
            <div className="px-4 py-2">
              <TypingIndicator content="Lizzy is typing" />
            </div>
          ) : null}
        </ul>
      </div>
      <form className="flex items-center justify-between w-full p-3 border-gray-300" onSubmit={onSubmit}>

<UploadFile/>
          <input
            type="text"
            placeholder="Enter a question here"
            className="block w-full py-3.5 pl-4 mx-3 bg-[#f0f4f9] rounded-full outline-none focus:text-gray-700"
            name="message"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
          />

          <button type="submit">
            <svg
              className="w-7 h-7 text-gray-500 origin-center transform rotate-90"
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z" />
            </svg>
          </button>
      </form>

    </div>
  );
};


export default ChatContainer;

