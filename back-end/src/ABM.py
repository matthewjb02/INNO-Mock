import random

# --- Instellingen ---
WIDTH, HEIGHT = 500, 500
AGENT_COUNT = 10
SPEED = 2

# --- 1. Domein Klasse: Agent ---
class Agent:
    def __init__(self, id, x, y):
        """Creëert een agent met een unieke ID"""
        self.id = id
        self.x = x
        self.y = y

    def move(self):
        """Beweeg willekeurig"""
        self.x += random.choice([-SPEED, 0, SPEED])
        self.y += random.choice([-SPEED, 0, SPEED])

        # Houd agent binnen het scherm
        self.x = max(0, min(WIDTH, self.x))
        self.y = max(0, min(HEIGHT, self.y))

# --- 2. Simulatie Klasse ---
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

# Testen van de simulatie
if __name__ == "__main__":
    sim = Simulation(AGENT_COUNT)
    for _ in range(5):  # Simuleer 5 stappen
        sim.step()
        print(sim.get_agents())