import React, { useState } from 'react';
import Login from './Login';
import Signup from './Signup';
import { fetchWithAuth } from '../api';

const Home = () => {
    const [loggedIn, setLoggedIn] = useState(false);
    const [videos, setVideos] = useState([]);

    const handleLogin = async () => {
        setLoggedIn(true);
        try {
            const data = await fetchWithAuth('/videos');
            setVideos(data);
        } catch (error) {
            console.error('Error fetching videos:', error.response.data);
        }
    };

    return (
        <div>
            {loggedIn ? (
                <div>
                    <h1>Welcome to the Video App</h1>
                    <div>
                        {videos.map((video) => (
                            <div key={video.id}>
                                <h3>{video.name}</h3>
                                <video src={video.source_url} controls />
                            </div>
                        ))}
                    </div>
                </div>
            ) : (
                <div>
                    <h1>Login or Signup</h1>
                    <Login onLogin={handleLogin} />
                    <Signup />
                </div>
            )}
        </div>
    );
};

export default Home;
