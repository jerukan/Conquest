from enum import Enum

import pygame
from util.window import Window
from util.colors import Colors

class GameUnit:

    """
    base class for a generic unit
    buildings have 0 speed for reasons

    :parameter name (str): the name of the unit
    :parameter stats (int[]): a list of stats in the exact following order: [maxHealth, attack, speed, attacksPerTurn, range, cost]
    :parameter team (Team()): what team this unit is on
    :parameter position (int[y, x]): the position of the unit on the board, with a reversed axis
    :parameter sprite (Surface): the sprite of the unit, preferably pixel art
    """

    def __init__(self, name, stats, unittype, sprite, team=None, position=None):
        self.name = name

        self.maxHealth = stats[0]
        self.currentHealth = self.maxHealth
        self.attack = stats[1]
        self.speed = stats[2]
        self.currentSpeed = self.speed
        self.attacksPerTurn = stats[3]
        self.availableAttacks = self.attacksPerTurn
        self.range = stats[4]
        self.cost = stats[5]

        self.unittype = unittype

        self.sprite = sprite
        self.spriteRect = sprite.get_rect()

        self.team = team

        self.position = position




    def targetAction(self, targetunit):
        if targetunit.team.number != self.team.number and self.availableAttacks > 0:
            targetunit.takeDamage(self.attack)
            self.availableAttacks -= 1


    def onCreation(self):
        pass


    def onTurnStart(self):
        pass


    def onTurnEnd(self):
        pass


    def onDeath(self):
        pass

    """cool stuff"""
    def setHealth(self, health):
        self.currentHealth = health


    def healUnit(self, amount):
        self.currentHealth += amount
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth


    def takeDamage(self, damage):
        self.currentHealth -= damage


    def resetSpeed(self):
        self.currentSpeed = self.speed


    def resetAttack(self):
        self.availableAttacks = self.attacksPerTurn

    """display stuff"""
    def displayUnit(self, tileRect):
        self.spriteRect.center = tileRect.center

        highlightSurface = pygame.Surface((self.spriteRect.width, self.spriteRect.height))
        highlightSurface = highlightSurface.convert_alpha(Window.SURFACE)
        highlightSurface.fill(Colors.teamcolors[self.team.color])
        Window.SURFACE.blit(highlightSurface, self.spriteRect.topleft)

        Window.SURFACE.blit(self.sprite, self.spriteRect)
        Window().displayText("Health: " + str(self.currentHealth) + "/" + str(self.maxHealth), tileRect.x + 5, tileRect.y + 5, 20)
        if self.unittype == self.UnitType.SOLDIER:
            Window().displayText("Speed: " + str(self.currentSpeed) + "/" + str(self.speed), tileRect.bottomleft[0] + 5, tileRect.bottomleft[1] - 15, 20)


    class UnitType(Enum):

        SOLDIER = 1
        BUILDING = 2