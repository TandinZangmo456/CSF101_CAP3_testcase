import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 600, 500
PLAYER_COUNT = 1  # Set number of players

# Define font
font = pygame.font.Font(None, 32)

# Scoring
high_score = 0
score = 0
score_text = font.render("Score: " + str(score), True, (255, 255, 255))

# Game Over
game_over = False

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("space1.jpg").convert()

# Image setup
def load_and_resize_image(image_path, size):
    image = pygame.image.load(image_path).convert()
    return pygame.transform.scale(image, size)

mouse_image = load_and_resize_image("mouse.jpg", (50, 50))
trash_image = load_and_resize_image("trash.jpg", (50, 50))
player_image = load_and_resize_image("cat.jpg", (50, 50))

# Drawing function for images
def draw_image(surface, image, x, y):
    surface.blit(image, (x, y))

# Player class
class Player:
    def __init__(self, image, x, y):
        self.image = image
        self.x, self.y = x, y

# Define start menu function
def draw_start_menu():
    screen.fill((0, 0, 0))  # Fill the screen with black
    title = font.render('My Game', True, (255, 255, 255))
    start_button = font.render('Press SPACE to start', True, (255, 255, 255))
    high_score_text = font.render('High Score: ' + str(high_score), True, (255, 255, 255))
    instructions = font.render('Press LEFT and RIGHT to move, UP to jump', True, (255, 255, 255))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - title.get_height() // 2))
    screen.blit(start_button, (WIDTH // 2 - start_button.get_width() // 2, HEIGHT // 2 + 50))
    screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(instructions, (WIDTH // 2 - instructions.get_width() // 2, HEIGHT // 2 + title.get_height() + high_score_text.get_height() + 20))
    pygame.display.update()

# Players initialization
players = [Player(player_image, WIDTH // 2, HEIGHT - 100) for _ in range(PLAYER_COUNT)]

# Mouse and Trash initialization
def reset_positions():
    return random.randint(0, WIDTH - 100), random.randint(0, HEIGHT - 100)

mouseX, mouseY = reset_positions()
trashX, trashY = reset_positions()

# Function to draw image on the surface
def draw_image(surface, image, x, y):
    surface.blit(image, (x, y))

# Counter initialization
counter = 0

# Main game loop
running = True
start_menu = True

def check_collision(player_x, player_y, trash_x, trash_y):

    if (
        player_x < trash_x + 50
        and player_x + 50 > trash_x
        and player_y < trash_y + 50
        and player_y + 50 > trash_y
    ):
        return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start_menu:
                start_menu = False

    if start_menu:
        draw_start_menu()
    else:
        counter += 1
        if counter >= 100:
            mouseX, mouseY = reset_positions()
            trashX, trashY = reset_positions()
            counter = 0

        for player in players:
            keys = pygame.key.get_pressed()
            player_speed = 3
            if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= player_speed
            if keys[pygame.K_RIGHT] and player.x < WIDTH - player_speed:
                player.x += player_speed
            if keys[pygame.K_UP] and player.y > 0:
                player.y -= player_speed
            if keys[pygame.K_DOWN] and player.y < HEIGHT - player_speed:
                player.y += player_speed

                if player.x < 0 or player.x > WIDTH:
                    game_over = True

        screen.fill((255, 0, 0))
        screen.blit(bg, (0, 0))

        draw_image(screen, mouse_image, mouseX, mouseY)
        draw_image(screen, trash_image, trashX, trashY)

        for player in players:
            draw_image(screen, player.image, player.x, player.y)

        for player in players:
            if player.x < mouseX < player.x + 50 and player.y < mouseY < player.y + 50:
                score += 1
                if score == 50:
                    game_over = True
                mouseX, mouseY = reset_positions()

        for player in players:
            if player.x < trashX < player.x + 50 and player.y < trashY < player.y + 50:
                game_over = True
        
        for player in players:
            if check_collision(player.x, player.y, trashX, trashY):
                game_over = True

        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        mouseX += random.randint(-1, 1)
        mouseY += random.randint(-1, 1)
        trashX += random.randint(-1, 1)
        trashY += random.randint(-1, 1)

        if mouseX < 0 or mouseX > WIDTH:
            mouseX, mouseY = reset_positions()
        if mouseY < 0 or mouseY > HEIGHT:
            mouseX, mouseY = reset_positions()

        if trashX < 0 or trashX > WIDTH:
            trashX, trashY = reset_positions()
        if trashY < 0 or trashY > HEIGHT:
            trashX, trashY = reset_positions()

       

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
                    score = 0

pygame.quit()
sys.exit()
