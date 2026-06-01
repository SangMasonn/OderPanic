import pygame
from core.settings import WIDTH, HEIGHT, FPS
from entities.player import Player
from entities.station import Station
from entities.customer import Customer

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Order Panic")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

player1 = Player(100, 500, (255, 0, 0))
player2 = Player(300, 500, (0, 0, 255))

tables = [
    Station(100, 80, 150, 80, "Table 1", (120, 80, 40)),
    Station(420, 80, 150, 80, "Table 2", (120, 80, 40)),
    Station(740, 80, 150, 80, "Table 3", (120, 80, 40)),
]

customers = [
    Customer(tables[0]),
    Customer(tables[1])
]

ingredient_station = Station(80, 580, 200, 80, "Ingredients", (80, 120, 80))
cook_station = Station(400, 580, 200, 80, "Cook", (150, 80, 80))
serve_station = Station(720, 580, 200, 80, "Serve", (80, 80, 150))
score = 0
served_customers = 0

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player1.move(keys, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)
    player2.move(keys, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)

    # Player 1 nhận order
    if keys[pygame.K_e]:
        player1_rect = pygame.Rect(
            player1.x,
            player1.y,
            player1.size,
            player1.size
        )

        for customer in customers:
            if player1_rect.colliderect(customer.table.rect):
                customer.order_taken = True

    # Player 2 lấy món ở khu Ingredients
        # Player 2 lấy món hoặc giao món
    if keys[pygame.K_RETURN]:
        player2_rect = pygame.Rect(
            player2.x,
            player2.y,
            player2.size,
            player2.size
        )

        # Lấy món ở Ingredients
        if player2_rect.colliderect(ingredient_station.rect):
            for customer in customers:
                if customer.order_taken and not customer.finished:
                    player2.holding_food = customer.food
                    break

        # Giao món cho khách
        for customer in customers:
            if player2_rect.colliderect(customer.table.rect):
                if customer.order_taken and not customer.finished:
                    if player2.holding_food == customer.food:
                        customer.finished = True
                        player2.holding_food = None
                        score += 100
                        served_customers += 1

    for customer in customers:
        customer.update()

    screen.fill((35, 35, 35))

    for table in tables:
        table.draw(screen, font)

    for customer in customers:
        customer.draw(screen, font)

    ingredient_station.draw(screen, font)
    cook_station.draw(screen, font)
    serve_station.draw(screen, font)
    

    player1.draw(screen)
    player2.draw(screen)

    if player2.holding_food:
        text = font.render(
            "Holding: " + player2.holding_food,
            True,
            (255, 255, 255)
        )
        screen.blit(text, (20, 20))

    score_text = font.render(
        "Score: " + str(score),
        True,
        (255, 255, 255)
    )
    screen.blit(score_text, (20, 50))

    served_text = font.render(
        "Served: " + str(served_customers),
        True,
        (255, 255, 255)
    )
    screen.blit(served_text, (20, 80))

    pygame.display.update()

pygame.quit()