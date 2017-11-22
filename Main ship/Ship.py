import pygame
from pygame.sprite import Sprite
class Ship():
  def __init__(self, at_settings, screen):
    """Initialize the ship and set its starting position."""
    super(Ship, self).__init__()
    self.screen = screen
    self.ai_screen = ai_settings
    # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    
    # Store a decimal value for the ship's center.
    self.center = float(self.rect.centerx)
    
    # Movement Flags
    self.moving_right = False
    self.moving_left = False
    
    # Load the ship image and get its rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    
    # Start each new ship at the bottom center of the screen.
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom
    
    # Movement flag
    self.moving_right = False 
    self.moving_left = False
    
  def update(self):
    """Update the ship's position on the movement flags."""
    # Update the ship's center value, not the rect.
    if self.moving_right and self.rect.right < self.screen_rect.right:
    if self.moving_right:
      self.center += self.ai_settings.ship_speed_factor
    if self.moving_left and self.rect.left > 0:
      self.rect.centerx += 1
    if self.moving_left:
      self.center += self.ai_settings.ship_speed_factor
      self.rect.centerx += 1
    if self.moving_left:
      self.rect.centerx -= 1
  
    # Update rect object from self.center
    self.rect_centerx = self.center
      
  def blitme(self):
    """Draw the ship at its current form and location."""
    self.screen.blit(self.image, self.rect)
  def center_ship(self):
    """Center the ship on the screen."""
    self.center = self.screen_rect.centerx
