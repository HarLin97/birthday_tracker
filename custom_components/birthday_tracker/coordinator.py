from datetime import date
from homeassistant.config_entries import ConfigEntry
from .helpers import (
    parse_birth_date,
    calculate_age,
    get_next_solar_birthday,
    get_next_lunar_birthday,
    get_days_until,
    get_lunar_birth_date,
    is_today_birthday,
)
from .const import (
    CONF_NAME,
    CONF_BIRTH_DATE,
    CONF_ENABLE_LUNAR,
    ATTR_AGE,
    ATTR_NEXT_SOLAR_BIRTHDAY,
    ATTR_NEXT_LUNAR_BIRTHDAY,
    ATTR_DAYS_UNTIL_SOLAR,
    ATTR_DAYS_UNTIL_LUNAR,
    ATTR_IS_TODAY_SOLAR_BIRTHDAY,
    ATTR_IS_TODAY_LUNAR_BIRTHDAY,
    ATTR_SOLAR_BIRTH_DATE,
    ATTR_LUNAR_BIRTH_DATE,
)


class BirthdayCoordinator:
    """Centralized birthday data manager."""

    def __init__(self):
        self._data: dict[str, dict] = {}

    def update_entry(self, entry: ConfigEntry):
        """Recalculate birthday data for a single entry."""
        today = date.today()
        name = entry.data[CONF_NAME]
        birth_date = parse_birth_date(entry.data[CONF_BIRTH_DATE])
        enable_lunar = entry.data.get(CONF_ENABLE_LUNAR, True)

        self._data[entry.entry_id] = self._calculate_all_fields(
            name, birth_date, today, enable_lunar
        )

    def get(self, entry_id: str) -> dict | None:
        """Get computed birthday data for a specific entry."""
        return self._data.get(entry_id)

    def _calculate_all_fields(
        self, name: str, birth_date: date, today: date, enable_lunar: bool
    ) -> dict:
        """Compute all birthday-related fields."""
        next_solar = get_next_solar_birthday(birth_date, today)

        result = {
            CONF_NAME: name,
            ATTR_SOLAR_BIRTH_DATE: birth_date,
            ATTR_NEXT_SOLAR_BIRTHDAY: next_solar,
            ATTR_DAYS_UNTIL_SOLAR: get_days_until(next_solar, today),
            ATTR_AGE: calculate_age(birth_date, today),
            ATTR_IS_TODAY_SOLAR_BIRTHDAY: is_today_birthday(birth_date, today),
        }

        if enable_lunar:
            lunar_birth = get_lunar_birth_date(birth_date)
            next_lunar = get_next_lunar_birthday(lunar_birth, today)
            result.update(
                {
                    ATTR_LUNAR_BIRTH_DATE: lunar_birth,
                    ATTR_NEXT_LUNAR_BIRTHDAY: next_lunar,
                    ATTR_DAYS_UNTIL_LUNAR: get_days_until(next_lunar, today),
                    ATTR_IS_TODAY_LUNAR_BIRTHDAY: is_today_birthday(next_lunar, today),
                }
            )

        return result
