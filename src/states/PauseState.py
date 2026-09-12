from typing import Optional

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings
from src.Bird import Bird
from src.World import World
from src import gameModes


class PauseState(BaseState):
    def enter(self, world: Optional[World] = None, bird: Optional[Bird] = None, score: Optional[int] = 0, gamemode: gameModes.GameMode = None) -> None:
            self.world = world if world is not None else World()
            self.bird = bird if bird is not None else Bird()
            self.score = score if score is not None else 0
            self.gamemode = gamemode
            self.selected_option = 0 

    def render(self, surface: pygame.Surface) -> None:
        self.world.render(surface)
        self.bird.render(surface)
        render_text(
                surface,
                f"Score: {self.score}",
                settings.FONTS["flappy"],
                20,
                10,
                settings.COLOR_WHITE,
                shadowed=True,
            )
        color_easy = settings.COLOR_YELLOW if self.selected_option == 0 else settings.COLOR_WHITE
        color_hard = settings.COLOR_YELLOW if self.selected_option == 1 else settings.COLOR_WHITE

        render_text(
            surface,
            "Continue",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH / 2,
            settings.VIRTUAL_HEIGHT / 2,
            color_easy,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "Go to title screen",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH / 2,
            (settings.VIRTUAL_HEIGHT / 2) + 25, 
            color_hard,
            center=True,
            shadowed=True,
        )
        

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id in ("move_up", "move_down") and input_data.pressed:
        
            self.selected_option = 1 - self.selected_option
            settings.SOUNDS["score"].play() 
        elif input_id == "pause_key" and input_data.pressed:
            self.state_machine.change("playing",world = self.world, bird = self.bird, score = self.score, gamemode = self.gamemode)
            return
             
        elif input_id == "confirm" and input_data.pressed:
            if self.selected_option == 0:
                self.state_machine.change("playing",world = self.world, bird = self.bird, score = self.score, gamemode = self.gamemode)
                return
            else:
                self.state_machine.change("title")
                return
