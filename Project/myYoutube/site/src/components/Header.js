import React from "react";

const Header = ({ navigate }) => {
    const isLoggedIn = !!localStorage.getItem("authToken");

    const handleLogout = () => {
        localStorage.removeItem("authToken");
        navigate("login");
    };

    return (
        <nav className="navbar navbar-light bg-light">
            <div className="container-fluid">
                <span className="navbar-brand">MyVideoApp</span>
                <div>
                    {!isLoggedIn && (
                        <>
                            <button
                                className="btn btn-outline-primary me-2"
                                onClick={() => navigate("login")}
                            >
                                Login
                            </button>
                            <button
                                className="btn btn-outline-success"
                                onClick={() => navigate("signup")}
                            >
                                Signup
                            </button>
                        </>
                    )}
                    {isLoggedIn && (
                        <>
                            <button
                                className="btn btn-outline-info me-2"
                                onClick={() => navigate("my-videos")}
                            >
                                My Videos
                            </button>
                            <button
                                className="btn btn-outline-secondary"
                                onClick={handleLogout}
                            >
                                Logout
                            </button>
                        </>
                    )}
                </div>
            </div>
        </nav>
    );
};

export default Header;
