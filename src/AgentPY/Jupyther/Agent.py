import agentpy as ap

class Agent(ap.Agent):

    def __init__(self, model, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
    """ Klasse die de agenten in de simulatie definieert """

    def setup(self):
        """ Initialiseer de agent en zet zijn startpositie """
        self.position = self.model.grid.positions[self]

    def step(self):
        """ Beweeg de agent willekeurig """
        self.position = self.model.grid.move_by(self, (self.model.p.random(), self.model.p.random()))