import React, { useEffect, useState } from 'react';
import axios from 'axios';

const AllVideos = ({ navigate }) => {
    const [videos, setVideos] = useState([]);

    useEffect(() => {
        const fetchVideos = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/all-videos/');
                setVideos(response.data);
            } catch (error) {
                console.error('Error fetching videos:', error);
                alert('Failed to fetch all videos');
            }
        };
        fetchVideos();
    }, []);

    return (
        <div className="container mt-5">
            <h2 className="text-center mb-4">All Videos</h2>
            <div className="row">
                {videos.map((video) => (
                    <div className="col-md-4 mb-4" key={video.id}>
                        <div className="card shadow">
                            <video
                                src={`http://127.0.0.1:8000/media/${video.source}`}
                                className="card-img-top"
                                controls
                            />
                            <div className="card-body">
                                <h5 className="card-title">{video.name}</h5>
                                <p className="card-text">Uploaded by: {video.UserID}</p>
                            </div>
                        </div>
                    </div>
                ))}
            </div>
            <button
                className="btn btn-primary mt-3"
                onClick={() => navigate('home')}
            >
                Back to Home
            </button>
        </div>
    );
};

export default AllVideos;
