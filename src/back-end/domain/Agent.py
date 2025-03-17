import random
WIDTH, HEIGHT = 500, 500
AGENT_COUNT = 10
SPEED = 2


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