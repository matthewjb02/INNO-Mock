import AppService from "../services/AppService.js";

class AppController {
    constructor(setAgents) {
        this.setAgents = setAgents;
    }

    async fetchAgents() {
        try {
            const data = await AppService.getAgents();
            this.setAgents(data);
        } catch (error) {
            console.error("Error fetching agents:", error);
        }
    }

    async handleStep() {
        try {
            await AppService.stepSimulation();
            await this.fetchAgents(); // Update agenten na een stap
        } catch (error) {
            console.error("Error stepping simulation:", error);
        }
    }
}

export default AppController;