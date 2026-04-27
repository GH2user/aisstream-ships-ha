import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import (
    DOMAIN, CONF_API_KEY, CONF_MAX_SHIPS, CONF_MIN_LENGTH,
    DEFAULT_MAX_SHIPS, DEFAULT_MIN_LENGTH
)


class AisstreamShipsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Aisstream Ships", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_API_KEY): str,
                vol.Optional(CONF_MAX_SHIPS, default=DEFAULT_MAX_SHIPS):
                    vol.All(int, vol.Range(min=2, max=10)),
                vol.Optional(CONF_MIN_LENGTH, default=DEFAULT_MIN_LENGTH):
                    vol.All(int, vol.Range(min=0, max=500)),
            })
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return AisstreamShipsOptionsFlow(config_entry)


class AisstreamShipsOptionsFlow(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self._config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema({
                vol.Optional(CONF_MAX_SHIPS,
                    default=self._config_entry.data.get(CONF_MAX_SHIPS, DEFAULT_MAX_SHIPS)):
                    vol.All(int, vol.Range(min=2, max=10)),
                vol.Optional(CONF_MIN_LENGTH,
                    default=self._config_entry.data.get(CONF_MIN_LENGTH, DEFAULT_MIN_LENGTH)):
                    vol.All(int, vol.Range(min=0, max=500)),
            })
        )
