import sys
from time import sleep
from pygame.sprite import Group
from bullet import bullet
from alien import Alien
import pygame

def check_high_score(stats, sb):
  """Check to see if there a new high score."""
  if stats.score > stats.high_score:
    stats_high_score = stats.score
    sb.prep_high_score()

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
  """Respond to ship being hit by alien."""
  if stats.ships_left > 0:
  # Decrement ships_left.
  stats.ships_left -= 1
  
  # Update scoreboard.
  sb.prep_ships()
  
  # Empty the list of aliens and bullets.
  aliens.empty()
  bullets.empty()
  
   #Create a new alien fleet and center the ship.
   create_fleet(ai_settings, screen, ship, aliens)
   ship.center_ship()
    # Pause.
   sleep(0.5)
else:
  stats.game_active = False
  pygame.mouse.set_set_visible(True)

def create_fleet(ai_settings, screen, aliens):
  """Create a full fleet of aliens."""
  #Create an alien and find the number of aliens in a row.
  #Spacing between each alien is equal to on alien width.
  alien = Alien(ai_settings, screen)
  number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
  alien_width = alien.rect.width
def get_number_aliens_x(ai_settings, alien_width):
  """Determine the number of aliens that fit in a row."""
  availible_space_x = ai_settings.screen_width - 2 * alien_width
  number_aliens_x = int(avalible_space_x / (2 * alien_width))
  return number_aliens_x
  
  #Create the first row of aliens.
  for aliens_number in range(number_aliens_x):
    create_alien(ai_settings, screen, aliens, alien_number)
    #Create an alien and place it in the rows.
def get_number_rows(ai_settings, ship_height, alien_height):
  """Determine the number of rows of aliens that fit on the screen."""
  availible_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
  number_rows = int(availible_space_y / (2 * alien_height))
  return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
  """Create an alien and place it in the row."""
  
alien = Alien(ai_settings, screen)
    alien_x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def check_events(ship):
def check_events(ai_settings, screen, ship, bullets):
  """Responds to keypress and mouse events."""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.key == pygame.K_q:
      sys.exit()
      
    elif event.key == pygame.K_SPACE:
def fire_bullet(ai_settings, screen, ship, bullets):
  """Fire a bullet if limit not reached yet."""
      # Create a new bullet and add it to the bullets group.
      if len(bullets) < ai_settings.bullets_allowed:
      new_bullet = Bullet(ai_settings, screen, ship)
      bullets.add(new_bullet)
      
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ai_settings, screen, ship, bullets)
      if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
      ship.moving_left = True
  
 elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)
      if event.key == pygame.K_RIGHT:
        ship_moving_right = False
    elif event.key == pygame.K_LEFT:
      ship.moving_left = False
        #Move the ship to the right.
        ship.rect.centerx += 1
  
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import ship
import game_functions as gf

def run_game():
  #Initialize game and create a screen object.
  pygame.init()
  # Create an instance to store game statistics and create a scoreboard
  ai_settings = Settings()
  screen = pygame.display.set.mode((ai_settings.screen_width, at_settings.screen_height))
  screen = pygame.display.set_mode((1200, 800))
  pygame.display.set_caption("Alien Invasion")
  
  # Make the play button.
  play_button = Button(ai_settings, screen, "Play")
  
  # Create an instance to store game statistics.
  stats = Gamestats(ai_settings)
  
  sb - Scoreboard(ai_settings, screen, stats)
  # Make a ship, a group of bullets, and a group of aliens.
  ship = Ship(ai_settings, screen)
  # Make a group to store bullets in.
  bullets = Group()
  aliens = Group()
  
  # Create the fleet of aliens.
  gf.create_fleet(ai_settings, screen, aliens)
  
  # Set the background color.
  bg_color = (230, 230, 230)
  
  #Start the main loop for the game.
  while True:
    gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
    
    if stats.game_active:
    ship.update()
    gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
    gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
    gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
    gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
    gf.update_aliens(ai_settings, ship, aliens)
    gf.update_bullets(aliens,bullets)
    gf.update_aliens(ai_settings, aliens)
    gf.update_screen(ai_screen, screen, ship)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button)
    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

def check_fleet_edges(ai_settings, aliens):
      """Respond appropriately if any aliens have reached an edge."""
      for alien in aliens.sprites():
        if alien.check_edges():
          change_fleet_direction(ai_settings, aliens)
          break
    def change_fleet_direction(ai_settings, aliens):
      """Drop the entire fleet and change the fleet's direction."""
      for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1
    
    def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
      """Check if the fleet is at an edge, and then update the postions of all aliens in the fleet."""
      check_fleet_edges(ai_settings, aliens)
      aliens.update()
    def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
      """Check if any aliens have reached the bottom of the screen."""
      screen_rect = screen.get_rect()
      for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
          # Treat this the same as if the ship got hit.
          ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
          break
    
    def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
      # Look for alien-ship collusions.
      if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
        print("Ship hit!!!")
        
# Look for aliens hitting the bottom of the screen.
      check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)
    
    def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
      """Update position of bullets and get rid of old bullets."""
    #Update bullet positions.
    #Check for any bullets that have to hit aliens.
    #If so, get rid of the bullet and the alien.
    
    def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
      """Respond to bullet and aliens that have collided."""
      # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
      for aliens in collision.values():
          stats.score += ai_settings.alien_points * len(aliens)
          sb.prep_score()
      check_high_score(stats, sb)
      
    
    if len(aliens) == 0:
      #Destroy existing bullets, speed up game, and create new fleet.
      #Destroy existing bullets and create new fleet.
      bullets.empty()
      ai_settings.increase_speed()
      create_fleet(ai_settings, screen, ship, aliens)
    bullets.update()
    
    # Get rid of bullets that have disappeared.
    
for bullet in bullets.copy():
      if bullet.rect.bottom <= 0:
        bullets.remove(bullet)
        
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    
    print(len(bullets))
    
    gf.update_screen(ai_settings, ship, screen, stats, play_button, bullets):
    
    #Watch for keyboard and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
        
    elif event.type == pygame.MOUSEBUTTONDOWN:
      mouse_x, mouse_y = pygame.mouse.get_pos()
      check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)
      
    def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
      """Start a new game when the Player clicks play."""
      button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
      if button_clicked and not stats.game_active:
        #Reset the game settings.
        ai_settings.initialize_dynamic_settings()
        #Hide the mouse curser.
        pygame.mouse.set_visible(False)
      if play_button.rect.collidepoint(mouse_x, mouse_y):
        # Reset the game statistics.
        stats.reset_stats()
        
 stats.game_active = True
        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        #Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
    def update_screen(ai_settings, screen, ship, aliens, bullets, play_button):
        
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    screen.fill(bg_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets:
      bullet.draw_bullet()
      ship.blitme()
      alien.blitme()
      aliens.draw(screen)
      
    # Draw the play button if the game is inactive.
    
if not stats.game_active:
      play_button.draw_button()
        
    # Make the most recently drawn screen visible.
    pygame.display.flip()
    
run_game()
