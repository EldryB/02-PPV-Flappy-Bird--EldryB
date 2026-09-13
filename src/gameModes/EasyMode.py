import random 
import pygame

from gale.input_handler import InputData
import settings
from src.World import World
from src.Bird import Bird

from .GameMode import GameMode
from gale.text import render_text

class EasyMode(GameMode):

    def update(self,dt: float = 0, world: World = None) -> None:
        if world.generate_logs:
            world.logs_spawn_timer += dt

            if world.logs_spawn_timer >= settings.TIME_TO_SPAWN_LOGS:
                world.logs_spawn_timer = 0.0
                y = max(
                    settings.MIN_LOG_Y,
                    min(
                        world.last_log_y + random.randint(-20, 20),
                        settings.MAX_LOG_Y,
                    ),
                )
                world.last_log_y = y
                world.logs.append(world.log_pair_factory.create(settings.VIRTUAL_WIDTH, y))

    def render(self, surface: pygame.Surface) -> None :
        render_text(
                surface,
                "EasyMode",
                settings.FONTS["flappy"],
                settings.VIRTUAL_WIDTH - 190,
                10,
                settings.COLOR_WHITE,
                shadowed=True,
            )
        


    def on_input(self, bird: Bird, input_id: str, input_data: InputData) -> None:
        pass

    def powerup_bird(self, rect: pygame.Rect, bird: Bird = None) -> None:
        pass