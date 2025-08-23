class Player:
    def __init__(self, id: int, name: str, position: str, team: str, price: float):
        self.id = id
        self.name = name
        self.position = position
        self.team = team
        self.price = price

    def __repr__(self):
        return f"<Player(id={self.id}, name={self.name}, position={self.position}, team={self.team}, price={self.price})>"