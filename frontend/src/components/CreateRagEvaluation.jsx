
import { useEffect, useState } from "react";
import Modal from "react-modal";
import { PlusIcon, XMarkIcon } from "@heroicons/react/20/solid";
import { useForm, FormProvider } from "react-hook-form";
import DropDownInput from "./DropDownInput";
import { fetchContractOptions, createRag } from "../api/chat_api";
import Notification from "./Notification";

const CreateRagEvaluation = () => {
  const [showModal, setShowModal] = useState(false);
  const [ragOptions, setRagOptions] = useState([]);
  const [notification, setNotification] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    // Function to fetch contract options and update state
    const fetchData = async () => {
      try {
        const options = await fetchContractOptions();
        if (options) {
          setRagOptions(options); // Update state with fetched options
        } else {
          console.error("Failed to fetch contract options");
        }
      } catch (error) {
        console.error("Error fetching contract options:", error);
      }
    };

    fetchData(); // Call the fetchData function when the component mounts
  }, []); 

  const onSubmit = async (data) => {
    try {
      setIsLoading(true)
      const response = await createRag(data);
      setIsLoading(false)

      console.log("response: ", response);
      if (response != null) {
        // Show success notification and close modal
        setNotification({ message: "Rag created successfully", success: true });
        setShowModal(false);

      } else {
        // Show error notification
      

        setNotification({ message: response.message, success: false });
      }

    } catch (error) {
      console.error("Error creating rag:", error);
      // Show error notification
      setNotification({
        message: "An error occurred while creating rag",
        success: false,
      });
    }
  };

  // const methods = useForm<any>();
  const methods = useForm({
    defaultValues: {},
  });

  useEffect(() => {
    if (ragOptions) {
      var default_values = {};
      for (let i = 0; i < ragOptions.length; i++) {
        default_values[ragOptions[i].name] = ragOptions[i].items[0]["key"];
      }

      methods.reset(default_values);
    }
  }, [ragOptions, methods]);

  return (
    <div style={{ zIndex: "1000" }}>
      
      <div>
        <div
          className="modal-container bg-white border-2 border-gray-200 rounded-lg p-8 join-waitlist-box box-border shadow-welcome fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2"
       
        >
          <FormProvider {...methods}>
            <form
              className="relative "
              onSubmit={methods.handleSubmit(onSubmit)}
            >
              <div className="bg-white rounded-lg px-4 py-6 mx-auto max-w-md">
                <div className="flex items-end justify-end">
                  <button
                    className="absolute top-0 right-0 text-gray-500 hover:text-gray-700"
                    onClick={() => setShowModal(false)}
                  >
                    <XMarkIcon className="h-7 w-7" aria-hidden="true" />
                  </button>
                </div>
                <div className="mt-4">
                  <div className="flex font-sans justify-center font-semibold text-2xl pt-2 bg-white">
                    <h1>Create Rag Evaluation</h1>
                  </div>
                  <div className="w-96 mt-4 flex flex-col gap-6">
                    {ragOptions.length &&
                      ragOptions.map((ragOption, index) => {
                        return (
                          <DropDownInput
                            key={index}
                            label={ragOption.label}
                            items={ragOption.items}
                            name={ragOption.name}
                          />
                        );
                      })}

                    <div className="flex justify-end submit-center relative mt-5 px-6">
                      <button
                        disabled={isLoading}
                        id="signInButton"
                        type="submit"
                        className={` bg-[#25a7ff] flex justify-center text-cneter text-white w-full hover:bg-blue-300 focus:ring-4  rounded-lg px-3 py-2 text-center items-center bg-primary font-sans font-semibold text-base h-11`}
                      >
                        {isLoading ? <div className="flex flex-row gap-2 items-center justify-center">
                          <svg
                            width="20"
                            height="20"
                            fill="currentColor"
                            className="mr-2 animate-spin"
                            viewBox="0 0 1792 1792"
                            xmlns="http://www.w3.org/2000/svg"
                          >
                            <path d="M526 1394q0 53-37.5 90.5t-90.5 37.5q-52 0-90-38t-38-90q0-53 37.5-90.5t90.5-37.5 90.5 37.5 37.5 90.5zm498 206q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm-704-704q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm1202 498q0 52-38 90t-90 38q-53 0-90.5-37.5t-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm-964-996q0 66-47 113t-113 47-113-47-47-113 47-113 113-47 113 47 47 113zm1170 498q0 53-37.5 90.5t-90.5 37.5-90.5-37.5-37.5-90.5 37.5-90.5 90.5-37.5 90.5 37.5 37.5 90.5zm-640-704q0 80-56 136t-136 56-136-56-56-136 56-136 136-56 136 56 56 136zm530 206q0 93-66 158.5t-158 65.5q-93 0-158.5-65.5t-65.5-158.5q0-92 65.5-158t158.5-66q92 0 158 66t66 158z"></path>
                          </svg>
                          loading
                        </div>: "Submit Form"}
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </form>
          </FormProvider>
        </div>
      </div>
      {notification && (
        <Notification
        setNotification={setNotification}
          message={notification.message}
          success={notification.success}
        />
      )}
    </div>
  );
};

export default CreateRagEvaluation;
