#!/usr/bin/python3
"""
This Python module sends a packet
"""

from argparse import ArgumentParser, Namespace
from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice
from digi.xbee.models.address import XBee64BitAddress


def get_options() -> Namespace:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('input', type=str, help='This is the input sent to the remote device')
    parser.add_argument('-d', '--device', default="/dev/ttyUSB0", type=str, help='Which device the XBee thingy is connected to')
    parser.add_argument('-b', '--baudrate', default=9600, type=int, help='Baudrate to use')
    parser.add_argument('-m', '--mac', default="0013A2004155BA72", type=str, help='recipient MAC address string')
    return parser.parse_args()


def main() -> None:
    options = get_options()

    # Instantiate a local XBee node.
    xbee = XBeeDevice(options.device, options.baudrate)
    xbee.open()

    # Instantiate a remote XBee node.
    remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string(options.mac))

    # Send data using the remote object.
    xbee.send_data(remote, options.input)


if __name__ == '__main__':
    main()
