import pygame, sys, time
# The use of the main function is described in Chapter 9.
# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 140, 0)

def game_over(screen, clock, stage, player1, player2):
    done = False

    over_font = pygame.font.SysFont("Impact", 32, False, False)
    if player1.score >= 3:
        over_text = over_font.render("PLAYER 1 WINS", True, RED)
    if player2.score >= 3:
        over_text = over_font.render("PLAYER 2 WINS", True, RED)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(stage, [0, 0])
        screen.blit(over_text, [250, 100])
        pygame.display.flip()
        clock.tick(60)
        time.sleep(5)
        sys.exit()

def intro_screen(screen, clock):
    done = False

    intro_font = pygame.font.SysFont("Impact", 32, False, False)
    intro_sub_font = pygame.font.SysFont("Impact", 16)

    title_text = intro_font.render("Final Fight", True, RED)
    p1_controls = intro_sub_font.render("PLAYER 1: Movement: WASD. Punch: R. Kick: T", True, RED)
    p2_controls = intro_sub_font.render("PLAYER2: Movement: Arrow Keys. Punch: J. Kick: K", True, RED)
    start_game = intro_font.render("Press SPACE To Begin", True, RED)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    done = True
        screen.fill(BLACK)
        screen.blit(title_text, [275, 100])
        screen.blit(p1_controls, [200, 150])
        screen.blit(p2_controls, [200, 175])
        screen.blit(start_game, [210, 200])
        pygame.display.flip()
        clock.tick(60)

def player_round_win(screen, clock, stage, player1, player2):
    done = False

    round_font = pygame.font.SysFont("Impact", 32, False, False)
    if player1.win == True:
        round_text = round_font.render("PLAYER 1 WINS THE ROUND", True, RED)
    if player2.win == True:
        round_text = round_font.render("PLAYER 2 WINS THE ROUND", True, RED)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(stage, [0, 0])
        screen.blit(round_text, [190, 100])
        pygame.display.flip()
        clock.tick(60)
        time.sleep(5)
        #resets player 1
        player1.x_coords = 25
        player1.y_coords = 300
        player1.x_speed = 0 
        player1.y_speed = 0
        player1.kick = False
        player1.punch = False
        player1.win = False
        #resets player 2
        player2.x_coords = 550
        player2.y_coords = 300
        player2.x_speed = 0
        player2.y_speed = 0
        player2.kick = False
        player2.punch = False
        player2.win = False
        done = True

def player_bounds(player):
    if player.x_coords >= 575:
           player.x_coords = 575
    elif player.x_coords <= 0:
           player.x_coords = 0
    if player.y_coords >= 350:
           player.y_coords = 350
    elif player.y_coords <= 0:
           player.y_coords = 0

def player_speed_changes(player):
    player.x_coords += player.x_speed
    player.y_coords += player.y_speed


class player():
    def __init__(self):
        self.x_speed = 0
        self.y_speed = 0
        self.x_coords = 0
        self.y_coords = 0
        self.punch = False
        self.kick = False
        self.win = False
        self.score = 0
        self.win = False
    def player_hitbox(self):
        self.player_box = pygame.Rect(self.x_coords + 25, self.y_coords, 80, 100)


