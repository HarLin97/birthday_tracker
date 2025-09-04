from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo
from ..const import DOMAIN


class BirthdayTracker:
    """Base class for all birthday-related sensors."""

    def __init__(self, entry: ConfigEntry, field: str, device_info: DeviceInfo):
        self._entry = entry
        self._field = field
        self._attr_should_poll = False
        self._attr_unique_id = f"{entry.entry_id}_{field}"
        self._attr_has_entity_name = True
        self._attr_translation_key = field
        self._attr_device_info = device_info
        
    async def async_added_to_hass(self):
        """Register entity for centralized refresh."""
        self.hass.data[DOMAIN].setdefault("entities", []).append(self)

    @property
    def available(self):
        return True
