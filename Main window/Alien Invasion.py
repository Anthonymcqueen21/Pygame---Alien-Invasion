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
