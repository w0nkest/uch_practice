import pygame


class HPbar:
    def __init__(self, x, y, right=True):
        self.hp = 10
        self.x = x
        self.y = y
        self.is_right = right

    def render(self, screen):
        pygame.draw.rect(screen, pygame.Color('Grey'), (self.x, self.y, 544, 80), 4)            # (680, 100), 5
        pygame.draw.rect(screen, pygame.Color('Green'), (self.x + 5, self.y + 5, 536, 72))      # (670, 90)
        if self.hp < 0:
            self.hp = 0
        for i in range(10 - self.hp):
            if self.is_right:
                pygame.draw.rect(screen, pygame.Color('Red'), (self.x + 4 + i * 54, self.y + 4, 54, 72))
                # self.x + 5 + i * 67, self.y + 5, 67, 90
            else:
                pygame.draw.rect(screen, pygame.Color('Red'), ((self.x + 5 + 9 * 54) - i * 54,
                                                               self.y + 4, 54, 72))
                # (self.x + 5 + 9 * 67) - i * 67, self.y + 5, 67, 90
        hp_font = pygame.font.Font(None, 80)       # 100
        hp_text = hp_font.render(f"100 / {self.hp * 10}", True, 'White')
        if self.is_right:
            hp_text = hp_font.render(f"{self.hp * 10} / 100", True, 'White')
        hp_text_x = self.x + 160        # 200
        hp_text_y = self.y + 16         # 20
        screen.blit(hp_text, (hp_text_x, hp_text_y))
