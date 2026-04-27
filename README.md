# Aisstream Ships — Custom Home Assistant Integration

A custom HACS integration for Home Assistant that tracks passenger vessels in real time via the [AISstream.io](https://aisstream.io) WebSocket API. Originally built to monitor ships on the River Mersey / Liverpool Bay area, it works with any configurable bounding box worldwide.

---

## Features

- **Live ship tracking** via AISstream.io WebSocket (`cloud_push` — no polling)
- Filters for **passenger vessels** (AIS ship types 60–69) including ferries and cruise ships
- Configurable **bounding box**, maximum number of ships, and minimum vessel length
- Creates HA sensor entities for ship count, header summary, individual ship slots, and formatted display lines
- Exposes rich **state attributes** per ship: destination, speed, status, length, MMSI, lat/lon, and last seen timestamp
- Auto-reconnects on connection loss with a 30-second backoff

---

## Installation via HACS

1. In Home Assistant, go to **HACS → Integrations → ⋮ → Custom repositories**
2. Add `https://github.com/peterstnsz/aisstream-ships-ha` as an **Integration**
3. Search for **Aisstream Ships** and install
4. Restart Home Assistant
5. Go to **Settings → Devices & Services → Add Integration** and search for **Aisstream Ships**

---

## Configuration

During setup you will be prompted for:

| Field                   | Description                                                    | Default |
| ----------------------- | -------------------------------------------------------------- | ------- |
| **AISstream API Key**   | Free key from [aisstream.io](https://aisstream.io)             | —       |
| **Max ships to track**  | Number of ship sensor slots created (2–10)                     | 10      |
| **Min ship length (m)** | Filter out small vessels. `0` = all, `150` = cruise ships only | 0       |

Settings can be updated later via **Settings → Devices & Services → Aisstream Ships → Configure**.

### Bounding Box

The default bounding box covers the **Liverpool / River Mersey** area:

```python
DEFAULT_BBOX = [[[53.25, -3.20], [53.50, -2.85]]]
```

To track a different area, modify `DEFAULT_BBOX` in `const.py` or pass a custom value via `CONF_BOUNDING_BOX` in your config entry data.

---

## Entities Created

For a configuration with `max_ships = 5`, the following sensors are created:

| Entity ID                             | Name                    | Description                                             |
| ------------------------------------- | ----------------------- | ------------------------------------------------------- |
| `sensor.aisstream_ship_count`         | Aisstream Ship Count    | Number of matching ships currently visible              |
| `sensor.aisstream_ships_header`       | Aisstream Ships Header  | Summary string, e.g. `Ships in area: 3`                 |
| `sensor.aisstream_ship_1` … `_5`      | Aisstream Ship 1–5      | Ship name for each slot                                 |
| `sensor.aisstream_ship_line_1` … `_5` | Aisstream Ship Line 1–5 | Formatted one-liner: `SHIP NAME (Underway > LIVERPOOL)` |

### State Attributes (per ship slot)

```yaml
destination: LIVERPOOL
status: 0
speed_knots: 12.4
length_m: 171
mmsi: 235123456
lat: 53.401
lon: -3.012
last_seen: '2026-04-27T09:15:00+00:00'
```

---

## Example Lovelace Card

```yaml
type: entities
title: Ships in Area
entities:
  - entity: sensor.aisstream_ship_count
  - entity: sensor.aisstream_ship_line_1
  - entity: sensor.aisstream_ship_line_2
  - entity: sensor.aisstream_ship_line_3
```

---

## Requirements

- Home Assistant 2023.6 or later
- `websockets >= 10.0` (installed automatically by HACS)
- A free API key from [aisstream.io](https://aisstream.io)

---

## Project Structure

```
custom components/
└── aisstream-ships/
    ├── __init__.py        # Integration setup & teardown
    ├── config_flow.py     # UI config & options flow
    ├── const.py           # Constants, defaults, bounding box
    ├── coordinator.py     # WebSocket connection & ship data management
    ├── manifest.json      # HACS/HA integration manifest
    ├── sensor.py          # Sensor entity definitions
    └── translations/
        └── en.json        # UI string translations
hacs.json                  # HACS repository metadata
```

---

## Licence

MIT — see [LICENSE](LICENSE) if present, otherwise feel free to use and adapt.
