"""
A platform which allows you to get information about a random BreDog beer.
For more details about this component, please refer to the documentation at
https://gitlab.com/custom_components/brewdog
"""
from datetime import timedelta
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.aiohttp_client import async_get_clientsession

__version__ = '0.1.0'

REQUIREMENTS = ['brewdog==1.0.0']

ATTR_DESCRIPTION = 'description'
ATTR_FIRSTBREWED = 'first brewed'

SCAN_INTERVAL = timedelta(seconds=120)

ICON = 'mdi:beer'

async def async_setup_platform(
        hass, config, async_add_entities, discovery_info=None):
    from brewdog.api import API
    session = async_get_clientsession(hass)
    brewdog = API(hass.loop, session)
    async_add_entities([BrewDogSensor(brewdog)], True)

class BrewDogSensor(Entity):
    def __init__(self, api):
        from brewdog.const import ATTRIBUTION
        self._state = None
        self._attribution = ATTRIBUTION
        self._firstbrewerd = None
        self._description = None
        self._image = None
        self.api = api

    async def async_update(self):
        brewdog = await self.api.get_beer_random()
        rbd = brewdog[0]
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
            ATTR_DESCRIPTION: self._description,
            ATTR_ATTRIBUTION: self._attribution
        }
