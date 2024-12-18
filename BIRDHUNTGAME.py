import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
SKY_BLUE = (135, 206, 235)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bird Shooting Game")

bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (50, 50))

background_image = pygame.image.load("background.jpG")
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

class Bird:
    def __init__(self):
        self.reset()
        self.hit = False  

    def move(self):
        if not self.hit:  
            self.x += self.speed
            if self.x > SCREEN_WIDTH:
                self.reset()
                return True  
        return False

    def reset(self):
        self.x = -50
        self.y = random.randint(50, SCREEN_HEIGHT - 150)
        self.speed = random.uniform(1.5, 3.5)  
        self.hit = False  

    def draw(self):
        if not self.hit: 
            screen.blit(bird_image, (self.x, self.y))


def show_start_screen():
    screen.blit(background_image, (0, 0)) 
    title_font = pygame.font.Font(None, 74)
    start_text = font.render("Start", True, BLACK)
    title_text = title_font.render("Bird Shooting Game", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


def show_game_over_screen():
    screen.fill(WHITE)
    game_over_text = font.render("Game Over!", True, BLACK)
    final_score_text = font.render(f"Final Score: {score}", True, BLACK)
    restart_text = font.render("Click to Restart", True, BLACK)
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))
    screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False


font = pygame.font.Font(None, 36)
birds = [Bird() for _ in range(3)]  
score = 0
misses = 0

show_start_screen()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for bird in birds:
                if bird.x < mouse_x < bird.x + 50 and bird.y < mouse_y < bird.y + 50 and not bird.hit:
                    score += 1
                    bird.hit = True  
                    bird.reset()  
                    for bird in birds:
                        bird.speed = min(bird.speed + 0.05, 5.0)  
                    break

    
    screen.blit(background_image, (0, 0))  
    for bird in birds:
        if bird.move():
            misses += 1
        bird.draw()

   
    if misses >= 5: 
        show_game_over_screen()
        score = 0  
        misses = 0  
        birds = [Bird() for _ in range(3)]  

 
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
