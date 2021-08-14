"""Config flow for Omnik Inverter integration."""
from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigEntry, ConfigFlow, OptionsFlow
from homeassistant.const import CONF_NAME, CONF_HOST
from homeassistant.data_entry_flow import FlowResult

from .const import (
    DOMAIN,
)

class OmnikInverterFlowHandler(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Omnik Inverter."""

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    )-> FlowResult:
        """Handle a flow initiated by the user."""
        if user_input is not None:
            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data={
                    CONF_HOST: user_input[CONF_HOST],
                },
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default="Solar"
                    ): str,
                    vol.Required(CONF_HOST): str,
                }
            )
        )