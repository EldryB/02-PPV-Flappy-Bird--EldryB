"""
ISPPV1 2023
Study Case: Flappy Bird

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition of the class Bird.
"""

import pygame

import settings

class Bird():
    def __init__(self, x: float, y: float, width: float, height: float) -> None:
        self.x: float = x
        self.y: float = y
        self.width: float = width
        self.height: float = height
        self.vy: float = 0.0
        self.vx: float = 0.0
        self.jumping: bool = False
        self.power = False
        self.power_timer: float = 0.0

    def get_power(self)-> None:
        self.power_timer = 0.0
        self.power = True

    def quit_power(self) -> None:
        self.power_timer = 0.0
        self.power = False
        settings.SOUNDS["power_up"].stop()
        pygame.mixer.music.play(loops=-1)
        
    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(round(self.x), round(self.y), self.width, self.height)

    def jump(self) -> None:
        self.jumping = True

    def update(self, dt: float) -> None:
        self.vy += settings.GRAVITY * dt
        if self.jumping:
            settings.SOUNDS["jump"].play()
            self.vy = -settings.JUMP_TAKEOFF_SPEED
            self.jumping = False

        if self.power:
            self.power_timer += dt

        if self.power_timer > 7.5:
            self.quit_power()

        self.y += self.vy * dt
        self.x += self.vx * dt

    def render(self, surface: pygame.Surface) -> None:
        if self.power:
            surface.blit(settings.TEXTURES["bird_power"], self.get_rect())

        else:
            surface.blit(settings.TEXTURES["bird"], self.get_rect())
