import requests

class FPLClient:
    BASE_URL = "https://fantasy.premierleague.com/api/"

    def get_players(self):
        response = requests.get(f"{self.BASE_URL}bootstrap-static/")
        response.raise_for_status()
        data = response.json()
        return data['elements']

    def get_leagues(self):
        response = requests.get(f"{self.BASE_URL}leagues-classic/")
        response.raise_for_status()
        return response.json()

    def get_team(self, team_id):
        response = requests.get(f"{self.BASE_URL}entry/{team_id}/history/")
        response.raise_for_status()
        return response.json()