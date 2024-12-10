import React, { useState } from "react";
import axiosInstance from "../api/axiosInstance"; // Import the centralized Axios instance

const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loginStatus, setLoginStatus] = useState("");

    const handleLogin = async (e) => {
        e.preventDefault();

        try {
            const response = await axiosInstance.post("/login/", { username, password });
            localStorage.setItem("authToken", response.data.token); // Store token in localStorage
            setLoginStatus("Login successful!");
        } catch (error) {
            console.error("Login failed:", error.response?.data || error.message);
            setLoginStatus("Invalid username or password.");
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button type="submit">Login</button>
            </form>
            <p>{loginStatus}</p>
        </div>
    );
};

export default Login;
