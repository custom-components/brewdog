"""
A platform which allows you to get information about a random BreDog beer.
For more details about this component, please refer to the documentation at
https://gitlab.com/custom_components/brewdog
"""
from datetime import timedelta

import requests

from homeassistant.helpers.entity import Entity

__version__ = '0.0.2'

ATTR_COMPONENT = 'component'
ATTR_COMPONENT_VERSION = 'component_version'
ATTR_DESCRIPTION = 'description'
ATTR_FIRSTBREWED = 'first brewed'

SCAN_INTERVAL = timedelta(seconds=120)

ICON = 'mdi:beer'

BASE_URL = 'https://api.punkapi.com/v2/beers/random'

def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([BrewDogSensor()])

class BrewDogSensor(Entity):
    def __init__(self):
        self._state = None
        self.update()

    def update(self):
        rbd = requests.get(BASE_URL, timeout=5).json()[0]
        self._state = rbd['tagline']
        self._firstbrewerd = rbd['first_brewed']
        self._description = rbd['description']
        self._image = rbd['image_url']

    @property
    def name(self):
        return 'Random Brewdog'

    @property
    def entity_picture(self):
        """Return preview of current game."""
        return self._image

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return ICON

    @property
    def friendly_name(self):
        return self._fiendlyname

    @property
    def device_state_attributes(self):
        return {
            ATTR_FIRSTBREWED: self._firstbrewerd,
            ATTR_DESCRIPTION: self._description
        }
