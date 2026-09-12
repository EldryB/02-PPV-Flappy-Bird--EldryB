import pygame

import settings

class PowerUp():
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
        self.width: float = settings.POWER_UP_WIDTH
        self.height: float = settings.POWER_UP_HEIGHT

    def update(self, dt: float) -> None:
        self.x += -settings.MAIN_SCROLL_SPEED * dt

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["powerup"], self.get_rect())

    def is_out_of_game(self) -> bool:
        return self.x < -settings.LOG_WIDTH

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(round(self.x), round(self.y), settings.POWER_UP_WIDTH, settings.POWER_UP_HEIGHT)

    def collides(self, rect: pygame.Rect) -> bool:
        return self.get_rect().colliderect(rect)
