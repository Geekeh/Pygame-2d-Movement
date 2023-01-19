import pygame

pygame.init()

width = 1280
height = 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tutorial Video")
clock = pygame.time.Clock()

p_pos = pygame.Vector2(50, 610)
player_speed = 5
while True:

    player = pygame.Rect(int(p_pos.x), int(p_pos.y), 50, 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        

    if pygame.key.get_pressed()[pygame.K_w]:
        p_pos.y -= player_speed
    if pygame.key.get_pressed()[pygame.K_s]:
        p_pos.y += player_speed
    if pygame.key.get_pressed()[pygame.K_d]:
        p_pos.x += player_speed
    if pygame.key.get_pressed()[pygame.K_a]:
        p_pos.x -= player_speed

    screen.fill(0x0000ff)
    pygame.draw.rect(screen, 0xff0000, player)
    pygame.display.update()
    clock.tick(60)
