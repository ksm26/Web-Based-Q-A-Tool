import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000", // Make sure this matches the backend URL
});

export default instance;
