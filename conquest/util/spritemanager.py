from util.constants import Constants

import pygame

class SpriteManager:
    """
    A class creating all the needed sprites for the game
    """

    '''tile sprites'''
    grassland_tile1 = pygame.transform.scale(pygame.image.load("sprites/tile_sprites/grassland_tile1.bmp"), (Constants.TILESIZE, Constants.TILESIZE))
    grassland_tile2 = pygame.transform.scale(pygame.image.load("sprites/tile_sprites/grassland_tile2.bmp"), (Constants.TILESIZE, Constants.TILESIZE))
    grassland_tile3 = pygame.transform.scale(pygame.image.load("sprites/tile_sprites/grassland_tile3.bmp"), (Constants.TILESIZE, Constants.TILESIZE))

    tileList =[
        grassland_tile1,
        grassland_tile2,
        grassland_tile3
    ]

    '''unit sprites'''
    # soldiers
    spearman_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/spearman.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))
    footman_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/footman.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))
    archer_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/archer.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))

    # buildings
    village_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/village.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))
    wall_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/wall.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))
    goldmine_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/goldmine.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))
    farm_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/farm.bmp"), (int(Constants.TILESIZE * Constants.UNITSCALESIZE), int(Constants.TILESIZE * Constants.UNITSCALESIZE)))