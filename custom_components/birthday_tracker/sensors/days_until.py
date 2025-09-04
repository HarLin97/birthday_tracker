from homeassistant.components.sensor import SensorEntity, SensorStateClass
from ..const import DOMAIN, ATTR_DAYS_UNTIL_SOLAR, ATTR_DAYS_UNTIL_LUNAR
from .birthday_tracker import BirthdayTracker


class DaysUntilSolarSensor(BirthdayTracker, SensorEntity):
    """Sensor that displays days until next solar birthday."""

    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_DAYS_UNTIL_SOLAR, device_info)
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_device_class = None
        self._attr_icon = "mdi:calendar-clock"

    @property
    def native_value(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        return data.get(ATTR_DAYS_UNTIL_SOLAR)


class DaysUntilLunarSensor(BirthdayTracker, SensorEntity):
    def __init__(self, entry, device_info):
        super().__init__(entry, ATTR_DAYS_UNTIL_LUNAR, device_info)
        self._attr_state_class = SensorStateClass.MEASUREMENT
        self._attr_device_class = None
        self._attr_icon = "mdi:calendar-clock-outline"

    @property
    def native_value(self):
        data = self.hass.data[DOMAIN]["coordinator"].get(self._entry.entry_id)
        return data.get(ATTR_DAYS_UNTIL_LUNAR)
