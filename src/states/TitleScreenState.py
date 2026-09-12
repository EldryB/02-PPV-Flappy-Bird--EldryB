import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings
from src.World import World
from src import gameModes 

class TitleScreenState(BaseState):
    def enter(self) -> None:
        self.world = World()
        self.selected_option = 0 

    def update(self, dt: float) -> None:
        self.world.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        self.world.render(surface)
        
        render_text(
            surface,
            "Flappy Bird",
            settings.FONTS["flappy"],
            settings.VIRTUAL_WIDTH / 2,
            settings.VIRTUAL_HEIGHT / 3,
            settings.COLOR_WHITE,
            center=True,
            shadowed=True,
        )

        color_easy = settings.COLOR_YELLOW if self.selected_option == 0 else settings.COLOR_WHITE
        color_hard = settings.COLOR_YELLOW if self.selected_option == 1 else settings.COLOR_WHITE

        render_text(
            surface,
            "Normal Mode",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH / 2,
            2 * settings.VIRTUAL_HEIGHT / 3,
            color_easy,
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "Hard Mode",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH / 2,
            (2 * settings.VIRTUAL_HEIGHT / 3) + 25, 
            color_hard,
            center=True,
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id in ("move_up", "move_down") and input_data.pressed:

            self.selected_option = 1 - self.selected_option
            settings.SOUNDS["score"].play() 

        elif input_id == "confirm" and input_data.pressed:
            if self.selected_option == 0:
                self.state_machine.change("count_down", gamemode=gameModes.EasyMode())
            else:
                self.state_machine.change("count_down", gamemode=gameModes.HardMode())