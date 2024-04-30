import pygame
import random
import os

# start pygame
pygame.init()

dirname = os.path.dirname(__file__)

# screen dimensions
screen_width, screen_height = 1300, 576

# display 
window = pygame.display.set_mode((screen_width, screen_height))

#Getting the fishing rod color
WHITE = (255,255,255)

#Creating a rod class within fish.py to avoid import errors
class Rod:
    def __init__(self,image,x,y):
        self.image = image
        self.x = x
        self.y = y
        self.line_length = 0
        self.color = WHITE
        self.line_thickness = 4
        self.reel_speed = 5
        self.line_max_length = screen_height - 50
        self.casting = False

    def set_casting(self, bool_value):
        self.casting = bool_value

    def draw(self,screen):
        pygame.draw.line(screen, self.color, (self.x ,self.y), (self.x , self.y + self.line_length), self.line_thickness)
    
    def cast_line(self):
        if self.line_length < self.line_max_length:
            self.line_length += self.reel_speed
    
    def reel_in(self):
        if self.line_length > 0:
            self.line_length -=5
        else:
            self.set_casting(False)

# images
background_image_path = os.path.join(dirname, 'images/background.png')
background_image = pygame.image.load(background_image_path)

player_image_path = os.path.join(dirname, 'images/fisherman.png')
player_image = pygame.image.load(player_image_path)
player_image = pygame.transform.scale(player_image, (250,250))

rod_image_path = os.path.join(dirname, 'images/rod.png')
rod_image = pygame.image.load(rod_image_path)
rod_image = pygame.transform.scale(rod_image, (100,100))

hook_image_path = os.path.join(dirname, 'images/hook.png')
hook_image = pygame.image.load(hook_image_path)
hook_image = pygame.transform.scale(hook_image, (50,50))

#fish_image_paths
fish_image_paths = [
    os.path.join(dirname, 'images/fish_1.png'),
    os.path.join(dirname, 'images/fish_2.png'),
    os.path.join(dirname, 'images/fish_3.png'),
    os.path.join(dirname, 'images/fish_4.png')
]

#trash_image_paths
trash_image_paths = [
    os.path.join(dirname, 'images/boot.png'),
    os.path.join(dirname, 'images/boot.png'),
    os.path.join(dirname, 'images/boot.png')
]

#hostile_fish_paths
hostile_fish_image_paths = [
    os.path.join(dirname, 'images/hostile_fish_1.png'),
    os.path.join(dirname, 'images/hostile_fish_2.png'),
    os.path.join(dirname, 'images/hostile_fish_3.png'),
    os.path.join(dirname, 'images/hostile_fish_4.png')
]


# select each fish image randomly from available options
def choose_fish_image():
    fish_images = [
        pygame.image.load(fish_image_paths[0]),
        pygame.image.load(fish_image_paths[1]),
        pygame.image.load(fish_image_paths[2]),
        pygame.image.load(fish_image_paths[3])
    ]
    return random.choice(fish_images)

# select each trash image randomly from available options
def choose_trash_image():
    trash_images = [
        pygame.image.load(trash_image_paths[0]),
        pygame.image.load(trash_image_paths[1]),
        pygame.image.load(trash_image_paths[2])
    ]
    return random.choice(trash_images)

# select each hostile fish image randomly from available options
def choose_hostile_fish_image():
    hostile_fish_images = [
        pygame.image.load(hostile_fish_image_paths[0]),
        pygame.image.load(hostile_fish_image_paths[1]),
        pygame.image.load(hostile_fish_image_paths[2]),
        pygame.image.load(hostile_fish_image_paths[3])
    ]
    return random.choice(hostile_fish_images)

# player location and speed
player_x = screen_width // 2
player_y = screen_height - 700
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

fishing_rod = Rod(rod_image, player_x + 248, player_y + 125)

#Hook properties
hook_x = fishing_rod.x - 42
hook_y = fishing_rod.y - 7

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                fishing_rod.set_casting(True)
        
    # Get keys state
    keys = pygame.key.get_pressed()
    
    # Checking if the arrow keys are pressed down
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        fishing_rod.x += player_speed
        hook_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        fishing_rod.x -= player_speed
        hook_x -= player_speed
    if keys[pygame.K_SPACE] and fishing_rod.casting == False:
        fishing_rod.cast_line()
        hook_y += 5
    if keys[pygame.K_UP]:
        fishing_rod.reel_in()
        hook_y -= 5
            
    # set background
    window.blit(background_image, (0, 0))

    #Draw the rod
    window.blit(fishing_rod.image,(player_x + 165, player_y + 50))
    
    #draw the fisherman
    window.blit(player_image, (player_x,player_y))

    #draw the hook
    window.blit(hook_image, (hook_x, hook_y))

    #Draw the rod_line
    fishing_rod.draw(window)

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
        if hook_x - 50 < fish[0] < hook_x + 50 and hook_y - 5 < fish[1] < hook_y+5:
            fishes.remove(fish)
            if fishable_objects[0] == 'fish':
                score += fish_points[0]
            elif fishable_objects[0] == 'hostile fish':
                score += fish_points[1]
            elif fishable_objects[0] == 'trash':
                score += fish_points[2]
        
    #Detect horizontal bounds for the fisherman, hook, and rod
    if player_x < -150:
        player_x = -150
        hook_x = 205 - 150
        fishing_rod.x = 247 - 150
    if player_x > screen_width - 270:
        player_x = screen_width - 270
        fishing_rod.x = screen_width - 22
        hook_x = fishing_rod.x - 42
    
    #Detect vertical bounds for the hook
    if hook_y < fishing_rod.y - 7:
        hook_y = fishing_rod.y - 7
    if hook_y > fishing_rod.line_max_length:
        hook_y = fishing_rod.line_max_length

    
    # update display
    pygame.display.flip()

# quit pygame
pygame.quit()