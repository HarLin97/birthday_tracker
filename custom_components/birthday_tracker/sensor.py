from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from .const import CONF_NAME, CONF_ENABLE_LUNAR, DOMAIN
from .sensors import (
    AgeSensor,
    DaysUntilSolarSensor,
    DaysUntilLunarSensor,
    SolarBirthDateSensor,
    LunarBirthDateSensor,
    NextSolarBirthdaySensor,
    NextLunarBirthdaySensor,
    IsTodaySolarSensor,
    IsTodayLunarSensor,
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up all birthday sensors for a single config entry."""
    name = entry.data[CONF_NAME]
    enable_lunar = entry.data.get(CONF_ENABLE_LUNAR, True)

    device_info = DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=name,
        manufacturer="VergilGao",
        model="Birthday Tracker",
    )

    sensors = [
        AgeSensor(entry, device_info),
        DaysUntilSolarSensor(entry, device_info),
        SolarBirthDateSensor(entry, device_info),
        NextSolarBirthdaySensor(entry, device_info),
        IsTodaySolarSensor(entry, device_info),
    ]

    if enable_lunar:
        sensors.extend(
            [
                DaysUntilLunarSensor(entry, device_info),
                LunarBirthDateSensor(entry, device_info),
                NextLunarBirthdaySensor(entry, device_info),
                IsTodayLunarSensor(entry, device_info),
            ]
        )

    async_add_entities(sensors, update_before_add=True)
