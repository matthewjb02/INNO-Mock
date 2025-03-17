const API_URL = "http://127.0.0.1:5000";

class AppService {
    async getAgents() {
        const response = await fetch(`${API_URL}/agents`);
        return response.json();
    }

    async stepSimulation() {
        const response = await fetch(`${API_URL}/step`, { method: "POST" });
        return response.json();
    }
}

// Exporteer een instantie van de service
export default new AppService();