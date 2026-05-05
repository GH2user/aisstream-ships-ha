DOMAIN = "aisstream_ships"
AISSTREAM_WS = "wss://stream.aisstream.io/v0/stream"
VESSEL_TYPES = set(range(10, 99))

CONF_API_KEY = "api_key"
CONF_MAX_SHIPS = "max_ships"
CONF_MIN_LENGTH = "min_length_m"
CONF_BOUNDING_BOX = "bounding_box"

DEFAULT_MAX_SHIPS = 10
DEFAULT_MIN_LENGTH = 0
DEFAULT_BBOX = [[[53.25, -3.20], [53.50, -2.85]]]

STATUS_MAP = {
    0: "Underway", 1: "Anchored", 2: "Not Under Command", 3: "Restricted",
    4: "Constrained by Draught", 5: "Moored", 6: "Aground", 7: "Fishing",
    8: "Sailing", -1: "Unknown"
}

SIGNAL_UPDATE = f"{DOMAIN}_update"
