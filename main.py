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
    return parser.parse_args()


def main() -> None:
    # Instantiate a local XBee node.
    xbee = XBeeDevice("/dev/ttyUSB0", 9600)
    xbee.open()

    # Instantiate a remote XBee node.
    remote = RemoteXBeeDevice(xbee, XBee64BitAddress.from_hex_string("0013A2004155BA72"))

    # Send data using the remote object.
    xbee.send_data(remote, get_options().input)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
