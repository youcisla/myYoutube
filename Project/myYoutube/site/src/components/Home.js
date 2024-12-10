import React from 'react';

const Home = ({ navigate }) => (
    <div className="container text-center vh-100 d-flex flex-column justify-content-center align-items-center">
        <h1 className="display-4 text-primary">Welcome to MyVideoApp</h1>
        <p className="lead text-muted">Enjoy your journey of creating and managing videos.</p>
        <button className="btn btn-primary mt-3" onClick={() => navigate('upload')}>Upload Video</button>
    </div>
);

export default Home;
