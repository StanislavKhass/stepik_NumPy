
# Example file showing a circle moving on screen
import pygame
import sys




pygame.init()

#print("Результат вычитания двух веторов = радиус вектор",result)
#print("Результат вычитания двух веторов =  модуль вектора",result_modul)

screen = pygame.display.set_mode((1014, 720))
FPSCLOCK = pygame.time.Clock()
RED = pygame.Color("red")
GREEN = pygame.Color("green")
WHITE = pygame.Color("white")

COLOR_IN_VECTOR = pygame.Color("purple")

center_position =  pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)

vector1 = pygame.Vector2(center_position.x ,center_position.y)
vector2 = pygame.Vector2(100 + center_position.x , center_position.y)

vector3 = pygame.Vector2(center_position.x+100 ,center_position.y)
vector4 = pygame.Vector2(100 + center_position.x , -100 +center_position.y)


vector5 = pygame.Vector2(center_position.x+100 ,-100+center_position.y)
vector6 = pygame.Vector2(center_position.x , -100 +center_position.y)

vector7 = pygame.Vector2(center_position.x ,-100+center_position.y)
vector8 = pygame.Vector2(center_position.x , 0 +center_position.y)


vector_startpoint =  pygame.Vector2(800 ,800)
vector_endpoint =  pygame.Vector2(600 ,700)
radius_vector = vector_endpoint - vector_startpoint

print(radius_vector.x, radius_vector.y)

angle = 360
done = False

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    angle = angle  % 360


    pygame.draw.line(screen, "red", (vector1.x , vector1.y) , (vector2.x , vector2.y) ,1)
    pygame.draw.circle(screen, "green", (vector2.x , vector2.y), 3)
    pygame.draw.line(screen, "red", (vector3.x , vector3.y) , (vector4.x , vector4.y) ,1)
    pygame.draw.circle(screen, "green", (vector4.x , vector4.y), 3)
    pygame.draw.line(screen, "red", (vector5.x , vector5.y) , (vector6.x , vector6.y) ,1)
    pygame.draw.circle(screen, "green", (vector6.x , vector6.y), 3)
    pygame.draw.line(screen, "red", (vector7.x , vector7.y) , (vector8.x , vector8.y) ,1)
    pygame.draw.circle(screen, "green", (vector8.x , vector8.y), 3)



    pygame.draw.line(screen, "green", (center_position.x , center_position.y ) , (center_position.x+radius_vector.x , center_position.y+(-radius_vector.y)) ,1)



    pygame.draw.circle(screen, "green", (center_position.x+radius_vector.x , center_position.y+(-radius_vector.y)), 3)




    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 1
    if keys[pygame.K_s]:
        player_pos.y += 1
    if keys[pygame.K_a]:
        player_pos.x -= 1
    if keys[pygame.K_d]:
        player_pos.x += 1

    if player_pos.x >= center_position.x + 0 and player_pos.x <= + center_position.x + 100 and \
    player_pos.y <= center_position.y + 0 and player_pos.y >= center_position.y + (-100):
        COLOR_IN_VECTOR = pygame.Color("white")
    else:
        COLOR_IN_VECTOR = pygame.Color("purple")
    pygame.draw.circle(screen, COLOR_IN_VECTOR, (player_pos.x , player_pos.y), 3)

    pygame.display.flip()
    FPSCLOCK.tick(60)

pygame.quit()
sys.exit()
