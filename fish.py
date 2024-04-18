import pygame
import random

# start pygame
pygame.init()

# screen dimensions
screen_width, screen_height = 1300, 576

# display 
window = pygame.display.set_mode((screen_width, screen_height))

# images
background_image = pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/background.png')
player_image = pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/fisherman.png')
rod_image = pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/rod.png')

# select each fish image randomly from available options
def choose_fish_image():
    fish_images = [
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/fish_1.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/fish_2.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/fish_3.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/fish_4.png')
    ]
    return random.choice(fish_images)

# select each trash image randomly from available options
def choose_trash_image():
    trash_images = [
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/boot.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/boot.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/boot.png')
    ]
    return random.choice(trash_images)

# select each hostile fish image randomly from available options
def choose_hostile_fish_image():
    hostile_fish_images = [
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/hostile_fish_1.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/hostile_fish_2.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/hostile_fish_3.png'),
        pygame.image.load('/Users/zoe/Documents/seo/fish_game/images/hostile_fish_4.png')
    ]
    return random.choice(hostile_fish_images)

# player location and speed
player_x = screen_width // 2
player_y = screen_height - 100
player_speed = 5

# fish properties
fish_size = (40, 40)
fish_speed = 1
fish_descent = 10
fishes = []

# trash properties
trash_size = (40, 40)
trash_speed = 0.5
trash_descent = 5
multiple_trash = []

# hostile fish properties
hostile_fish_size = (40, 40)
hostile_fish_speed = 1.25
hostile_fish_descent = 10
hostile_fishes = []

# randomize the amount of fish that gets generated
fish_amount = random.randint(1,6)
trash_amount = random.randint(1,3)
hostile_fish_amount = random.randint(1,2)

# randomize fishable objects
fishable_objects = ['fish', 'hostile fish', 'trash']
fish_points = [100, -50, 0]  # points for fish, hostile fish, trash

# populate fish so that there are no more than 10 fish on the screen
for fish in range(fish_amount):
    fish_image = choose_fish_image()
for fish in range(fish_amount):
    fish_x = random.randint(0, screen_width - fish_size[0])
    fish_y = random.randint(25,200)
    fish_direction = random.choice([-1, 1])
    fish = [fish_x, fish_y, fish_direction]
    fishes.append(fish)

# populate trash so that there are no more than 3 trash on the screen
for trash in range(trash_amount):
    trash_image = choose_trash_image()
for trash in range(trash_amount):
    trash_x = random.randint(0, screen_width - trash_size[0])
    trash_y = random.randint(25,200)
    trash_direction = random.choice([-1, 1])
    trash = [trash_x, trash_y, trash_direction]
    multiple_trash.append(trash)
    
# populate hostile fish so that there are no more than 2 hostile fish on the screen
for hostile_fish in range(hostile_fish_amount):
    hostile_fish_image = choose_hostile_fish_image()
for hostile_fish in range(hostile_fish_amount):
    hostile_fish_x = random.randint(0, screen_width - hostile_fish_size[0])
    hostile_fish_y = random.randint(25,200)
    hostile_fish_direction = random.choice([-1, 1])
    hostile_fish = [hostile_fish_x, hostile_fish_y, hostile_fish_direction]
    hostile_fishes.append(hostile_fish)

# setup score
score = 0

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # set background
    window.blit(background_image, (0, 0))
    
    # draw fish
    for fish in fishes:
        fish[0] += fish_speed * fish[2]
        if fish[0] <= 0 or fish[0] >= screen_width - fish_size[0]:
            fish[2] *= -1  # flip direction
            fish[1] += fish_descent  # gradually move down
        window.blit(fish_image, (fish[0], fish[1]))
        
    # draw trash
    for trash in multiple_trash:
        trash[0] += trash_speed * trash[2]
        if trash[0] <= 0 or trash[0] >= screen_width - trash_size[0]:
            trash[2] *= -1
            trash[1] += trash_descent
        window.blit(trash_image, (trash[0], trash[1]))
        
    # draw hostile fish
    for hostile_fish in hostile_fishes:
        hostile_fish[0] += hostile_fish_speed * hostile_fish[2]
        if hostile_fish[0] <= 0 or hostile_fish[0] >= screen_width - hostile_fish_size[0]:
            hostile_fish[2] *= -1
            hostile_fish[1] += hostile_fish_descent
        window.blit(hostile_fish_image, (hostile_fish[0], hostile_fish[1]))

    # collision detection for fishing rod
    # if fishing rod collides with fish, remove fish from list and add change score based on fish type
    for fish in list(fishes):
        if player_x < fish[0] < player_x + 100 and player_y < fish[1] < player_y + 100:
            fishes.remove(fish)
            if fishable_objects[0] == 'fish':
                score += fish_points[0]
            elif fishable_objects[0] == 'hostile fish':
                score += fish_points[1]
            elif fishable_objects[0] == 'trash':
                score += fish_points[2]
        
    # update display
    pygame.display.flip()

# quit pygame
pygame.quit()