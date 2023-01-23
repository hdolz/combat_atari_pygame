import pygame
from modules.event_enum import *
from modules.player import *

class EventHandler():

    def __init__(self) -> None:
        pass

    def handleEvent(self, event, p1: Player, p2: Player):
        if event:
            if event == Event.MOVEP1:
                p1.forward = True
            if event == Event.MOVEP2:
                p2.forward = True
            if event == Event.STOPMOVEP1:
                p1.forward = False
            if event == Event.STOPMOVEP2:
                p2.forward = False
            if event == Event.ROTATELEFTP1:
                p1.rotate_left = True
            if event == Event.ROTATELEFTP2:
                p2.rotate_left = True
            if event == Event.ROTATERIGHTP1:
                p1.rotate_right = True
            if event == Event.ROTATERIGHTP2:
                p2.rotate_right = True
            if event == Event.STOPROTATEP1:
                p1.rotate_left = False
                p1.rotate_right = False
            if event == Event.STOPROTATEP2:
                p2.rotate_left = False
                p2.rotate_right = False
            if event == Event.SHOOTP1:
                p1.shoot()
            if event == Event.SHOOTP2:
                p2.shoot()

    def getEvent(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                #P1 controls
                if event.key == pygame.K_w:
                    return Event.MOVEP1
                if event.key == pygame.K_a:
                    return Event.ROTATELEFTP1
                if event.key == pygame.K_d:
                    return Event.ROTATERIGHTP1
                if event.key == pygame.K_LCTRL:
                    return Event.SHOOTP1
                #P2 controls
                if event.key == pygame.K_i:
                    return Event.MOVEP2
                if event.key == pygame.K_j:
                    return Event.ROTATELEFTP2
                if event.key == pygame.K_l:
                    return Event.ROTATERIGHTP2
                if event.key == pygame.K_SPACE:
                    return Event.SHOOTP2
            if event.type == pygame.KEYUP:
                #P1 controls
                if event.key == pygame.K_w:
                    return Event.STOPMOVEP1
                if event.key == pygame.K_a:
                    return Event.STOPROTATEP1
                if event.key == pygame.K_d:
                    return Event.STOPROTATEP1
                #P2 controls
                if event.key == pygame.K_i:
                    return Event.STOPMOVEP2
                if event.key == pygame.K_j:
                    return Event.STOPROTATEP2
                if event.key == pygame.K_l:
                    return Event.STOPROTATEP2