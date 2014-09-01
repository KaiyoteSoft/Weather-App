import pygame, sys, time
import urllib2
import datetime
import json
import pprint
import random

class Weather():
    def __init__(self, city, font):
        import time
        self.city = city
        self.font = font
        self.internet_connection()
        self.spot = 147

        if self.font == "random":
            RED = ((255, 0, 0))
            GREEN = ((0, 255, 0))
            LIGHT_BLUE = ((85, 190, 255))
            LIGHT_GREEN = ((32, 255, 128))
            PURPLE = ((236, 32, 255))
            PINK = ((255, 32, 206))
            WHITE = ((255, 255, 255))
            normal_font = random.choice(["Gabrielle.ttf", "animeace2_reg.ttf", "SketchRockwell-Bold.ttf"])
            weather_font = pygame.font.Font("fonts/{}".format(normal_font), 35)
            weather_font_large = pygame.font.Font("fonts/{}".format(normal_font), 45)
            wind_font = pygame.font.Font("fonts/{}".format(normal_font), 28)



        if self.font == "normal":
            normal_font = ("animeace2_reg.ttf")
            weather_font = pygame.font.Font("fonts/{}".format(normal_font), 35)
            weather_font_large = pygame.font.Font("fonts/{}".format(normal_font), 45)
            wind_font = pygame.font.Font("fonts/{}".format(normal_font), 28)
            #title_font = pygame.font.Font("fonts/{}".format(normal_font), 200)

        self.middle_surf = pygame.image.load("img/middle_surf.png")
        self.small_surf = pygame.image.load("img/tahoe.jpg")
        self.large_surf = pygame.image.load("img/big_wave.jpg")

        RED = ((255, 0, 0))
        GREEN = ((0, 255, 0))
        LIGHT_BLUE = ((85, 190, 255))
        LIGHT_GREEN = ((32, 255, 128))
        PURPLE = ((236, 32, 255))
        PINK = ((255, 32, 206))
        WHITE = ((255, 255, 255))

        if self.connected == True:
            data = self.info.read()
            j_data = json.loads(data)

            surf_data = self.surf.read()
            j_surf_data = json.loads(surf_data)
            # print(j_surf_data)

            surf_data_2 = self.surf_2.read()
            j_surf_data_2 = json.loads(surf_data_2)

            tide_data = self.tide.read()
            j_tide_data = json.loads(tide_data)

