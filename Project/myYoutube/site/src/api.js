import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

// Signup API
export const signup = async (userData) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/register/`, userData); // Ensure trailing slash
        return response.data;
    } catch (error) {
        console.error('Signup failed:', error.response?.data || error.message);
        throw error;
    }
};

// Login API
export const login = async (credentials) => {
    try {
        const response = await axios.post('http://127.0.0.1:8000/login/', credentials); // Ensure trailing slash
        return response.data;
    } catch (error) {
        console.error('Login failed:', error.response?.data || error.message);
        throw error;
    }
};

// Example Authenticated API Call
export const fetchWithAuth = async (url) => {
    try {
        const token = localStorage.getItem('token'); // Retrieve token from local storage
        const response = await axios.get(`${API_BASE_URL}${url}`, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        });
        return response.data;
    } catch (error) {
        console.error('Fetch with Auth failed:', error.response?.data || error.message);
        throw error;
    }
};
