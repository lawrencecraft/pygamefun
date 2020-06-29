import pygame
import time
import random

def game_loop(window):
    clock = pygame.time.Clock()
    stop = False

    circle_coords = [250, 250]
    circle_radius = 10
    velocity = [0,0]

    painted = pygame.Surface((500, 500))

    drawing = True

    event_vel_map = {
        pygame.K_UP: [0, -1],
        pygame.K_DOWN: [0, 1],
        pygame.K_RIGHT: [1, 0],
        pygame.K_LEFT: [-1, 0]
    }

    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 255)
    ]

    color = random.choice(colors)

    while not stop:
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Ended")
                stop = True
            elif event.type == pygame.KEYDOWN and (event.key == pygame.K_q or event.key == pygame.K_ESCAPE):
                print("Q pressed")
                stop = True
            elif event.type == pygame.KEYDOWN and event.key in event_vel_map:
                dv = event_vel_map[event.key]

                velocity[0] += dv[0]
                velocity[1] += dv[1]

            elif event.type == pygame.KEYUP and event.key in event_vel_map:
                dv = event_vel_map[event.key]

                velocity[0] -= dv[0]
                velocity[1] -= dv[1]
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                drawing = not drawing
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                oldColor = color
                while color == oldColor:
                    color = random.choice(colors)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                painted.fill((0, 0, 0))
        
        
        circle_coords[0] = min(max(circle_coords[0] + velocity[0], circle_radius), 500 - circle_radius)
        circle_coords[1] = min(max(circle_coords[1] + velocity[1], circle_radius), 500 - circle_radius)

        if drawing:
           pygame.draw.circle(painted, color, circle_coords, circle_radius)

        window.blit(painted, (0, 0))

        pygame.draw.circle(window, (127, 127, 127), circle_coords, circle_radius)
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


def main():
    pygame.init()
    window = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Pygame test")

    game_loop(window)


if __name__ == "__main__":
    main()
