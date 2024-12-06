import React, { useEffect, useState } from 'react';
import { fetchVideos, deleteVideo } from '../api';

const Home = () => {
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        fetchVideos().then(data => setVideos(data));
    }, []);

    const handleDelete = (id) => {
        deleteVideo(id).then(() => {
            setVideos(videos.filter(video => video.id !== id));
        });
    };

    return (
        <div className="container">
            <h2>Videos</h2>
            <div className="row g-3">
                {videos.map(video => (
                    <div key={video.id} className="col-md-4">
                        <div className="card">
                            <video controls className="card-img-top" src={`http://127.0.0.1:8000/media/${video.source}`} />
                            <div className="card-body">
                                <h5 className="card-title">{video.name}</h5>
                                <button className="btn btn-danger btn-sm" onClick={() => handleDelete(video.id)}>Delete</button>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Home;
