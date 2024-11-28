import pygame
import random
import time
from gpiozero import Button

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 1368
screen_height = 768

# Colors
black = (0, 0, 0)
almond = (239, 222, 205)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
tail = (114, 160, 193)

# Set up display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Racing Game by Omer and Evyatar")

# Load images
car1_image = pygame.image.load('car1.png')
car2_image = pygame.image.load('car2.png')
coin_image = pygame.image.load('coin.png')
obstacle_image = pygame.image.load('obstacle.png')
power_up_image = pygame.image.load('power_up.png')
car_width = 50
car_height = 100

# Load sounds
coin_sound = pygame.mixer.Sound('coin.wav')
collision_sound = pygame.mixer.Sound('collision.wav')
power_up_sound = pygame.mixer.Sound('power_up.wav')
winning_sound = pygame.mixer.Sound('win.wav')  # Add this line to load the winning sound
pygame.mixer.music.load('background_music.mp3')

# Fonts
font = pygame.font.SysFont(None, 55)
large_font = pygame.font.SysFont(None, 75)

# GPIO Button setup
btn_car1_up = Button(3)
btn_car1_down = Button(2)
btn_car1_left = Button(10)
btn_car1_right = Button(4)
btn_car2_up = Button(21)
btn_car2_down = Button(20)
btn_car2_left = Button(16)
btn_car2_right = Button(12)

# Function to draw text
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Function to draw cars
def draw_car(x, y, car_image):
    screen.blit(car_image, (x, y))

# Function to draw obstacles
def draw_obstacle(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle[0], obstacle[1]))

# Function to draw coins
def draw_coin(coins):
    for coin in coins:
        screen.blit(coin_image, (coin[0], coin[1]))

# Function to draw power-ups
def draw_power_up(power_ups):
    for power_up in power_ups:
        screen.blit(power_up_image, (power_up[0], power_up[1]))

