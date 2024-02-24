import { useEffect, useState } from 'react';
import { uploadFile } from '../api/chat_api';
import Notification from './Notification';

const UploadFile = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [notification, setNotification] = useState(null);

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    setSelectedFile(file);
  };

  useEffect(() => {
    const uploadSelectedFile = async () => {
      if (selectedFile) {
        // Check if the selected file type is allowed
        const allowedTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
        if (!allowedTypes.includes(selectedFile.type)) {
          setNotification({ message: 'Only PDF, DOCX, and TXT files are allowed.', success: false });
          setSelectedFile(null); // Reset selected file
          return;
        }

        // Start loading
        setLoading(true);

        // Call the API to upload the file
        try {
          const response = await uploadFile(selectedFile);
          console.log('File uploaded successfully:', response);
          setNotification({ message: 'File uploaded successfully', success: true });
          // Reset selected file
          setSelectedFile(null); 
        } catch (error) {
          console.error('Error uploading file:', error);
          setNotification({ message: 'Error uploading file. Please try again later.', success: false });
          // Reset selected file
          setSelectedFile(null); 
        } finally {
          // Stop loading
          setLoading(false);
        }
      }
    };

    uploadSelectedFile();
  }, [selectedFile]);

  return (
    <div className="relative">
      {/* Loading spinner covering the whole screen */}
      {loading && (
        <div className="fixed inset-0 flex items-center justify-center bg-gray-300 bg-opacity-75 z-50">
          <div className="animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-gray-900"></div>
        </div>
      )}

      <button className="relative z-10">
        <input type="file" accept=".pdf,.docx,.txt" onChange={handleFileChange} className="absolute inset-0 w-full h-full opacity-0 cursor-pointer" />

        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="w-7 h-7 text-gray-500"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"
          />
        </svg>
      </button>

      {notification && (
        <Notification
          message={notification.message}
          success={notification.success}
        />
      )}
    </div>
  );
};

export default UploadFile;
