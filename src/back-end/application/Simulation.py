import random
WIDTH, HEIGHT = 500, 500
from ..domain.Agent import Agent

class Simulation:
    def __init__(self, agent_count):
        """Initialiseer agents in de simulatie"""
        self.agents = [Agent(i, random.randint(0, WIDTH), random.randint(0, HEIGHT)) for i in range(agent_count)]

    def step(self):
        """Laat alle agents één stap bewegen"""
        for agent in self.agents:
            agent.move()

    def get_agents(self):
        """Geeft de huidige status van alle agents terug"""
        return [vars(agent) for agent in self.agents]


