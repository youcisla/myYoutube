import React, { useEffect, useState } from "react";
import { fetchMyVideos } from "../api/fetchMyVideos";

const MyVideos = () => {
    const [videos, setVideos] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const getVideos = async () => {
            try {
                const data = await fetchMyVideos();
                setVideos(data);
            } catch (error) {
                console.error("Failed to fetch videos:", error);
            } finally {
                setLoading(false);
            }
        };
        getVideos();
    }, []);

    if (loading) {
        return <p>Loading your videos...</p>;
    }

    return (
        <div className="container mt-4">
            <h2>Your Videos</h2>
            {videos.length > 0 ? (
                <ul className="list-group">
                    {videos.map((video) => (
                        <li key={video.id} className="list-group-item">
                            {video.name}
                        </li>
                    ))}
                </ul>
            ) : (
                <p>No videos found.</p>
            )}
        </div>
    );
};

export default MyVideos;