#TODO:intro screen, change window name, stop player overlap
def main():
   """ Main function for the game. """
   pygame.init()
   # Set the width and height of the screen [width,height]
   size = [700, 500]
   screen = pygame.display.set_mode(size)
   pygame.display.set_caption("Final Fight")
   # Loop until the user clicks the close button.
   done = False
   # Used to manage how fast the screen updates
   clock = pygame.time.Clock()
   #run intro screen first
   intro_screen(screen, clock)
   #setting player vars
   player1 = player()
   player1.x_coords = 25
   player1.y_coords = 300
   player2 = player()
   player2.x_coords = 550
   player2.y_coords = 300
   #loading images
   stage = pygame.image.load("dudstage.jpg")
   stage = pygame.transform.scale(stage, [700, 500])
   #player 1 neutral image and current variable
   player1_n_sprite = pygame.image.load("ken.png").convert_alpha()
   player1_n_sprite = pygame.transform.scale(player1_n_sprite,[125, 150])
   player1_current = player1_n_sprite
   #player 1 attack images
   #player 1 punch
   player1_punch_sprite = pygame.image.load("kenpunch.png").convert_alpha()
   player1_punch_sprite = pygame.transform.scale(player1_punch_sprite,[125, 150])
   #player 1 kick
   player1_kick_sprite = pygame.image.load("kenkick.png").convert_alpha()
   player1_kick_sprite = pygame.transform.scale(player1_kick_sprite, [125, 150])
   #player 2
   player2_n_sprite = pygame.image.load("ryu.png").convert_alpha()
   player2_n_sprite = pygame.transform.scale(player2_n_sprite, [125, 150])
   player2_current = player2_n_sprite
   #player 2 attack images
   #player 2 punch
   player2_punch_sprite = pygame.image.load("ryupunch.png").convert_alpha()
   player2_punch_sprite = pygame.transform.scale(player2_punch_sprite, [135, 160])
   #player 2 kick 
   player2_kick_sprite = pygame.image.load("ryukick.png").convert_alpha()
   player2_kick_sprite = pygame.transform.scale(player2_kick_sprite, [135, 160])
   #score font
   score_font = pygame.font.SysFont("Impact", 64, False,  False)
   player1_score_text = "" 
   player2_score_text = ""
   # -------- Main Program Loop -----------
   while not done:
       # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               done = True
           elif event.type == pygame.KEYDOWN:
               #player1 movement keys
               if event.key == pygame.K_w:
                   player1.y_speed = -3
               elif event.key == pygame.K_s:
                   player1.y_speed = 3
               elif event.key == pygame.K_a:
                   player1.x_speed = -3
               elif event.key == pygame.K_d:
                   player1.x_speed = 3
               #player1 attack keys
               elif event.key == pygame.K_r:
                   player1.punch = True
                   player1_current = player1_punch_sprite
               elif event.key == pygame.K_t:
                   player1.kick = True
                   player1_current = player1_kick_sprite
               #player2 movement keys
               elif event.key == pygame.K_UP:
                   player2.y_speed = -3
               elif event.key == pygame.K_DOWN:
                   player2.y_speed =3
               elif event.key == pygame.K_LEFT:
                   player2.x_speed = -3
               elif event.key == pygame.K_RIGHT:
                   player2.x_speed = 3
               #player2 attack keys
               elif event.key == pygame.K_k:
                   player2.punch = True
                   player2_current = player2_punch_sprite
               elif event.key == pygame.K_j:
                   player2.kick = True
                   player2_current = player2_kick_sprite
           #removing speed on key release
           elif event.type == pygame.KEYUP:
               #player1
               if event.key == pygame.K_w or event.key == pygame.K_s:
                   player1.y_speed = 0
               elif event.key == pygame.K_a or event.key == pygame.K_d:
                   player1.x_speed = 0
               #stopping player1 attacks
               elif event.key == pygame.K_r:
                   player1.punch = False
                   player1_current = player1_n_sprite
               elif event.key == pygame.K_t:
                   player1.kick = False
                   player1_current = player1_n_sprite
               #player2
               elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                   player2.y_speed = 0
               elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                   player2.x_speed = 0
               #stopping player2 attacks
               elif event.key == pygame.K_k:
                   player2.punch = False
                   player2_current = player2_n_sprite
               elif event.key == pygame.K_j:
                   player2.kick = False
                   player2_current = player2_n_sprite
           player1_score_text = str(player1.score)
           player2_score_text = str(player2.score)
       # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
       # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
       #affecting coords by speeds
       player_speed_changes(player1)
       player_speed_changes(player2)
       #setting player1 bounds
       player_bounds(player1)
       #setting player2 bounds
       player_bounds(player2)
       # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
       # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
       # First, clear the screen to white. Don't put other drawing commands
       # above this, or they will be erased with this command.
       screen.fill(WHITE)
       #display stage
       screen.blit(stage, [0,0])
       #display player1 image
       screen.blit(player1_current, [player1.x_coords, player1.y_coords])
       #display player2 image
       screen.blit(player2_current, [player2.x_coords, player2.y_coords])
       #display scores
       p1_score_counter = score_font.render(player1_score_text, True, RED)
       p2_score_counter = score_font.render(player2_score_text, True, RED)
       screen.blit(p1_score_counter, [200, 0])
       screen.blit(p2_score_counter, [500, 0])
       #drawing hitboxes
       player1.player_hitbox()
       player2.player_hitbox()
       #player1 attack hitbox checks
       if player1.punch == True:
           p1_punch_box = pygame.Rect(player1.x_coords + 12, player1.y_coords + 10, 100, 25)
           if p1_punch_box.colliderect(player2.player_box):
               player1.score += 1
               print(player1.score)
               player1.win = True
               player_round_win(screen, clock, stage, player1, player2)
       if player1.kick == True:
           p1_kick_box = pygame.Rect(player1.x_coords + 12, player1.y_coords + 55, 100, 25)
           if p1_kick_box.colliderect(player2.player_box):
               player1.score += 1
               print(player1.score)
               player1.win = True
               player_round_win(screen, clock, stage, player1, player2)
       #player2 attack hitbox checks
       if player2.punch == True:
          p2_punch_box = pygame.Rect(player2.x_coords - 12, player2.y_coords + 28, 100, 25)
          if p2_punch_box.colliderect(player1.player_box):
             player2.score += 1
             print(player2.score)
             player2.win = True
             player_round_win(screen, clock, stage, player1, player2)
       if player2.kick == True:
           p2_kick_box = pygame.Rect(player2.x_coords - 12, player2.y_coords + 59, 100, 25)
           if p2_kick_box.colliderect(player1.player_box):
               player2.score += 1
               print(player2.score)
               player2.win = True
               player_round_win(screen, clock, stage, player1, player2)
        #if someone wins 3 rounds
       if player1.score >= 3 or player2.score >=3:
           game_over(screen, clock, stage, player1, player2)
           done = True
       # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
       # Go ahead and update the screen with what we've drawn.
       pygame.display.flip()
       # Limit to 60 frames per second
       clock.tick(60)
   # Close the window and quit.
   # If you forget this line, the program will 'hang'
   # on exit if running from IDLE.
   pygame.quit()
if __name__ == "__main__":
   main()
