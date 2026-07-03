# THIS WAS MADE ENTIRELY BY MICROSOFT BING'S CHAT AI
## NO PART OF THIS WAS MADE BY A HUMAN
### ALL CREDIT GOES TO MICROSOFT BING CHAT

# Import pygame module
import pygame

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen surface
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the window title
pygame.display.set_caption("Platformer")

# Define the gravity constant
GRAVITY = 1

# Define the player class
class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y):
        # Call the parent class constructor
        super().__init__()

        # Set the image and rect attributes
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        # Set the initial position
        self.rect.x = x
        self.rect.y = y

        # Set the initial velocity
        self.vx = 0
        self.vy = 0

    # Update the player position and velocity
    def update(self):
        # Apply gravity
        self.vy += GRAVITY

        # Move horizontally
        self.rect.x += self.vx

        # Check for horizontal collisions with platforms
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for platform in collision_list:
            # If moving right, set the right edge to the left edge of the platform
            if self.vx > 0:
                self.rect.right = platform.rect.left
            # If moving left, set the left edge to the right edge of the platform
            elif self.vx < 0:
                self.rect.left = platform.rect.right

            # Stop horizontal movement
            self.vx = 0

        # Move vertically
        self.rect.y += self.vy

        # Check for vertical collisions with platforms
        collision_list = pygame.sprite.spritecollide(self, platform_list, False)
        for platform in collision_list:
            # If falling down, set the bottom edge to the top edge of the platform
            if self.vy > 0:
                self.rect.bottom = platform.rect.top
            # If jumping up, set the top edge to the bottom edge of the platform
            elif self.vy < 0:
                self.rect.top = platform.rect.bottom

            # Stop vertical movement
            self.vy = 0

# Define the platform class
class Platform(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, x, y, width, height):
        # Call the parent class constructor
        super().__init__()

        # Set the image and rect attributes
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # Set the position
        self.rect.x = x
        self.rect.y = y

# Create a group for all sprites
all_sprites_list = pygame.sprite.Group()

# Create a group for platforms
platform_list = pygame.sprite.Group()

# Create a player object and add it to the sprite group
player = Player(100, 450)
all_sprites_list.add(player)

# Create some platforms and add them to the sprite and platform groups
platform1 = Platform(0, 550, 800, 50)
all_sprites_list.add(platform1)
platform_list.add(platform1)

platform2 = Platform(200, 400, 100, 20)
all_sprites_list.add(platform2)
platform_list.add(platform2)

platform3 = Platform(400, 300, 150, 30)
all_sprites_list.add(platform3)
platform_list.add(platform3)

platform4 = Platform(600, 200, 100, 20)
all_sprites_list.add(platform4)
platform_list.add(platform4)

# Define a clock object to control the frame rate
clock = pygame.time.Clock()

# Define a boolean variable to indicate the game loop condition
running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        # If the user clicks the close button, exit the game loop
        if event.type == pygame.QUIT:
            running = False
        
        # If the user presses a key down
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.vx = -5
            # If the key is the right arrow, set the horizontal velocity to 5
            elif event.key == pygame.K_RIGHT:
                player.vx = 5
            # If the key is the space bar and the player is on a platform, set the vertical velocity to -15
            elif event.key == pygame.K_SPACE and player.rect.bottom in [platform.rect.top for platform in platform_list]:
                player.vy = -20
        
        # If the user releases a key
        elif event.type == pygame.KEYUP:
            # If the key is the left or right arrow, stop the horizontal movement
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.vx = 0

    # Update the sprites
    all_sprites_list.update()

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the sprites
    all_sprites_list.draw(screen)

    # Update the display
    pygame.display.flip()

    # Set the frame rate to 60 FPS
    clock.tick(60)

# Quit pygame
pygame.quit()