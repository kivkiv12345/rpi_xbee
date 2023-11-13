#!/usr/bin/python3
"""
This Python module continuously receives packets
"""

from argparse import ArgumentParser, Namespace
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress


def get_options() -> Namespace:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('-d', '--device', default="/dev/ttyUSB0", type=str, help='Which device the XBee thingy is connected to')
    parser.add_argument('-b', '--baudrate', default=9600, type=int, help='Baudrate to use')
    parser.add_argument('-t', '--timeout', default=1000, type=int, help='Timeout for receive')
    return parser.parse_args()


def main() -> None:
    options = get_options()

    # Instantiate a local XBee node.
    xbee = XBeeDevice(options.device, options.baudrate)
    xbee.open()

    while True:
        # Read data.
        xbee_message = xbee.read_data(options.timeout)
        if xbee_message is not None:
            print(xbee_message.data.decode())


if __name__ == '__main__':
    main()
