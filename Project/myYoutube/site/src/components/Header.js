import React from 'react';

const Header = ({ navigate }) => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <button className="navbar-brand btn btn-link" onClick={() => navigate('home')}>
                    MyVideoApp
                </button>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNav">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <button className="btn nav-link" onClick={() => navigate('home')}>Home</button>
                        </li>
                        <li className="nav-item">
                            <button className="btn nav-link" onClick={() => navigate('upload')}>Upload Video</button>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Header;
