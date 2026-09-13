import random
import pygame

from gale.input_handler import InputData
import settings
from src.World import World
from src.Bird import Bird

from .GameMode import GameMode
from gale.text import render_text

class HardMode(GameMode):

    def update(self,dt: float = 0, world: World = None) -> None:
        if world.generate_logs:

            time_log = random.randint(settings.MIN_TIME_TO_SPAWN_LOGS, settings.MAX_TIME_TO_SPAWN_LOGS)
            time_power = random.randint(20, 25)
            rel:float = time_log / settings.MIN_TIME_TO_SPAWN_LOGS
            displacement = 0

            if random.choice([True, False]):
                displacement = 72*(rel +((time_log - settings.MIN_TIME_TO_SPAWN_LOGS)/settings.MIN_TIME_TO_SPAWN_LOGS*2))
            else:
                displacement = -72*(rel +((time_log - settings.MIN_TIME_TO_SPAWN_LOGS)/settings.MIN_TIME_TO_SPAWN_LOGS*2))

            world.logs_spawn_timer += dt
            world.power_spawn_timer += dt

            if world.logs_spawn_timer >= time_log/100:
                world.logs_spawn_timer = 0.0
                y = max(
                    settings.MIN_LOG_Y,
                    min(
                        world.last_log_y - displacement,
                        settings.VIRTUAL_HEIGHT - 115 - settings.LOG_HEIGHT,
                    ),
                )
                world.last_log_y = y

                aux = random.choice([0, 1, 2, 3])
                is_closing_log =  True if aux == 0 else False
                world.logs.append(
                    world.log_pair_factory.create(
                        settings.VIRTUAL_WIDTH, 
                        y, 
                        {"is_hard": is_closing_log} 
                    )
                )
                if world.power_spawn_timer >= time_power:
                    world.power_spawn_timer = 0.0
                    pos_y_powerup = random.randint(5, settings.VIRTUAL_HEIGHT - settings.POWER_UP_HEIGHT - 5)
                    pos_x_powerup = settings.VIRTUAL_WIDTH if world.logs_spawn_timer > 1.2 else settings.VIRTUAL_WIDTH + 75
                    world.powerups.append(
                        world.powerup_factory.create(
                            pos_x_powerup,
                            pos_y_powerup
                        )
                    )

    def render(self, surface: pygame.Surface) -> None :
        render_text(
            surface,
            "HardMode",
            settings.FONTS["flappy"],
            settings.VIRTUAL_WIDTH - 190,
            10,
            settings.COLOR_WHITE,
            shadowed=True,
        )
        


    def on_input(self, bird: Bird, input_id: str, input_data: InputData) -> None:
        if input_id in ("move_left", "move_right"):
            if input_data.pressed:
                bird.vx = (
                    -settings.BIRD_SPEED if input_id == "move_right" else settings.BIRD_SPEED
                )
            elif input_data.released:
                sign = -1 if input_id == "move_right" else 1
                if bird.vx == sign * settings.BIRD_SPEED:
                    bird.vx = 0

    def powerup_bird(self, bird: Bird) -> None:
        bird.get_power()