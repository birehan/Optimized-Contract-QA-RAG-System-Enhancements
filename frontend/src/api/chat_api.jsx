import axios from 'axios';
const baseUrl = "http://127.0.0.1:5000/api/v1";

export async function fetchContractOptions() {
  try {
    const response = await axios.get(`${baseUrl}/rag-options`);
    return response.data.data;
  } catch (error) {
    console.error('Error fetching data:', error);
    return null;
  }
}

export async function createRag(data) {
  try {
    const response = await axios.post(`${baseUrl}/create-rag`, data);
    return response.data.data; // Assuming the response contains a message field
  } catch (error) {
    console.error('Error posting data:', error);
    return null;
  }
}

export async function postChat(data) {
  try {
    const response = await axios.post(`${baseUrl}/chat`, data);
    return response.data.data; // Assuming the response contains a message field
  } catch (error) {
    console.error('Error posting data:', error);
    return null;
  }
}

export async function uploadFile(file) {
  try {
    const formData = new FormData();
    formData.append('file', file);

    const response = await axios.post(`${baseUrl}/file-upload`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    return response.data.data; // Assuming the response contains a message field
  } catch (error) {
    console.error('Error uploading file:', error);
    return null;
  }
}