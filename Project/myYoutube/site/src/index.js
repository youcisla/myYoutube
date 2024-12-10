import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import ReactDOM from 'react-dom/client';
import AllVideos from './components/AllVideos';
import Header from './components/Header';
import Home from './components/Home';
import Login from './components/Login';
import MyVideos from './components/MyVideos';
import Signup from './components/Signup';
import UploadVideo from './components/UploadVideo';

const App = () => {
    const [page, setPage] = useState('home');

    return (
        <div>
            <Header navigate={setPage} />
            {page === 'home' && <Home navigate={setPage} />}
            {page === 'login' && <Login navigate={setPage} />}
            {page === 'signup' && <Signup navigate={setPage} />}
            {page === 'upload' && <UploadVideo navigate={setPage} />}
            {page === 'my-videos' && <MyVideos navigate={setPage} />}
            {page === 'all-videos' && <AllVideos navigate={setPage} />}
        </div>
    );
};

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
