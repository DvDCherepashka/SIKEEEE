import pygame

W = 800
H = 600
a = (255, 255, 255)
b = (255, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('Текст')
screen.fill(BLUE)
pygame.display.flip()
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 96, True, False)
font2 = pygame.font.SysFont('Arial', 48, True, False)
font_box = pygame.Surface((W - 30, font.get_height()))
font2_box = pygame.Surface((W - 30, font2.get_height()))

text = font.render("Всем привет", True, a)
screen.blit(text, (100, 200))
text = font2.render("Ловушкажижкера", True, b)
screen.blit(text, (215, 350))


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()
