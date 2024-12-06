import React, { useState } from 'react';
import ReactDOM from 'react-dom/client'; // Updated import
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/index.css';

import Header from './components/Header';
import Home from './components/Home';
import UploadVideo from './components/UploadVideo';

const App = () => {
    const [page, setPage] = useState('home');

    return (
        <div>
            <Header navigate={setPage} />
            {page === 'home' && <Home />}
            {page === 'upload' && <UploadVideo navigate={setPage} />}
        </div>
    );
};

// Use React 18 createRoot API
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
