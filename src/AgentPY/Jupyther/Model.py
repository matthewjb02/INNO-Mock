import sys
import os
import agentpy as ap

# Voeg de project root toe aan het sys.path als de 'domain' module niet wordt gevonden
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Correcte import van de Agent klasse
import Agent

class Model(ap.Model):
    """ Simulatiemodel dat agents aanmaakt en hun gedrag beheert """

    def setup(self):
        """ Initialiseert de agents en het grid """
        self.agents = ap.AgentList(self, self.p.agents, Agent)
        self.grid = ap.Grid(self, (10, 10), track=True)
        self.grid.add_agents(self.agents, random=True)

    def step(self):
        """ Laat alle agents een stap zetten """
        self.agents.step()

    def update(self):
        """ Slaat de posities van agents op """
        self.record("positions", self.grid.positions)

    def end(self):
        """ Rapporteert de eindresultaten """
        self.report("Eindposities", self.grid.positions)