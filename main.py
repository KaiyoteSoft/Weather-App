import urllib2
import json
import pygame, sys
from pygame.locals import *
from choose_weather import Weather
import pprint
import time
import datetime

try:
    import android
except ImportError:
    android = None

pygame.init()

if android:
    android.init()
    android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

try:
    import pygame.mixer as mixer
except ImportError:
    import android.mixer as mixer

city = "palo alto, ca"



windowSurface = pygame.display.set_mode((1280, 770))

RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
LIGHT_BLUE = ((85, 190, 255))
LIGHT_GREEN = ((32, 255, 128))
PURPLE = ((236, 32, 255))
PINK = ((255, 32, 206))
WHITE = ((255, 255, 255))

weather_font = pygame.font.Font("fonts/animeace2_reg.ttf", 35)
weather_font_large = pygame.font.Font("fonts/animeace2_reg.ttf", 45)
wind_font = pygame.font.Font("fonts/animeace2_reg.ttf", 28)
title_font = pygame.font.Font("fonts/ASTONISH.TTF", 200)
sorry_font = pygame.font.Font("fonts/ASTONISH.TTF", 150)


palo_alto_pic = pygame.image.load("img/palo_alto.jpg")
rain_pic = pygame.image.load("img/rain.jpg")
sun_pic = pygame.image.load("img/sun.jpg")
lightning_pic = pygame.image.load("img/lightning.jpg")



pull = sys.argv

if len(pull) < 2:
    city = "palo alto"
else:
    city = (pull[1])

weather = Weather("Palo Alto, ca")
### checking for internet connection

if weather.connected == True:

    pa_button = True
    sc_button = True

    pa_1 = pygame.Rect(90, 120, 40, 40)
    pa_2 = pygame.Rect(90, 180, 40, 40)
    sc_rect = pygame.Rect(70, 450, 40, 40)
    pa_weather = pygame.draw.circle(windowSurface, RED, (150, 175), 100, 5)
    sc_weather = pygame.draw.circle(windowSurface, LIGHT_BLUE, (150, 475), 100, 5)
    menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)


    title_rect = pygame.Rect(580, 10, 600, 100)
    title_2_rect = pygame.Rect(640, 80, 600, 100)
    picture_rect = pygame.Rect(100, 475, 900, 400)
    menu_rect = pygame.Rect(1040, 575, 40, 40)
    sun_rect = pygame.Rect(400, 300, 300, 300)
    rain_rect = pygame.Rect(1000, 400, 300, 300)
    lightning_rect = pygame.Rect(550, 450, 300, 300)


    title = title_font.render("Weather", True, PURPLE)
    title_2 = title_font.render("App", True, LIGHT_BLUE)
    pa_1_text = weather_font.render("Palo", True, WHITE)
    pa_2_text = weather_font.render("Alto", True, WHITE)
    sc_text = wind_font.render("Capitola", True, LIGHT_GREEN)
    menu_text = weather_font.render("Home", True, LIGHT_BLUE)

else:
    print("Sorry, no internet connection. Try again later")
    ## rectangles for no-internet screen
    sorry_rect = pygame.Rect(20, 330, 1000, 1000)

    sorry_rect_2 = pygame.Rect(330, 450, 500, 500)
    sorry_text = sorry_font.render("Sorry, no internet connection.", True, LIGHT_BLUE)
    sorry_text_2 = sorry_font.render(" Try again later", True, RED)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        mouse_pos = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if pa_weather.collidepoint(mouse_pos):
                pa_button = False
                weather = Weather(city = "Palo Alto, ca")
                # pa_button_2 = False
            if sc_weather.collidepoint(mouse_pos):
                sc_button = False
                weather = Weather(city = "Capitola, ca")
            if menu.collidepoint(mouse_pos):
                pa_button = True
                sc_button = True
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


    if weather.connected == True:

        if pa_button == True:
            windowSurface.fill((0,0,0))
            pa_weather = pygame.draw.circle(windowSurface, RED, (150, 175), 100, 5)
            windowSurface.blit(pa_1_text, pa_1)
            windowSurface.blit(pa_2_text, pa_2)
            sc_weather = pygame.draw.circle(windowSurface, LIGHT_BLUE, (150, 475), 100, 5)
            windowSurface.blit(sc_text, sc_rect)
            windowSurface.blit(title, title_rect)
            windowSurface.blit(title_2, title_2_rect)
            windowSurface.blit(lightning_pic, lightning_rect)
            windowSurface.blit(sun_pic, sun_rect)
            windowSurface.blit(rain_pic, rain_rect)

        if pa_button == False:
            windowSurface.fill((0,0,0))
            # windowSurface.blit(choose_weather, description_rect)
            #weather.draw()
            # windowSurface.blit(sunrise_text, sunrise_rect)
            windowSurface.blit(weather.draw(), (0, 0))
            windowSurface.blit(palo_alto_pic, picture_rect)
            menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)
            windowSurface.blit(menu_text, menu_rect)

        if sc_button == False:
            windowSurface.fill((0,0,0))
            windowSurface.blit(weather.draw(), (0, 0))
            menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)
            windowSurface.blit(menu_text, menu_rect)





    if weather.connected == False:

        windowSurface.blit(sorry_text, sorry_rect)
        windowSurface.blit(sorry_text_2, sorry_rect_2)
    pygame.display.update()









