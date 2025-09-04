from homeassistant.components.sensor import SensorEntity
from ..const import DOMAIN, ATTR_SOLAR_BIRTH_DATE, ATTR_LUNAR_BIRTH_DATE
from .birthday_tracker import BirthdayTracker


class SolarBirthDateSensor(BirthdayTracker, SensorEntity):
    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_SOLAR_BIRTH_DATE, device_info)
        self._attr_state_class = None
        self._attr_device_class = None
        self._attr_icon = "mdi:calendar-star"

    @property
    def native_value(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        date_obj = data.get(ATTR_SOLAR_BIRTH_DATE)
        return date_obj.strftime("%Y-%m-%d") if date_obj else None


class LunarBirthDateSensor(BirthdayTracker, SensorEntity):
    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_LUNAR_BIRTH_DATE, device_info)
        self._attr_state_class = None
        self._attr_device_class = None
        self._attr_icon = "mdi:calendar-multiple"

    @property
    def native_value(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        lunar = data.get(ATTR_LUNAR_BIRTH_DATE)
        return lunar.toString() if lunar else None
