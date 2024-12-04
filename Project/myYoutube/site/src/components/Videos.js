import React, { useState } from "react";
import { addVideo, deleteVideo } from "../api";

const Videos = () => {
    const [videos, setVideos] = useState([]); // Assume videos fetched from the backend
    const [videoData, setVideoData] = useState({ name: "", source: "" });

    const handleAddVideo = async () => {
        try {
            const newVideo = await addVideo(videoData);
            setVideos([...videos, newVideo.data]);
            setVideoData({ name: "", source: "" }); // Reset form
        } catch (error) {
            alert("Error adding video: " + error.message);
        }
    };

    const handleDeleteVideo = async (videoId) => {
        try {
            await deleteVideo(videoId);
            setVideos(videos.filter((video) => video.id !== videoId));
        } catch (error) {
            alert("Error deleting video: " + error.message);
        }
    };

    return (
        <div>
            <h2>Manage Videos</h2>

            <div>
                <input
                    type="text"
                    placeholder="Video Name"
                    value={videoData.name}
                    onChange={(e) => setVideoData({ ...videoData, name: e.target.value })}
                />
                <input
                    type="file"
                    onChange={(e) => setVideoData({ ...videoData, source: e.target.files[0] })}
                />
                <button onClick={handleAddVideo}>Add Video</button>
            </div>

            <ul>
                {videos.map((video) => (
                    <li key={video.id}>
                        <h3>{video.name}</h3>
                        <button onClick={() => handleDeleteVideo(video.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Videos;
