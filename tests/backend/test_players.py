import pytest
from app.models.player import Player
from app.schemas.player import PlayerSchema

def test_player_creation():
    player_data = {
        "name": "Test Player",
        "team": "Test Team",
        "position": "Midfielder",
        "price": 10.0
    }
    player = Player(**player_data)
    assert player.name == "Test Player"
    assert player.team == "Test Team"
    assert player.position == "Midfielder"
    assert player.price == 10.0

def test_player_schema_validation():
    player_data = {
        "name": "Test Player",
        "team": "Test Team",
        "position": "Midfielder",
        "price": 10.0
    }
    player_schema = PlayerSchema(**player_data)
    assert player_schema.name == "Test Player"
    assert player_schema.team == "Test Team"
    assert player_schema.position == "Midfielder"
    assert player_schema.price == 10.0

def test_invalid_player_data():
    with pytest.raises(ValueError):
        Player(name="Invalid Player", team="Invalid Team", position="Midfielder", price="invalid_price")