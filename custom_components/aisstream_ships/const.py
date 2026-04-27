DOMAIN = "aisstream_ships"
AISSTREAM_WS = "wss://stream.aisstream.io/v0/stream"
PASSENGER_TYPES = set(range(60, 70))

CONF_API_KEY = "api_key"
CONF_MAX_SHIPS = "max_ships"
CONF_MIN_LENGTH = "min_length_m"
CONF_BOUNDING_BOX = "bounding_box"

DEFAULT_MAX_SHIPS = 10
DEFAULT_MIN_LENGTH = 0
DEFAULT_BBOX = [[[53.25, -3.20], [53.50, -2.85]]]

STATUS_MAP = {
    0: "Underway", 1: "Anchored", 3: "Restricted",
    5: "Moored", 8: "Sailing", -1: "Unknown"
}

SIGNAL_UPDATE = f"{DOMAIN}_update"
