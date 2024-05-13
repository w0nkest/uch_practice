import pygame


class Playerstay(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

    def update_pos(self, pl1_pos, pl2_pos):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerrun(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.something = 1
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self, pl1_pos, pl2_pos):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame * self.something]
        if self.something == 1:
            self.rect = self.rect.move(-24, 0)      # (-30, 0)
            if self.r:
                pl2_pos[0] -= 24                    # 30
            else:
                pl1_pos[0] += 24                    # 30
        else:
            self.rect = self.rect.move(24, 0)       # (30, 0)
            if self.r:
                pl2_pos[0] += 24                    # 30
            else:
                pl1_pos[0] -= 24                    # 30

    def update_pos(self, pl1_pos, pl2_pos):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerjump(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        if right:
            self.r = right
            self.mask = pygame.mask.from_surface(self.frames[6])
        else:
            self.mask = pygame.mask.from_surface(self.frames[3])
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)
        self.is_jumping = False

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        x = 3
        y = 5
        if self.r:
            x = 6
            y = 10
        if self.cur_frame < x:
            self.rect = self.rect.move(0, -44)      # (0, -55)
        else:
            self.rect = self.rect.move(0, 36)       # (0, 45)
        if self.cur_frame == y:
            self.is_jumping = False

    def update_pos(self, pl1_pos, pl2_pos):
        if not self.is_jumping:
            if self.r:
                self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
            else:
                self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playersit(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = -1
        self.is_sitting = False
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        x = 4
        if self.r:
            x = 5
        if self.cur_frame != x:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            self.is_sitting = True

    def update_pos(self, pl1_pos, pl2_pos):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerattack(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.r = right
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.is_attacking = False
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        x = 4
        if self.r:
            x = 10
        if self.cur_frame == x:
            self.is_attacking = False

    def update_pos(self, pl1_pos, pl2_pos):
        if self.r:
            self.rect = self.rect.move(pl2_pos[0] - self.rect[0], pl2_pos[1] - self.rect[1])
        else:
            self.rect = self.rect.move(pl1_pos[0] - self.rect[0], pl1_pos[1] - self.rect[1])


class Playerdeath(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, sprite_group, right=True):
        super().__init__(sprite_group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.is_right = right
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        if self.cur_frame != 5:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            if not self.is_right:
                self.rect = self.rect.move(-64, 0)      # (-80, 0)
        self.image = self.frames[self.cur_frame]

    def update_pos(self, pl1_pos, pl2_pos):
        x = 0
        if self.is_right:
            x = 120
        self.rect = self.rect.move(pl1_pos[0] - self.rect[0] + x, pl1_pos[1] - self.rect[1])

