import sys
import pygame
from Settings import Settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from Alien import Alien
from button import Button 
from scoreboard import Scoreboard

def runGame():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create an instance to store game statistics
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the play button
    play_button = Button(ai_settings, screen, 'Play')

    #Make a ship, a group of bullets, and a group of aliens
    #Make a ship
    ship = Ship(ai_settings, screen)
    #Make a group to store bullets in
    bullets = Group()
    aliens = Group()

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


runGame()