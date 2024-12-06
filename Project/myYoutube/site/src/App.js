import React, { useState } from 'react';
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

export default App;
