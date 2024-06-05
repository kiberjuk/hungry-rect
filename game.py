import time
from classes import*
from vars import name,scores
from sql import *

def game(name, score):
    pygame.init()

    # Главный цикл игры
    player = Player()
    player.set_name_scores(name, scores)
    all_sprites = pygame.sprite.Group()
    small_rectangles = pygame.sprite.Group()
    all_sprites.add(player)


    running = True
    clock = pygame.time.Clock()

    game_over = False
    game_over_timer = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not game_over:
            all_sprites.update()

            # Создание новых маленьких прямоугольников
            if len(small_rectangles) < 3 and random.randint(0, 100) < 2:
                small_rectangle = SmallRectangle()
                all_sprites.add(small_rectangle)
                small_rectangles.add(small_rectangle)

            # Проверка столкновения игрока с маленькими прямоугольниками
            hits = pygame.sprite.spritecollide(player, small_rectangles, True)
            for hit in hits:
                player.score += 1

            # Проверка на конец игры
            for rect in small_rectangles:
                if rect.rect.y > HEIGHT:
                    game_over = True
                    game_over_timer = time.time()


            screen.fill(WHITE)
            all_sprites.draw(screen)

            # Отображение счёта
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Счёт: {player.score}", True, RED)
            screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
            # Отображение игрока
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Игрок: {player.name}", True, RED)
            screen.blit(score_text, (WIDTH - score_text.get_width() - 150, 10))

        else:
            if time.time() - game_over_timer > 5:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()