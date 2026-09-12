"""
ISPPV1 2023
Study Case: Flappy Bird

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition of the class World: the scrolling
background/ground, and the log pairs the bird must fly through.
"""

import random
from typing import List

import pygame

from gale.factory import Factory

import settings
from src.LogPair import LogPair
from src.PowerUp import PowerUp


class World:
    def __init__(self, generate_logs: bool = False) -> None:
        self.generate_logs: bool = generate_logs
        self.background_x: float = 0.0
        self.ground_x: float = 0.0
        self.logs: List[LogPair] = []
        self.powerups: List[PowerUp] = []
        self.logs_spawn_timer: float = 0.0
        self.power_spawn_timer: float = 0.0
        self.last_log_y: float = settings.MIN_LOG_Y + random.randint(0, 80) + 20
        self.log_pair_factory: Factory = Factory(LogPair)
        self.powerup_factory: Factory = Factory(PowerUp)

    def reset(self, generate_logs: bool) -> None:
        self.generate_logs = generate_logs

    def collides(self, rect: pygame.Rect) -> bool:
        if rect.bottom >= settings.VIRTUAL_HEIGHT or rect.top <= -4 or rect.right >= settings.VIRTUAL_WIDTH or rect.left <= -4:
            return True

    def collides_log(self, rect: pygame.Rect) -> bool:
        return any(log_pair.collides(rect) for log_pair in self.logs)

    def get_power(self, rect: pygame.Rect) -> bool:
        for power in self.powerups:
            if power.collides(rect):
                self.powerups.remove(power)
                return True
        return False

    def update_scored(self, rect: pygame.Rect) -> bool:
        return any(log_pair.update_scored(rect) for log_pair in self.logs)

    def update(self, dt: float) -> None:
        self.background_x += -settings.BACK_SCROLL_SPEED * dt

        if self.background_x <= -settings.BACKGROUND_LOOPING_POINT:
            self.background_x = 0

        self.ground_x += -settings.MAIN_SCROLL_SPEED * dt

        if self.ground_x <= -settings.VIRTUAL_WIDTH:
            self.ground_x = 0

        for log_pair in self.logs:
            log_pair.update(dt)

        for power in self.powerups:
            power.update(dt)

        self.logs = [log_pair for log_pair in self.logs if not log_pair.is_out_of_game()]
        self.powerups = [power for power in self.powerups if not power.is_out_of_game()]

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["background"], (round(self.background_x), 0))

        for log_pair in self.logs:
            log_pair.render(surface)

        for power in self.powerups:
            power.render(surface)

        surface.blit(
            settings.TEXTURES["ground"],
            (round(self.ground_x), settings.VIRTUAL_HEIGHT - settings.GROUND_HEIGHT),
        )
