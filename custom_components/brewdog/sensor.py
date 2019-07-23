"""
A platform which allows you to get information about a random BreDog beer.
For more details about this component, please refer to the documentation at
https://github.com/custom-components/brewdog
"""
# pylint: disable=unused-argument,missing-docstring
from datetime import timedelta
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from integrationhelper import WebClient, Logger
from integrationhelper.const import CC_STARTUP

URL = "https://api.punkapi.com/v2/beers/random"
ISSUE_LINK = "https://github.com/custom-components/brewdog/issues/"
SCAN_INTERVAL = timedelta(seconds=120)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    logger = Logger(__name__)
    logger.info(CC_STARTUP.format(name="BrewDog", issue_link=ISSUE_LINK))
    webclient = WebClient(async_get_clientsession(hass), logger)
    async_add_entities([BrewDogSensor(webclient)], True)


class BrewDogSensor(Entity):
    def __init__(self, webclient):
        self._state = None
        self._firstbrewerd = None
        self._description = None
        self._image = None
        self.webclient = webclient

    async def async_update(self):
        brewdog = await self.webclient.async_get_json(
            URL, {"Accept": "application/json"}
        )
        rbd = brewdog[0]
        self._state = rbd["tagline"]
        self._firstbrewerd = rbd["first_brewed"]
        self._description = rbd["description"]
        self._image = rbd["image_url"]

    @property
    def name(self):
        return "Random Brewdog"

    @property
    def entity_picture(self):
        return self._image

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return "mdi:beer"

    @property
    def device_state_attributes(self):
        return {"first brewed": self._firstbrewerd, "description": self._description}