#### loading statements for weather
            max_temp = (j_data["main"]["temp_max"])
            max_temp = int(max_temp)
            min_temp = (j_data["main"]["temp_min"])
            min_temp = int(min_temp)
            current_temp = (j_data["main"]["temp"])
            current_temp = int(current_temp)
            wind_speed = (j_data["wind"]["speed"])
            # gust = (j_data["wind"]["gust"])
            date = (j_data["dt"])
            current_time = time.ctime(date)
            print(time)
            s_time = int(j_data["sys"]["sunrise"])
            s_set_time = int(j_data["sys"]["sunset"])
            # sunrise_time = datetime.datetime.fromtimestamp(s_time).strftime('%H:%M:%S')
            sunrise_time = datetime.datetime.fromtimestamp(s_time).strftime('%H:%M')
            sunset_time = datetime.datetime.fromtimestamp(s_set_time).strftime('%H:%M')

            self.description = weather_font_large.render("Weather in " + j_data["name"], True, RED)
            " is"
            self.description_2 = wind_font.render(j_data["sys"]["country"], True, RED)
            self.weather = weather_font.render(j_data["weather"][0]["description"], True, GREEN)
            self.maximum_temp = weather_font.render("Maximum temperature today is {} degrees".format(max_temp), True, PURPLE)
            self.minimum_temp = weather_font.render("Minimum temperature will be {} degrees".format(min_temp), True, PURPLE)
            self.current_temperature = weather_font.render("Current temperature is {} degrees.".format(current_temp), True, LIGHT_BLUE)
            self.wind_description = wind_font.render("The wind is blowing at {} mph ".format(wind_speed), True, LIGHT_GREEN)
            self.day = weather_font.render("Date: {}".format(current_time), True, PINK)
            self.sunrise_text = weather_font.render("Sun rises at {} and sets at {}".format(sunrise_time, sunset_time), True, LIGHT_BLUE)

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

    ### loading statements for surf
            if self.city == ("Surf, ca"):
                wave_condition = (j_surf_data[0]["shape_detail"]["swell"])
                self.wave_height = (j_surf_data[6]["size_ft"])
                location = (j_surf_data[0]["spot_name"])

                self.height = wind_font.render("The location is {} and the waves are {} feet".format(location, ("%.2f" % self.wave_height)),
                                               True, RED)
                self.condition = weather_font.render("The surf is {}".format(wave_condition), True, WHITE)

            #### 2nd surf report
                wave_condition_2 = (j_surf_data_2[0]["shape_detail"]["swell"])
                wave_height_2 = (j_surf_data_2[6]["size_ft"])
                location_2 = (j_surf_data_2[0]["spot_name"])

                self.height_2 = wind_font.render("The location is {} and the waves are {} feet".format(location_2, ("%.2f" % wave_height_2)),
                                               True, GREEN)
                self.condition_2 = weather_font.render("The surf is {}".format(wave_condition_2), True, WHITE)

            ### tide
                self.morning_tide = (j_tide_data[5]["tide"])
                self.afternoon_tide = (j_tide_data[14]["tide"])
                self.evening_tide = (j_tide_data[18]["tide"])
                self.morning_tide_text = weather_font.render("The tide at 5 in the morning is {}".format
                                                             (("%.2f" % self.morning_tide)), True, LIGHT_BLUE)
                self.afternoon_tide_text = weather_font.render("The tide at 2 in the afternoon is {}".format
                                                               (("%.2f" % self.afternoon_tide)), True, LIGHT_BLUE)
                self.evening_tide_text = weather_font.render("The tide at 6 in the evening is {}".format
                                                             (("%.2f" % self.evening_tide)), True, LIGHT_BLUE)



            ### rectangles for surf
                self.height_rect = pygame.Rect(20, 20, 600, 100)
                self.condition_rect = pygame.Rect(500, 120, 600, 100)

                self.surf_height_rect_2 = pygame.Rect(10, 80, 600, 100)
                self.morning_tide_rect = pygame.Rect(200, 160, 600, 100)
                self.afternoon_tide_rect = pygame.Rect(200, 200, 600, 100)
                self.evening_tide_rect = pygame.Rect(200, 240, 600, 100)

                self.middle_surf_rect = pygame.Rect(300, 465, 350, 350)

                print(self.height)

###### IF THE FONT = RANDOM THEN U HAVE
            ###### TO REDRAW EVERYTHING..
