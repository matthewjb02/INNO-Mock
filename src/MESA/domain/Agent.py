from mesa import Agent

class Agent(Agent):
    def __init__(self, unique_id, model):
        """
        Een agent die zich willekeurig beweegt binnen het model.
        """
        super().__init__(unique_id, model)

    def step(self):
        """
        De agent kiest bij elke stap een willekeurige nieuwe positie.
        """
        possible_moves = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        if possible_moves:
            new_position = self.random.choice(possible_moves)
            self.model.grid.move_agent(self, new_position)