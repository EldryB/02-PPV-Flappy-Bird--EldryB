"""
ISPPV1 2023
Study Case: Flappy Bird

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition of the class PlayingState.
"""

from typing import Optional

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings
from src.Bird import Bird
from src.World import World
from src import gameModes

class PlayingState(BaseState):
    def enter(self, world: Optional[World] = None, bird: Optional[Bird] = None, score: Optional[int] = 0, gamemode: gameModes.GameMode = None) -> None:
        self.world = world if world is not None else World()
        self.world.reset(True)
        self.gamemode = gamemode


        self.bird = bird if bird is not None else Bird(
            settings.VIRTUAL_WIDTH / 2 - settings.BIRD_WIDTH / 2,
            settings.VIRTUAL_HEIGHT / 2 - settings.BIRD_HEIGHT / 2,
            settings.BIRD_WIDTH,
            settings.BIRD_HEIGHT,
        )
        self.score = score if score is not None else 0

    def update(self, dt: float) -> None:
        self.bird.update(dt)
        self.gamemode.update(dt, world=self.world)
        self.world.update(dt)


        if (self.world.collides(self.bird.get_rect()) and self.bird.power):
            self.bird.quit_power()



        if ((self.world.collides_log(self.bird.get_rect()) and not self.bird.power) or self.world.collides(self.bird.get_rect())):
            settings.SOUNDS["explosion"].play()
            settings.SOUNDS["hurt"].play()
            self.state_machine.change("count_down", gamemode = self.gamemode)
            return

        if self.world.get_power(self.bird.get_rect()):
            self.gamemode.powerup_bird(self.bird)
            settings.SOUNDS["power_up"].play(loops=-1)
            pygame.mixer.music.stop()

        if self.world.update_scored(self.bird.get_rect()):
            self.score += 1
            settings.SOUNDS["score"].play()

    def render(self, surface: pygame.Surface) -> None:
        self.world.render(surface)
        self.bird.render(surface)
        self.gamemode.render(surface)
        render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["flappy"],
            20,
            10,
            settings.COLOR_WHITE,
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.gamemode.on_input(self.bird, input_id, input_data )

        if input_id == "jump" and input_data.pressed:
            self.bird.jump()

        if input_id == "pause_key" and input_data.pressed:
            self.state_machine.change("pause", world = self.world, bird = self.bird, score = self.score, gamemode = self.gamemode)
            return