### UNFORTUNATELY, IT IS NOT WORKING EVERY TIME???
        if self.font == "random":
            RED = ((255, 0, 0))
            GREEN = ((0, 255, 0))
            LIGHT_BLUE = ((85, 190, 255))
            LIGHT_GREEN = ((32, 255, 128))
            PURPLE = ((236, 32, 255))
            PINK = ((255, 32, 206))
            WHITE = ((255, 255, 255))
            normal_font = random.choice(["Gabrielle.ttf", "animeace2_reg.ttf", "SketchRockwell-Bold.ttf"])
            weather_font = pygame.font.Font("fonts/{}".format(normal_font), 35)
            weather_font_large = pygame.font.Font("fonts/{}".format(normal_font), 45)
            wind_font = pygame.font.Font("fonts/{}".format(normal_font), 28)
            title_font = pygame.font.Font("fonts/{}".format(normal_font), 200)
            print("Change font")

            self.description = weather_font_large.render("Weather in " + j_data["name"], True, RED)
            self.description_2 = wind_font.render(j_data["sys"]["country"], True, RED)
            self.weather = weather_font.render(j_data["weather"][0]["description"], True, GREEN)
            self.maximum_temp = weather_font.render("The maximum temperature today is {} degrees".format(max_temp), True, PURPLE)
            self.minimum_temp = weather_font.render("The minimum temperature will be {} degrees".format(min_temp), True, PURPLE)
            self.current_temperature = weather_font.render("The current temperature is {} degrees.".format(current_temp), True, LIGHT_BLUE)
            self.wind_description = wind_font.render("There is a wind blowing at {} mph ".format(wind_speed), True, LIGHT_GREEN)
            self.day = weather_font.render("The date is {}".format(current_time), True, PINK)
            self.sunrise_text = weather_font.render("The sun rises at {} and sets at {}".format(sunrise_time, sunset_time), True, LIGHT_BLUE)

            self.height_rect = pygame.Rect(20, 20, 600, 100)
            self.condition_rect = pygame.Rect(500, 120, 600, 100)

            self.surf_height_rect_2 = pygame.Rect(10, 80, 600, 100)
            self.morning_tide_rect = pygame.Rect(200, 160, 600, 100)
            self.afternoon_tide_rect = pygame.Rect(200, 200, 600, 100)
            self.evening_tide_rect = pygame.Rect(200, 240, 600, 100)

            self.middle_surf_rect = pygame.Rect(300, 465, 350, 350)

            # if self.city == ("Surf, ca"):
            wave_condition = (j_surf_data[0]["shape_detail"]["swell"])
            self.wave_height = (j_surf_data[6]["size_ft"])
            location = (j_surf_data[0]["spot_name"])

            self.height = wind_font.render("The location is {} and the waves are {} feet".format(location, ("%.2f" % self.wave_height)),
                                           True, RED)
            self.condition = weather_font.render("The surf is {}".format(wave_condition), True, WHITE)

        #### 2nd surf report
            wave_condition_2 = (j_surf_data_2[0]["shape_detail"]["swell"])
            wave_height_2 = (j_surf_data_2[6]["size_ft"])
            location_2 = (j_surf_data_2[0]["spot_name"])

            self.height_2 = wind_font.render("The location is {} and the waves are {} feet".format(location_2, ("%.2f" % wave_height_2)),
                                           True, GREEN)
            self.condition_2 = weather_font.render("The surf is {}".format(wave_condition_2), True, WHITE)

        ### tide
            self.morning_tide = (j_tide_data[5]["tide"])
            self.afternoon_tide = (j_tide_data[14]["tide"])
            self.evening_tide = (j_tide_data[18]["tide"])
            self.morning_tide_text = weather_font.render("The tide at 5 in the morning is {}".format
                                                         (("%.2f" % self.morning_tide)), True, LIGHT_BLUE)
            self.afternoon_tide_text = weather_font.render("The tide at 2 in the afternoon is {}".format
                                                           (("%.2f" % self.afternoon_tide)), True, LIGHT_BLUE)
            self.evening_tide_text = weather_font.render("The tide at 6 in the evening is {}".format
                                                         (("%.2f" % self.evening_tide)), True, LIGHT_BLUE)


            pygame.display.update()

    #def choose_weather(self, city):
    def draw(self):
        main_surface = pygame.Surface((1280, 770))
        main_surface.blit(self.description, self.description_rect)
        main_surface.blit(self.description_2, self.description2_rect)
        main_surface.blit(self.weather, self.weather_rect)
        main_surface.blit(self.maximum_temp, self.maximum_temp_rect)
        main_surface.blit(self.minimum_temp, self.min_temp_rect)
        main_surface.blit(self.current_temperature, self.current_temperature_rect)
        main_surface.blit(self.wind_description, self.wind_description_rect)
        main_surface.blit(self.day, self.day_rect)
        #main_surface.blit(self.palo_alto_pic, self.picture_rect)
        main_surface.blit(self.sunrise_text, self.sunrise_rect)

        if self.font == random:
            pygame.display.update()


        return(main_surface)

    def surf_draw(self):
        main_surface = pygame.Surface((1280, 770))
        main_surface.blit(self.height, self.height_rect)
        main_surface.blit(self.condition, self.condition_rect)
        main_surface.blit(self.height_2, self.surf_height_rect_2)

        main_surface.blit(self.morning_tide_text, self.morning_tide_rect)
        main_surface.blit(self.evening_tide_text, self.evening_tide_rect)
        main_surface.blit(self.afternoon_tide_text, self.afternoon_tide_rect)

        # if self.font == random:
        #     pygame.display.update()

        ### if statement for surf pictures
        if self.wave_height < 2:
            main_surface.blit(self.small_surf, self.middle_surf_rect)
        if self.wave_height > 2 and self.wave_height < 5:
            main_surface.blit(self.middle_surf, self.middle_surf_rect)
        if self.wave_height > 5:
            main_surface.blit(self.large_surf, self.middle_surf_rect)

        return(main_surface)


    def internet_connection(self):
        self.connected = True
        try:
            self.info = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial'.format(self.city))
            # self.surf = urllib2.urlopen('http://api.spitcast.com/api/spot/forecast/{}/'.format(self.spot))
            self.surf = urllib2.urlopen('http://api.spitcast.com/api/spot/forecast/147/')
            self.surf_2 = urllib2.urlopen('http://api.spitcast.com/api/spot/forecast/4/')
            self.tide = urllib2.urlopen('http://api.spitcast.com/api/county/tide/santa-cruz/')
        except IOError:
            self.connected = False
