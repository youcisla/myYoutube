import axios from "axios";

export const fetchMyVideos = async () => {
    try {
        const token = localStorage.getItem("authToken"); // Ensure you store the token after login
        const response = await axios.get("http://127.0.0.1:8000/my-videos/", {
            headers: {
                Authorization: `Token ${token}`, // Use 'Bearer' if you're using JWT
            },
        });
        console.log("Fetched videos:", response.data);
        return response.data;
    } catch (error) {
        console.error("Error fetching videos:", error);
        throw error;
    }
};
