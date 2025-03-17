import { useState, useEffect } from "react";
import AppController from "../../controller/AppController.js";

function App() {
    const [agents, setAgents] = useState([]);
    const controller = new AppController(setAgents);

    useEffect(() => {
        controller.fetchAgents().then(r => console.log(r));
    }, []);

    return (
        <div>
            <h1>Agent-Based Model</h1>
            <svg width="500" height="500" style={{ border: "1px solid black" }}>
                {agents.map((agent) => (
                    <circle key={agent.id} cx={agent.x} cy={agent.y} r="5" fill="blue" />
                ))}
            </svg>
            <button onClick={() => controller.handleStep()}>Step Simulation</button>
        </div>
    );
}

export default App;