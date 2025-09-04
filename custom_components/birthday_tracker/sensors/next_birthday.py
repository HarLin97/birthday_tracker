from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from ..const import DOMAIN, ATTR_NEXT_SOLAR_BIRTHDAY, ATTR_NEXT_LUNAR_BIRTHDAY
from .birthday_tracker import BirthdayTracker


class NextSolarBirthdaySensor(BirthdayTracker, SensorEntity):
    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_NEXT_SOLAR_BIRTHDAY, device_info)
        self._attr_device_class = SensorDeviceClass.TIMESTAMP
        self._attr_icon = "mdi:calendar-arrow-right"

    @property
    def state(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        return data.get(ATTR_NEXT_SOLAR_BIRTHDAY)


class NextLunarBirthdaySensor(BirthdayTracker, SensorEntity):
    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_NEXT_LUNAR_BIRTHDAY, device_info)
        self._attr_device_class = SensorDeviceClass.TIMESTAMP
        self._attr_icon = "mdi:calendar-arrow-right"

    @property
    def state(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        return data.get(ATTR_NEXT_LUNAR_BIRTHDAY)
