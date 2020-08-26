import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    # Initialize settings and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("D Shaws Alien Invasion Project")

    # Make the play button
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()