# Pause menu
def pause_menu():
    paused = True
    while paused:
        screen.fill(white)
        draw_text('Game Paused', large_font, black, screen, screen_width // 2 - 200, screen_height // 2 - 200)
        draw_text('1. Resume Game', font, black, screen, screen_width // 2 - 200, screen_height // 2 - 50)
        draw_text('2. Quit Game', font, black, screen, screen_width // 2 - 200, screen_height // 2 + 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    paused = False
                elif event.key == pygame.K_2:
                    pygame.quit()
                    quit()

# Main menu
def main_menu():
    menu = True
    while menu:
        screen.fill(tail)
        draw_text('Omer and Evyatar present:', large_font, black, screen, screen_width // 2 - 350, screen_height // 2 - 300)
        draw_text('The Racing Game', large_font, black, screen, screen_width // 2 - 250, screen_height // 2 - 200)
        draw_text('1. Start Game', font, black, screen, screen_width // 2 - 200, screen_height // 2 - 50)
        draw_text('2. Instructions', font, black, screen, screen_width // 2 - 200, screen_height // 2 + 50)
        draw_text('3. Quit', font, black, screen, screen_width // 2 - 200, screen_height // 2 + 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_time_menu()
                elif event.key == pygame.K_2:
                    instructions()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    quit()

# Instructions screen
def instructions():
    instruction = True
    while instruction:
        screen.fill(tail)
        draw_text('Instructions', large_font, black, screen, screen_width // 2 - 250, screen_height // 2 - 300)
        draw_text('1. Use buttons to move the cars', font, black, screen, screen_width // 2 - 600, screen_height // 2 - 150)
        draw_text('2. Collect coins to score points', font, black, screen, screen_width // 2 - 600, screen_height // 2 + 50)
        draw_text('3. Avoid obstacles', font, black, screen, screen_width // 2 - 600, screen_height // 2 + 150)
        draw_text('4. Collect power-ups to gain advantages', font, black, screen, screen_width // 2 - 600, screen_height // 2 + 250)
        draw_text('Press ENTER to return to main menu', font, black, screen, screen_width // 2 - 200, screen_height // 2 + 350)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    instruction = False

# Game time selection menu
def game_time_menu():
    game_time = 60  # default game time
    menu = True
    while menu:
        screen.fill(tail)
        draw_text('Select Game Time', large_font, black, screen, screen_width // 2 - 250, screen_height // 2 - 200)
        draw_text('1. 30 seconds', font, black, screen, screen_width // 2 - 200, screen_height // 2 - 50)
        draw_text('2. 60 seconds', font, black, screen, screen_width // 2 - 200, screen_height // 2 + 50)
        draw_text('3. 90 seconds', font, black, screen, screen_width // 2 - 200, screen_height // 2 + 150)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_time = 30
                    menu = False
                elif event.key == pygame.K_2:
                    game_time = 60
                    menu = False
                elif event.key == pygame.K_3:
                    game_time = 90
                    menu = False

    game_loop(game_time)

# Game loop
def game_loop(game_time):
    # Player positions
    car1_x = screen_width * 0.2
    car1_y = screen_height * 0.8
    car2_x = screen_width * 0.7
    car2_y = screen_height * 0.8

    # Speeds
    car1_speed = 5
    car2_speed = 5
    car1_x_change = 0
    car2_x_change = 0
    car1_y_change = 0
    car2_y_change = 0
    base_speed = 5
    slowdown_rate = 2  # Adjust slowdown rate as needed
    power_up_boost = 2  # Speed boost multiplier

    # Cooldown timers for collisions
    car1_last_collision_time = 0
    car2_last_collision_time = 0
    collision_cooldown = 2  # seconds

    # Obstacle parameters
    obstacle_width = 50
    obstacle_height = 50
    obstacle_speed = 10  # Faster obstacles
    obstacles = []

    # Coin parameters
    coin_width = 30
    coin_height = 30
    coins = []

    # Power-up parameters
    power_up_width = 30
    power_up_height = 30
    power_ups = []
    car1_power_up_active = False
    car2_power_up_active = False
    car1_power_up_start_time = 0
    car2_power_up_start_time = 0

    # Scores
    car1_score = 0
    car2_score = 0

    # Game clock
    clock = pygame.time.Clock()
    game_exit = False
    start_time = time.time()
    extra_time = False

    # Play background music
    pygame.mixer.music.play(-1)

    # Function to create obstacles
    def create_obstacle():
        obstacle_x = random.randrange(0, screen_width - obstacle_width)
        obstacle_y = -obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

    # Function to create coins
    def create_coin():
        coin_x = random.randrange(0, screen_width - coin_width)
        coin_y = -coin_height
        coins.append([coin_x, coin_y])

    # Function to create power-ups
    def create_power_up():
        power_up_x = random.randrange(0, screen_width - power_up_width)
        power_up_y = -power_up_height
        power_ups.append([power_up_x, power_up_y])

    # Function to show scores and time
    def show_scores_and_time(car1_score, car2_score, elapsed_time, extra_time):
        text1 = font.render(f'Player 1 Score: {car1_score}', True, black)
        text2 = font.render(f'Player 2 Score: {car2_score}', True, black)
        remaining_time = max(game_time - int(elapsed_time), 0)
        if extra_time:
            time_text = font.render(f'Time Left: {remaining_time + 10}s', True, red)
        else:
            time_text = font.render(f'Time Left: {remaining_time}s', True, black)
        screen.blit(text1, (10, 10))
        screen.blit(text2, (screen_width - 350, 10))
        screen.blit(time_text, (screen_width // 2 - 100, 10))

    # Main game loop
    while not game_exit:
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > game_time and not extra_time:
            if car1_score == car2_score:
                extra_time = True
                start_time += 10  # Add 10 seconds
            else:
                game_exit = True
        elif elapsed_time > game_time + 10:  # Extra 10 seconds if tie
            game_exit = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_menu()

        # Update car positions based on GPIO button states and current speed
        car1_y_change = -car1_speed if btn_car1_up.is_pressed else (car1_speed if btn_car1_down.is_pressed else 0)
        car1_x_change = -car1_speed if btn_car1_left.is_pressed else (car1_speed if btn_car1_right.is_pressed else 0)
        car2_y_change = -car2_speed if btn_car2_up.is_pressed else (car2_speed if btn_car2_down.is_pressed else 0)
        car2_x_change = -car2_speed if btn_car2_left.is_pressed else (car2_speed if btn_car2_right.is_pressed else 0)

        # Apply speed changes from power-ups
        if car1_power_up_active:
            car1_y_change *= power_up_boost
            car1_x_change *= power_up_boost
            if time.time() - car1_power_up_start_time >= 5:
                car1_power_up_active = False

        if car2_power_up_active:
            car2_y_change *= power_up_boost
            car2_x_change *= power_up_boost
            if time.time() - car2_power_up_start_time >= 5:
                car2_power_up_active = False

        # Update car positions
        car1_y += car1_y_change
        car2_y += car2_y_change
        car1_x += car1_x_change
        car2_x += car2_x_change

        # Keep cars within screen boundaries
        car1_x = max(0, min(car1_x, screen_width - car_width))
        car2_x = max(0, min(car2_x, screen_width - car_width))
        car1_y = max(0, min(car1_y, screen_height - car_height))
        car2_y = max(0, min(car2_y, screen_height - car_height))

        # Update obstacle positions
        for obstacle in obstacles:
            obstacle[1] += obstacle_speed

        # Update coin positions
        for coin in coins:
            coin[1] += obstacle_speed

        # Update power-up positions
        for power_up in power_ups:
            power_up[1] += obstacle_speed

        # Create new obstacles, coins, and power-ups
        if len(obstacles) < 10 and random.randint(0, 100) < 5:
            create_obstacle()
        if len(coins) < 10 and random.randint(0, 100) < 2:
            create_coin()
        if len(power_ups) < 2 and random.randint(0, 100) < 1:
            create_power_up()

        # Remove off-screen obstacles, coins, and power-ups
        obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]
        coins = [coin for coin in coins if coin[1] < screen_height]
        power_ups = [power_up for power_up in power_ups if power_up[1] < screen_height]

        # Define car rectangles for collision detection
        car1_rect = pygame.Rect(car1_x, car1_y, car_width, car_height)
        car2_rect = pygame.Rect(car2_x, car2_y, car_width, car_height)

        # Check for collisions with obstacles
        car1_collided = False
        car2_collided = False

        for obstacle in obstacles[:]:
            obstacle_rect = pygame.Rect(obstacle[0], obstacle[1], obstacle_width, obstacle_height)
            if car1_rect.colliderect(obstacle_rect):
                current_time = time.time()
                if current_time - car1_last_collision_time > collision_cooldown:
                    car1_collided = True
                    car1_last_collision_time = current_time
                    obstacles.remove(obstacle)

            if car2_rect.colliderect(obstacle_rect):
                current_time = time.time()
                if current_time - car2_last_collision_time > collision_cooldown:
                    car2_collided = True
                    car2_last_collision_time = current_time
                    obstacles.remove(obstacle)

        # Check for collisions between cars
        if car1_rect.colliderect(car2_rect):
            current_time = time.time()
            if current_time - car1_last_collision_time > collision_cooldown:
                car1_collided = True
                car1_last_collision_time = current_time
            if current_time - car2_last_collision_time > collision_cooldown:
                car2_collided = True
                car2_last_collision_time = current_time

        # Slow down cars on collision
        if car1_collided:
            car1_speed -= slowdown_rate  # Apply slowdown
            if car1_speed < base_speed:
                car1_speed = base_speed  # Ensure speed doesn't go below base speed
            pygame.mixer.Sound.play(collision_sound)
        if car2_collided:
            car2_speed -= slowdown_rate  # Apply slowdown
            if car2_speed < base_speed:
                car2_speed = base_speed  # Ensure speed doesn't go below base speed
            pygame.mixer.Sound.play(collision_sound)

        # Check for collisions with coins
        for coin in coins[:]:
            coin_rect = pygame.Rect(coin[0], coin[1], coin_width, coin_height)
            if car1_rect.colliderect(coin_rect):
                coins.remove(coin)
                car1_score += 1
                pygame.mixer.Sound.play(coin_sound)
            if car2_rect.colliderect(coin_rect):
                coins.remove(coin)
                car2_score += 1
                pygame.mixer.Sound.play(coin_sound)

        # Check for collisions with power-ups
        for power_up in power_ups[:]:
            power_up_rect = pygame.Rect(power_up[0], power_up[1], power_up_width, power_up_height)
            if car1_rect.colliderect(power_up_rect):
                power_ups.remove(power_up)
                car1_power_up_active = True
                car1_power_up_start_time = time.time()
                pygame.mixer.Sound.play(power_up_sound)
            if car2_rect.colliderect(power_up_rect):
                power_ups.remove(power_up)
                car2_power_up_active = True
                car2_power_up_start_time = time.time()
                pygame.mixer.Sound.play(power_up_sound)

        # Draw everything
        screen.fill(almond)
        draw_car(car1_x, car1_y, car1_image)
        draw_car(car2_x, car2_y, car2_image)
        draw_obstacle(obstacles)
        draw_coin(coins)
        draw_power_up(power_ups)
        show_scores_and_time(car1_score, car2_score, elapsed_time, extra_time)
        pygame.display.update()

        # Frame rate
        clock.tick(60)

    # Stop background music
    pygame.mixer.music.stop()

    # Play winning sound
    pygame.mixer.Sound.play(winning_sound)

    # Display winner
    winner = ""
    if car1_score > car2_score:
        winner = "Player 1 Wins!"
    elif car2_score > car1_score:
        winner = "Player 2 Wins!"
    else:
        winner = "It's a Tie!"

    screen.fill(white)
    draw_text(winner, large_font, black, screen, screen_width // 2 - 200, screen_height // 2 - 100)
    draw_text('Press ENTER to return to the main menu', font, black, screen, screen_width // 2 - 350, screen_height // 2)
    pygame.display.update()

    wait_for_input = True
    while wait_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    wait_for_input = False

# Run the game
main_menu()
