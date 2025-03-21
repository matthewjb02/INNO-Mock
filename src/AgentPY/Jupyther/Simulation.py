import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
from Model import Model  # Zorg ervoor dat Model correct is geïmplementeerd en geïmporteerd


def run_simulation(agent_count, steps):
    """ Voert de simulatie uit met opgegeven parameters en visualiseert deze """
    parameters = {"agents": agent_count, "steps": steps}
    model = Model(parameters)  # Zorg dat Model een juiste constructor heeft
    results = model.run()

    # Visualisatie van de agent-posities
    fig, ax = plt.subplots()
    positions = results.variables["positions"]  # Aangepaste referentie

    for step, pos in positions.items():
        x, y = zip(*pos.values())  # Extract X en Y coördinaten
        ax.clear()
        ax.scatter(x, y, color="blue")
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_title(f"Stap {step}")
        plt.pause(0.5)  # Simulatie-animatie effect

    plt.show()
