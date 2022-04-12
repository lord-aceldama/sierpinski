import sys
import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

points = []
point_surface = pygame.Surface((800, 600))
mouse = (-100, -100)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Add point
            if len(points) < 3:
                points.append(mouse)
                pygame.draw.circle(point_surface, pygame.Color('blue'), mouse, 1, width=1)

    text_surface = myfont.render(f'points: {len(points)}', False, (255, 255, 255))
    screen.blit(point_surface, (0, 0))
    screen.blit(text_surface, (5, 5))
    
    if len(points) < 3:
        pygame.draw.circle(screen, pygame.Color('green'), mouse, 0.5, width=1)
        if len(points) == 2:
            pygame.draw.circle(screen, pygame.Color('yellow'), mouse, 5, width=1)
        else:
            pygame.draw.circle(screen, pygame.Color('red'), mouse, 5, width=1)
    else:
        rnd_point = points[random.randint(0, 2)]
        new_point = (
            (points[-1][0] + rnd_point[0]) / 2,
            (points[-1][1] + rnd_point[1]) / 2,
        )
        points.append(new_point)
        pygame.draw.circle(point_surface, pygame.Color('blue'), new_point, 1, width=1)

    pygame.display.update()
    clock.tick(60)
