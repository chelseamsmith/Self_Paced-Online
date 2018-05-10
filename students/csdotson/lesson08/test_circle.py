#!/usr/bin/env python
"""
Test file used to develop (TDD) and test 'circle.py'
"""

import circle as c
import sys, os
import math

def test_radius():
    circle = c.Circle(4)
    assert circle.radius == 4

def test_diameter():
    circle = c.Circle(4)
    assert circle.diameter == 8

def test_diameter_change():
    circle = c.Circle(4)
    circle.diameter = 3
    assert circle.diameter == 3

def test_radius_changes_diameter():
    circle = c.Circle(4)
    circle.radius = 5
    assert circle.diameter == 10

# def test_diameter_changes_radius():
#     circle = c.Circle(4)
#     print(os.path.abspath(sys.modules[c.Circle.__module__].__file__))
#     circle.diameter = 4
#     assert circle.radius == 2

def test_area():
    circle = c.Circle(2)
    assert circle.area == (math.pi * math.pow(circle.radius, 2))

def test_circle_creation_from_diameter():
    circle = c.Circle.from_diameter(8)
    assert circle.diameter == 8
    assert circle.radius == 4
