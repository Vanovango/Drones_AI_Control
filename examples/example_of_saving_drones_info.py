
import pygame as pg

WIDTH = 1280
HIGH = 720
FPS = 60

SPEED = 20

window = pg.display.set_mode((WIDTH, HIGH))
clock = pg.time.Clock()

DRONES = {
    1: pg.image.load('../images/MASTER_drone.png')
}

DRONES_RECT = {
    1: DRONES[1].get_rect(centerx=WIDTH // 2, centery=HIGH // 2)
}


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            raise SystemExit

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                DRONES_RECT[1].move_ip(0, -SPEED)
            elif event.key == pg.K_DOWN:
                DRONES_RECT[1].move_ip(0, +SPEED)
            elif event.key == pg.K_LEFT:
                DRONES_RECT[1].move_ip(-SPEED, 0)
            elif event.key == pg.K_RIGHT:
                DRONES_RECT[1].move_ip(+SPEED, 0)
            # print current position of drone center: type - tuple
            print(DRONES_RECT[1].center)

    window.fill(pg.Color('black'))

    window.blit(DRONES[1], DRONES_RECT[1])   # draw DRONES
    pg.draw.circle(window, pg.Color('blue'), DRONES_RECT[1].center, 200, 2)  # draw circle around DRONES

    pg.display.update()
    clock.tick(FPS)
