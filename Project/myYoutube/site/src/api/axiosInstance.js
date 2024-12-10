// axiosInstance.js
import axios from "axios";

// Base Axios instance
const axiosInstance = axios.create({
    baseURL: "http://127.0.0.1:8000", // Django API Base URL
    timeout: 5000, // Set timeout for requests
});

// Add the Authorization token to headers (if available)
axiosInstance.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem("authToken");
        if (token) {
            config.headers.Authorization = `Token ${token}`;
        }
        return config;
    },
    (error) => Promise.reject(error)
);

export default axiosInstance;
