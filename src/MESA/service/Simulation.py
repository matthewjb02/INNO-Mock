from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from ..domain.Agent import Agent

class Simulation(Model):
    def __init__(self, N, width, height):
        """
        Initialize the model with a grid and a set of agents.
        """
        super().__init__()
        self.num_agents = N
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)

        # Set a fixed random seed for reproducibility
        self.random.seed(42)

        # Add agents to the model
        for i in range(self.num_agents):
            agent = Agent(i, self)
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))
            self.schedule.add(agent)

    def step(self):
        """
        Execute a step in the simulation: all agents act.
        """
        self.schedule.step()