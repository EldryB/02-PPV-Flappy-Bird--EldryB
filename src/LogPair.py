"""
ISPPV1 2023
Study Case: Flappy Bird

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition of the class LogPair: a top log
(rendered flipped upside down) and a bottom log, LOGS_GAP pixels
apart, that scroll left together and score once the bird passes them.
"""

import pygame

import settings
from typing import Optional
from gale.timer import Timer

class LogPair:
    def __init__(self, x: float, y: float, is_hard: bool = False) -> None:
        self.x: float = x
        self.y: float = y
        self.scored: bool = False
        self.hard = is_hard if is_hard is not None else False
        self.timer = 0.0
        self.is_open = True

        self.current_gap = settings.LOGS_GAP

    def get_top_rect(self) -> pygame.Rect:
        return pygame.Rect(round(self.x), round(self.y), settings.LOG_WIDTH, settings.LOG_HEIGHT)

    def get_bottom_rect(self) -> pygame.Rect:
        return pygame.Rect(
            round(self.x),
            round(self.y + self.current_gap + settings.LOG_HEIGHT),
            settings.LOG_WIDTH,
            settings.LOG_HEIGHT,
        )

    def collides(self, rect: pygame.Rect) -> bool:
        return self.get_top_rect().colliderect(rect) or self.get_bottom_rect().colliderect(rect)

    def update(self, dt: float) -> None:
        self.timer += dt
        self.x += -settings.MAIN_SCROLL_SPEED * dt
        if(self.hard and self.timer >= 1.5 and self.is_open == True):
            
            Timer.tween(0.2, [(self, {"current_gap": 0})], on_finish=lambda:settings.SOUNDS["close"].play())
            self.timer = 0.0
            self.is_open = False
            
        elif (self.hard and self.timer >= 0.5 and self.is_open == False):
            Timer.tween(0.2, [(self, {"current_gap": settings.LOGS_GAP})])
            self.timer = 0.0
            self.is_open = True

    def is_out_of_game(self) -> bool:
        return self.x < -settings.LOG_WIDTH

    def update_scored(self, rect: pygame.Rect) -> bool:
        if self.scored:
            return False

        if rect.left > self.x + settings.LOG_WIDTH:
            self.scored = True
            return True

        return False

    def render(self, surface: pygame.Surface) -> None:
        if self.hard:
            surface.blit(settings.TEXTURES["logh_inverted"], self.get_top_rect())
            surface.blit(settings.TEXTURES["log_h"], self.get_bottom_rect())
        else:
            surface.blit(settings.TEXTURES["log_inverted"], self.get_top_rect())
            surface.blit(settings.TEXTURES["log"], self.get_bottom_rect())
