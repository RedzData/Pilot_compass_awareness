import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Airport Locator Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Airport coordinates (for example)
airport_x, airport_y = 400, 300

# Plane class
class Plane:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.angle = 0

    def update(self, mouse_pos):
        self.x, self.y = mouse_pos
        dx = self.x - airport_x
        dy = self.y - airport_y
        self.angle = math.atan2(-dy, dx)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 20, 20))

    def draw_compass(self):
        compass_font = pygame.font.SysFont(None, 30)
        compass_text = compass_font.render("N", True, WHITE)
        screen.blit(compass_text, (width // 2 - 10, height // 2 - 50))
        compass_text = compass_font.render("S", True, WHITE)
        screen.blit(compass_text, (width // 2 - 10, height // 2 + 60))
        compass_text = compass_font.render("W", True, WHITE)
        screen.blit(compass_text, (width // 2 - 60, height // 2 + 10))
        compass_text = compass_font.render("E", True, WHITE)
        screen.blit(compass_text, (width // 2 + 40, height // 2 + 10))

# Initialize plane object
plane = Plane()

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Update plane position and angle
    plane.update(mouse_pos)

    # Draw plane
    plane.draw()

    # Draw compass
    plane.draw_compass()

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
