import urllib2
import json
import pygame, sys
from pygame.locals import *
# from choose_weather import *
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
class Weather():
    def __init__(self, city):
        import time
        self.city = city
        info = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial'.format(self.city))
        data = info.read()
        j_data = json.loads(data)
        max_temp = (j_data["main"]["temp_max"])
        min_temp = (j_data["main"]["temp_min"])
        current_temp = (j_data["main"]["temp"])
        wind_speed = (j_data["wind"]["speed"])
        # gust = (j_data["wind"]["gust"])
        date = (j_data["dt"])
        current_time = time.ctime(date)
        print(time)
        s_time = int(j_data["sys"]["sunrise"])
        s_set_time = int(j_data["sys"]["sunset"])
        sunrise_time = datetime.datetime.fromtimestamp(s_time).strftime('%H:%M:%S')
        sunset_time = datetime.datetime.fromtimestamp(s_set_time).strftime('%H:%M:%S')

        self.description = weather_font_large.render("The name of the city is " + j_data["name"], True, RED)
        self.description_2 = wind_font.render("It is located in the country of " + j_data["sys"]["country"], True, RED)
        self.weather = weather_font.render(j_data["weather"][0]["description"], True, GREEN)
        self.maximum_temp = weather_font.render("The maximum temperature today is {} degrees".format(max_temp), True, PURPLE)
        self.minimum_temp = weather_font.render("The minimum temperature will be {} degrees".format(min_temp), True, PURPLE)
        self.current_temperature = weather_font.render("The current temperature is {} degrees.".format(current_temp), True, LIGHT_BLUE)
        self.wind_description = wind_font.render("There is a wind blowing at {} mph ".format(wind_speed), True, LIGHT_GREEN)
        self.day = weather_font.render("The date is {}".format(current_time), True, PINK)
        self.sunrise_text = weather_font.render("The sun rises at {} and sets at {}".format(sunrise_time, sunset_time), True, LIGHT_BLUE)

        self.description_rect = pygame.Rect(120, 10, 600, 100)
        self.description2_rect = pygame.Rect(60, 60, 60, 100)
        self.weather_rect = pygame.Rect(300, 110, 600, 100)
        self.maximum_temp_rect = pygame.Rect(30, 160, 600, 100)
        self.min_temp_rect = pygame.Rect(30, 210, 600, 100)
        self.current_temperature_rect = pygame.Rect(60, 260, 600, 100)
        self.wind_description_rect = pygame.Rect(2, 310, 600, 100)
        self.day_rect = pygame.Rect(35, 360, 600, 100)
        self.menu_rect = pygame.Rect(1040, 575, 40, 40)
        self.sunrise_rect = pygame.Rect(50, 410, 600, 100)

    #def choose_weather(self, city):
    def draw(self):
         windowSurface.blit(self.description, self.description_rect)
         windowSurface.blit(self.description_2, self.description2_rect)
         windowSurface.blit(self.weather, self.weather_rect)
         windowSurface.blit(self.maximum_temp, self.maximum_temp_rect)
         windowSurface.blit(self.minimum_temp, self.min_temp_rect)
         windowSurface.blit(self.current_temperature, self.current_temperature_rect)
         windowSurface.blit(self.wind_description, self.wind_description_rect)
         windowSurface.blit(self.day, self.day_rect)
         #windowSurface.blit(self.palo_alto_pic, self.picture_rect)
         windowSurface.blit(self.sunrise_text, self.sunrise_rect)



windowSurface = pygame.display.set_mode((1280, 770))

RED = ((255, 0, 0))
GREEN = ((0, 255, 0))
LIGHT_BLUE = ((85, 190, 255))
LIGHT_GREEN = ((32, 255, 128))
PURPLE = ((236, 32, 255))
PINK = ((255, 32, 206))
WHITE = ((255, 255, 255))

sorry_font = pygame.font.Font("fonts/ASTONISH.TTF", 150)

palo_alto_pic = pygame.image.load("img/palo_alto.jpg")
rain_pic = pygame.image.load("img/rain.jpg")
sun_pic = pygame.image.load("img/sun.jpg")
lightning_pic = pygame.image.load("img/lightning.jpg")
weather_font = pygame.font.Font("fonts/animeace2_reg.ttf", 35)
weather_font_large = pygame.font.Font("fonts/animeace2_reg.ttf", 45)
wind_font = pygame.font.Font("fonts/animeace2_reg.ttf", 28)
title_font = pygame.font.Font("fonts/ASTONISH.TTF", 200)


pull = sys.argv

if len(pull) < 2:
    city = "palo alto"
else:
    city = (pull[1])

weather = Weather("Palo Alto, ca")
### checking for internet connection
try:

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
            weather.draw()
            windowSurface.blit(palo_alto_pic, picture_rect)
            # windowSurface.blit(sunrise_text, sunrise_rect)

            menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)
            windowSurface.blit(menu_text, menu_rect)

        if sc_button == False:
            windowSurface.fill((0,0,0))
            menu = pygame.draw.circle(windowSurface, WHITE, (1100, 600), 100, 5)
            weather.draw()
            windowSurface.blit(menu_text, menu_rect)




        pygame.display.update()
except IOError:
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
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        windowSurface.blit(sorry_text, sorry_rect)
        windowSurface.blit(sorry_text_2, sorry_rect_2)
        pygame.display.update()










