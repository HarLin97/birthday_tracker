from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.helpers.event import async_track_time_change
from datetime import datetime
from .const import DOMAIN
from .coordinator import BirthdayCoordinator

PLATFORMS = ["sensor"]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up from YAML (not used)."""
    return True  # 我们只支持 config flow，不处理 YAML 配置


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Birthday Tracker from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry

    # 初始化协调器（只初始化一次）
    if "coordinator" not in hass.data[DOMAIN]:
        coordinator = BirthdayCoordinator()
        hass.data[DOMAIN]["coordinator"] = coordinator

        # 注册每天凌晨 0 点刷新任务
        async def midnight_refresh(now):
            for entity in hass.data[DOMAIN].get("entities", []):
                coordinator.update_entry(entity._entry)
                entity.async_write_ha_state()

        async_track_time_change(hass, midnight_refresh, hour=0, minute=0, second=0)

    # 新 entry 添加时，只刷新当前 entry
    coordinator = hass.data[DOMAIN]["coordinator"]
    coordinator.update_entry(entry)

    # 转发实体平台
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok
