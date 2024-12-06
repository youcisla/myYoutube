import axios from "axios";
import React, { useState } from "react";

const API_BASE_URL = 'http://127.0.0.1:8000';
const response = await axios.post(`${API_BASE_URL}/auth/register`, userData); // Adjust as per Django URL patterns

const Signup = () => {
    const [formData, setFormData] = useState({
        username: "",
        email: "",
        password: "",
        pseudo: "",
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await signup(formData);
            alert('Signup successful!');
        } catch (error) {
            const errorMessage = error.response?.data?.data?.error || 'Signup failed!';
            console.error('Error during signup:', errorMessage);
            alert(errorMessage);
        }
    };

    const checkUsernameExists = async (username) => {
        try {
            const response = await axios.get(`${API_BASE_URL}/auth/check-username`, {
                params: { username },
            });
            return response.data.exists; // Backend should return true/false
        } catch (error) {
            console.error('Error checking username:', error);
            return false; // Allow the signup attempt if check fails
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="username"
                placeholder="Username"
                value={formData.username}
                onChange={handleChange}
                required
            />
            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <input
                type="password"
                name="password"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
                required
            />
            <input
                type="text"
                name="pseudo"
                placeholder="Pseudo"
                value={formData.pseudo}
                onChange={handleChange}
            />
            <button type="submit">Signup</button>
        </form>
    );
};

export default Signup;
