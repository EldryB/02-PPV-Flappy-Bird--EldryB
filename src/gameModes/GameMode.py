import pygame

from gale.input_handler import InputData

from src.World import World
from src.Bird import Bird



class GameMode():

    def update(self,dt: float = 0, world: World = None) -> None:
        raise NotImplementedError()

    def on_input(self, bird: Bird, input_id: str, input_data: InputData) -> None:
        raise NotImplementedError()

    def render(self, surface: pygame.Surface) -> None:
        raise NotImplementedError()
    
    def powerup_bird(self, rect: pygame.Rect, bird: Bird = None) -> None:
        raise NotImplementedError()