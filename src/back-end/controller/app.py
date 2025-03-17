from flask import Flask, jsonify
from flask_cors import CORS
from ..application.Simulation import Simulation
app = Flask(__name__)
CORS(app)  # Sta cross-origin requests toe voor React

# Initialiseer de simulatie
sim = Simulation(agent_count=10)

@app.route("/agents", methods=["GET"])
def get_agents():
    """Geeft de status van alle agents terug"""
    return jsonify(sim.get_agents())

@app.route("/step", methods=["POST"])
def step_simulation():
    """Voert een stap in de simulatie uit"""
    sim.step()
    return jsonify({"message": "Simulation stepped", "agents": sim.get_agents()})

if __name__ == "__main__":
    app.run(debug=True)