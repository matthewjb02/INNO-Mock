from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider
from ..service.Simulation import Simulation

# 🖼️ Hoe de agent eruitziet in de visualisatie
def agent_portrayal(agent):
    return {
        "Shape": "circle",
        "Color": "red",
        "Filled": "true",
        "r": 0.5  # Grootte van de cirkel
    }

# 📏 Grid instellen
grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

# 🔧 Instellen van gebruikersparameters in de UI
model_params = {
    "N": Slider("Aantal Agents", 10, 1, 50, 1),
    "width": 10,
    "height": 10
}

# 🚀 Webserver starten
server = ModularServer(Simulation, [grid], "Random Model", model_params)
server.port = 8521  # Standaardpoort

if __name__ == "__main__":
    print("✅ MESA Simulatie gestart op http://127.0.0.1:8521/")
    server.launch()