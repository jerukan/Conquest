from util.constants import Constants

import pygame

class SpriteManager:
    """
    A class creating all the needed sprites for the game
    """

    '''tile sprites'''
    grassland_tile1 = pygame.transform.scale(pygame.image.load("sprites/tile_sprites/grassland_tile1.bmp"), (Constants.TILE_SIZE, Constants.TILE_SIZE))
    grassland_tile2 = pygame.transform.scale(pygame.image.load("sprites/tile_sprites/grassland_tile2.bmp"), (Constants.TILE_SIZE, Constants.TILE_SIZE))
    grassland_tile3 = pygame.transform.scale(pygame.image.load("sprites/tile_sprites/grassland_tile3.bmp"), (Constants.TILE_SIZE, Constants.TILE_SIZE))

    tileList =[
        grassland_tile1,
        grassland_tile2,
        grassland_tile3
    ]

    '''unit sprites'''
    # soldiers
    spearman_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/spearman.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    footman_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/footman.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    archer_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/archer.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))

    # buildings
    village_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/village.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    wall_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/wall.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    goldmine_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/goldmine.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    farm_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/farm.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    armory_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/armory.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))
    magetower_sprite = pygame.transform.scale(pygame.image.load("sprites/unit_sprites/magetower.bmp"), (int(Constants.TILE_SIZE * Constants.UNIT_SCALE), int(Constants.TILE_SIZE * Constants.UNIT_SCALE)))