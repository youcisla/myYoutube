const API_BASE_URL = "http://localhost:5000";

export const addVideo = async (videoData) => {
    const response = await fetch(`${API_BASE_URL}/videos/create/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`, // Add token for authenticated users
        },
        body: JSON.stringify(videoData),
    });

    if (!response.ok) {
        throw new Error("Failed to add video");
    }

    return response.json();
};

export const deleteVideo = async (videoId) => {
    const response = await fetch(`${API_BASE_URL}/video/${videoId}/delete/`, {
        method: "DELETE",
        headers: {
            Authorization: `Bearer ${localStorage.getItem("token")}`, // Add token for authenticated users
        },
    });

    if (!response.ok) {
        throw new Error("Failed to delete video");
    }

    return response.json();
};
