#!python3
# -*- coding: utf-8 -*-

"""
space_age.py on 25/07/2017
parameters: an age given in seconds
returns: depending on the planet, how old one would be on it
"""


class SpaceAge(object):
    EARTH = 31557600

    def __init__(self, age):
        self.seconds = age

    def on_earth(self):
        return round(self.seconds / self.EARTH, 2)

    def on_mercury(self):
        return round(self.seconds / (self.EARTH * 0.2408467), 2)

    def on_venus(self):
        return round(self.seconds / (self.EARTH * 0.61519726), 2)

    def on_mars(self):
        return round(self.seconds / (self.EARTH * 1.8808158), 2)

    def on_jupiter(self):
        return round(self.seconds / (self.EARTH * 11.862615), 2)

    def on_saturn(self):
        return round(self.seconds / (self.EARTH * 29.447498), 2)

    def on_uranus(self):
        return round(self.seconds / (self.EARTH * 84.016846), 2)

    def on_neptune(self):
        return round(self.seconds / (self.EARTH * 164.79132), 2)
