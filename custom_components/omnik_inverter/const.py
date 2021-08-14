"""Constants for Omnik Inverter integration."""
from __future__ import annotations

from typing import Final

from homeassistant.components.sensor import (
    STATE_CLASS_MEASUREMENT,
    SensorEntityDescription,
)
from homeassistant.const import (
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_ENERGY,
    ENERGY_KILO_WATT_HOUR,
    POWER_WATT,
)
from homeassistant.util import dt

VERSION = '1.5.4'

CONF_CACHE_POWER_TODAY = 'cache_power_today'
CONF_USE_JSON = 'use_json'

JS_URL = 'http://{0}/js/status.js'
JSON_URL = 'http://{0}/status.json?CMD=inv_query&rand={1}'
CACHE_NAME = '.{0}{1}.json'
CACHE_VALUE_KEY = "cache_value"
CACHE_DAY_KEY = "cache_day"

SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]] = (
    SensorEntityDescription(
        key="powercurrent",
        icon="mdi:weather-sunny",
        name="Power Current",
        device_class=DEVICE_CLASS_POWER,
        native_unit_of_measurement=POWER_WATT,
        state_class=STATE_CLASS_MEASUREMENT,
    ),
    SensorEntityDescription(
        key="powertoday",
        icon="mdi:flash",
        name="Energy Today",
        device_class=DEVICE_CLASS_ENERGY,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        last_reset=dt.utc_from_timestamp(0),
    ),
    SensorEntityDescription(
        key="powertotal",
        icon="mdi:chart-line",
        name="Energy Total",
        device_class=DEVICE_CLASS_ENERGY,
        native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
        last_reset=dt.utc_from_timestamp(0),
    ),
)