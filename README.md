# web-traffic-status-lights
Display web traffic and/or web application conection stats on a series of lights using a Raspberry Pi and a relay

Example data sources include:
- Google Analytics
- Keen
- Datadog

# Installation
Clone this repository into the pi users home directory

Place the Adafruit APIkey in a file called `adafruitKey.txt` in this repo's directory

Install Upstart with: `sudo apt-get install upstart`

Place the statusservice.conf file in /etc/init

Reboot the Pi

## Sources File
The information for each of the data sources that are to be displayed should be located in a `sources.json` file. An example of what this file should look like can be found in the `example_sources.json` file.

TODO:
- dynamic threshold
- change source more frequently than the 5 min data refresh