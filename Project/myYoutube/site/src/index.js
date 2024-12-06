// Frontend Imports
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client'; // React 18 createRoot API
import './styles/index.css';

// Login Component
const Login = ({ navigate }) => {
    const [formData, setFormData] = useState({ username: '', password: '' });

    const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Logged in as: ${formData.username}`);
    };

    return (
        <div className="container vh-100 d-flex justify-content-center align-items-center">
            <div className="card p-4 shadow-lg" style={{ width: '350px' }}>
                <h2 className="text-center text-primary mb-4">Login</h2>
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
                    <button type="submit" className="btn btn-primary w-100">Login</button>
                </form>
                <button
                    className="btn btn-link text-secondary mt-3"
                    onClick={() => navigate('signup')}
                >
                    Don't have an account? Sign up
                </button>
            </div>
        </div>
    );
};

// Signup Component
const Signup = ({ navigate }) => {
    const [formData, setFormData] = useState({ username: '', email: '', password: '' });

    const handleChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

    const handleSubmit = (e) => {
        e.preventDefault();
        alert(`Signed up as: ${formData.username}`);
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

// Header Component
const Header = ({ navigate }) => (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-3">
        <a className="navbar-brand" href="#" onClick={() => navigate('home')}>
            MyVideoApp
        </a>
        <div className="navbar-nav ms-auto">
            <button className="btn btn-outline-primary me-2" onClick={() => navigate('login')}>Login</button>
            <button className="btn btn-outline-success" onClick={() => navigate('signup')}>Sign Up</button>
        </div>
    </nav>
);

// Home Component
const Home = ({ navigate }) => (
    <div className="container text-center vh-100 d-flex flex-column justify-content-center align-items-center">
        <h1 className="display-4 text-primary">Welcome to MyVideoApp</h1>
        <p className="lead text-muted">Enjoy your journey of creating and managing videos.</p>
        <button className="btn btn-primary mt-3" onClick={() => navigate('upload')}>Upload Video</button>
    </div>
);

// Upload Video Component
const UploadVideo = ({ navigate }) => (
    <div className="container vh-100 d-flex flex-column justify-content-center align-items-center">
        <h2 className="text-center text-primary mb-4">Upload Your Video</h2>
        <form>
            <div className="mb-3">
                <input type="file" className="form-control" />
            </div>
            <button className="btn btn-primary w-100">Upload</button>
        </form>
        <button
            className="btn btn-link text-secondary mt-3"
            onClick={() => navigate('home')}
        >
            Back to Home
        </button>
    </div>
);

// React App Component
const App = () => {
    const [page, setPage] = useState('home');

    return (
        <div>
            <Header navigate={setPage} />
            {page === 'home' && <Home navigate={setPage} />}
            {page === 'login' && <Login navigate={setPage} />}
            {page === 'signup' && <Signup navigate={setPage} />}
            {page === 'upload' && <UploadVideo navigate={setPage} />}
        </div>
    );
};

// Render React App
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
