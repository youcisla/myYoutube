import axios from 'axios';
import React, { useState } from 'react';

const Signup = ({ navigate }) => {
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        pseudo: '',
    });

    const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/signup/', formData);
            alert(response.data.message);
            navigate('login');
        } catch (error) {
            alert(error.response.data.error || 'Signup failed');
        }
    };

    return (
        <div className="container vh-100 d-flex justify-content-center align-items-center">
            <div className="card p-4 shadow-lg" style={{ width: '350px' }}>
                <h2 className="text-center text-success mb-4">Sign Up</h2>
                <form onSubmit={handleSubmit}>
                    <div className="mb-3">
                        <label htmlFor="username" className="form-label">Username</label>
                        <input
                            type="text"
                            id="username"
                            name="username"
                            className="form-control"
                            placeholder="Enter your username"
                            value={formData.username}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="email" className="form-label">Email</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            className="form-control"
                            placeholder="Enter your email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="pseudo" className="form-label">Pseudo</label>
                        <input
                            type="text"
                            id="pseudo"
                            name="pseudo"
                            className="form-control"
                            placeholder="Enter your pseudo"
                            value={formData.pseudo}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className="mb-3">
                        <label htmlFor="password" className="form-label">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            className="form-control"
                            placeholder="Enter your password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <button type="submit" className="btn btn-success w-100">Sign Up</button>
                </form>
                <button
                    className="btn btn-link text-secondary mt-3"
                    onClick={() => navigate('login')}
                >
                    Already have an account? Login
                </button>
            </div>
        </div>
    );
};

export default Signup;
