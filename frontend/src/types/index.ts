export type Player = {
  id: number;
  name: string;
  position: string;
  team: string;
  points: number;
};

export type Team = {
  id: number;
  name: string;
  players: Player[];
};

export type League = {
  id: number;
  name: string;
  teams: Team[];
};