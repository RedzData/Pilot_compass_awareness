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
BROWN = (139, 69, 19)

# Load airport image
airport_image = pygame.image.load('C:/Users/redzo/pilot_location/Airport.png')
airport_rect = airport_image.get_rect(center=(width//2.1, height//1.9))

# Plane class
class Plane:
    def __init__(self):
        self.x = width // 2
        self.y = height // 2
        self.angle = 0

    def update(self, mouse_pos):
        self.x, self.y = mouse_pos
        dx = self.x - airport_rect.centerx
        dy = self.y - airport_rect.centery
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

    def draw_location(self):
        location_font = pygame.font.SysFont(None, 20)
        dx = self.x - airport_rect.centerx
        dy = self.y - airport_rect.centery
        if dx == 0 and dy == 0:
            direction = "at the airport"
        else:
            if abs(dx) > abs(dy):
                if dx > 0:
                    direction = "East"
                else:
                    direction = "West"
            else:
                if dy > 0:
                    direction = "South"
                else:
                    direction = "North"
        location_text = location_font.render(f"N123AB {direction} of the airport", True, WHITE)
        screen.blit(location_text, (10, 10))

# Initialize plane object
plane = Plane()

# Main loop
running = True
while running:
    screen.fill(BROWN)  # Set background color to brown
    
    # Blit airport image
    screen.blit(airport_image, airport_rect)

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

    # Draw location information
    plane.draw_location()

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
