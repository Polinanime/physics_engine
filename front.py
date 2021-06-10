import pygame
from consts import WIDTH, HEIGHT
from core import World, Body
from structures import Vector

if __name__ == '__main__':
    all_bodies = []
    mass = 10 ** 9
    all_bodies.append(Body(0, mass, (300, 650), Vector((0, 0)), (255, 0, 0)))  # красный
    all_bodies.append(Body(1, mass, (890, 300), Vector((0, 0)), (0, 255, 0)))  # зеленый
    all_bodies.append(Body(2, mass, (900, 900), Vector((0, 0)), (0, 0, 255)))  # синий
    game = World(all_bodies)

    pygame.init()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        for elem in game.bodies:
            pygame.draw.circle(screen, elem.color, elem.coords, 20)

            k = 1
            if elem.coords[0] <= 0 or elem.coords[0] >= WIDTH:
                elem.velocity.coords = (-1 * elem.velocity.coords[0] * k, elem.velocity.coords[1])
                if elem.coords[0] <= 0:
                    elem.coords = (1, elem.coords[1])
                if elem.coords[0] >= WIDTH:
                    elem.coords = (WIDTH - 1, elem.coords[1])
            if elem.coords[1] <= 0 or elem.coords[1] >= HEIGHT:
                elem.velocity.coords = (elem.velocity.coords[0], elem.velocity.coords[1] * -1 * k)
                if elem.coords[0] <= 0:
                    elem.coords = (elem.coords[0], 1)
                if elem.coords[0] >= HEIGHT:
                    elem.coords = (elem.coords[0], HEIGHT - 1)

        game.count_all_forces_and_change_velocities()

        pygame.display.flip()
    pygame.quit()
