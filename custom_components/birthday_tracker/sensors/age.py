from homeassistant.components.sensor import SensorEntity, SensorStateClass
from ..const import ATTR_AGE, DOMAIN
from .birthday_tracker import BirthdayTracker


class AgeSensor(BirthdayTracker, SensorEntity):
    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_AGE, device_info)
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_icon = "mdi:cake-variant"

    @property
    def native_value(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        return data.get(ATTR_AGE)
