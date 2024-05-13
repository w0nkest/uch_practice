import pygame


class Button:
    def __init__(self, x, y, width_b, height_b, button_objects,
                 buttonText='Button', onclickFunction=None):
        self.x = x
        self.y = y
        self.width = width_b
        self.height = height_b
        self.onclickFunction = onclickFunction
        self.alreadyPressed = False
        self.buttonText = buttonText

        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, (255, 255, 255))
        button_objects.append(self)

    def process(self, screen):
        screen.blit(self.buttonSurf, (self.x, self.y))
        screen.blit(self.buttonSurf, self.buttonRect)

        self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, (255, 255, 255))
        mousePos = pygame.mouse.get_pos()
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurf = pygame.font.Font(None, 50).render(self.buttonText, True, self.fillColors['pressed'])
                self.onclickFunction()
                self.alreadyPressed = True
            else:
                self.alreadyPressed = False