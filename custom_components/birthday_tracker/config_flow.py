from datetime import datetime
from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, CONF_NAME, CONF_BIRTH_DATE, CONF_ENABLE_LUNAR


class BirthdayTrackerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            try:
                datetime.strptime(user_input[CONF_BIRTH_DATE], "%Y-%m-%d")
            except ValueError:
                errors[CONF_BIRTH_DATE] = "invalid_date"

            if not errors:
                return self.async_create_entry(
                    title=user_input[CONF_NAME], data=user_input
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME): str,
                    vol.Required(CONF_BIRTH_DATE): str,
                    vol.Optional(CONF_ENABLE_LUNAR, default=True): bool,
                }
            ),
            errors=errors,
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        return BirthdayTrackerOptionsFlowHandler(config_entry)


class BirthdayTrackerOptionsFlowHandler(config_entries.OptionsFlow):

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        existing = self.config_entry.data
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default=existing.get(CONF_NAME, "")): str,
                    vol.Required(
                        CONF_BIRTH_DATE, default=existing.get(CONF_BIRTH_DATE, "")
                    ): str,
                    vol.Optional(
                        CONF_ENABLE_LUNAR, default=existing.get(CONF_ENABLE_LUNAR, True)
                    ): bool,
                }
            ),
        )
