def load_fpl_data():
    import requests
    from backend.app.db.session import get_db_session
    from backend.app.models.player import Player

    # Fetch data from the Fantasy Premier League API
    response = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
    data = response.json()

    # Load players data into the local database
    players = data['elements']
    
    with get_db_session() as session:
        for player in players:
            player_record = Player(
                id=player['id'],
                first_name=player['first_name'],
                last_name=player['last_name'],
                team_id=player['team'],
                position=player['element_type'],
                total_points=player['total_points'],
                price=player['now_cost'] / 10  # Convert to float
            )
            session.add(player_record)
        session.commit()