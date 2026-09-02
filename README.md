# pd

A collection of Pure Data patches and companion Python/Node scripts used for
live installation and event control: DMX lighting over a USB DMX interface,
OSC control of a Behringer X-Air digital mixer, MIDI fader automation
recording/playback, and a small browser/Pure Data bridge.

These are working tools built for specific shows and installations, not a
packaged product — expect hard-coded serial ports, device IDs and file paths
that need editing per venue/setup.

**Status: working / actively used, unpolished.** No installer, no tests;
each subfolder is a self-contained patch or script set you point at your own
hardware.

---

## Contents

### `dmx/` — DMX512 lighting control over serial

Python scripts that speak the ENTTEC DMX USB Pro-style serial protocol
directly (`dmx.py`, `dmx_controller.py`) to drive DMX fixtures: full-on,
blackout, breathing/pulsing fades, per-channel ramps, random "freak out"
flicker, and saved "scene" presets (`chair.py`, `path.py`, `sculpture.py`,
`waiting_room.py`). `externals/dmx.pd` and `dmx.pd` are Pure Data patches for
the same interface. Serial port is set per script (`/dev/enttec`,
`/dev/ttyUSB0` — see the udev rule below).

Run directly, e.g.:
```bash
python3 dmx/breathe.py
```
Dependency: `pyserial`.

### `osc/` — OSC control of a Behringer X-Air mixer

`osc-xair.pd` is a Pure Data patch that sends OSC-over-UDP messages
(`oscformat`, `netsend`) to set channel fader levels on a Behringer X18/X-Air
mixer. Easily extended to mute/pan/EQ. See `osc/README.md` and the included
screenshot for the patch layout.

Requires Pure Data with the `oscformat`/`net` externals (mrpeach or similar).

### `midi-automation/` — MIDI fader record & playback

`midi-automations.pd` records fader movements from a Korg nanoKONTROL-class
MIDI controller to a text log (`data.log`, `ceiling1.log`, `dimmer.log`) and
plays them back into faders, with `interpolate.pd` smoothing between
recorded points. Useful for repeatable lighting/sound fades without a full
show-control system.

### `fader-record-and-playback/` — standalone fader record/playback patch

`faders-record-and-playback.pd` is a simpler, self-contained variant of the
midi-automation patch: record fader movement to `automation.txt` and play it
back.

### `website_integration/` — Pure Data ↔ browser bridge (Node/WebSocket)

`bridge.js` is a small Node WebSocket server that relays messages between a
running Pure Data patch (`pd_patch.pd`) and a browser page (`index.html`,
`color.html`) — e.g. to reflect Pure Data output as an on-screen colour.
Run with:
```bash
cd website_integration
npm install
node bridge.js
```
then open `index.html` in a browser.

> **Known bloat:** `website_integration/node_modules/` is committed to git.
> It has been left in place and `.gitignore` now excludes `node_modules`
> going forward, but the already-tracked copy has not been removed from
> history (that would need a history rewrite, out of scope here).

### Root-level patches and notes

- `test.pd`, `recursion.pd`, `timed-positions.pd`, `heartbeatpulses.pd`,
  `ikeda tests.pd`, `arduino-send-float.pd` — standalone experiments/sketches
  (timing, recursion, sending floats to an Arduino over serial).
- `40hz.mp3` — an audio test file referenced by one of the patches.
- `99-usb-alias.rules` / `usbdevices.txt` — a udev rules example and notes
  for giving fixed serial-port aliases (e.g. `/dev/enttec`) to specific USB
  DMX/serial hardware by vendor/product/serial ID, so scripts can hard-code a
  stable device path. Install with:
  ```bash
  sudo cp 99-usb-alias.rules /etc/udev/rules.d/
  sudo udevadm control --reload-rules && sudo udevadm trigger
  ```

## Requirements

- [Pure Data](https://puredata.info/) (vanilla + `mrpeach`/OSC and MIDI
  support for the OSC and MIDI-automation patches)
- Python 3 with `pyserial` for the `dmx/` scripts
- Node.js with `ws` for `website_integration/`

## License

MIT — see [LICENSE](LICENSE).
