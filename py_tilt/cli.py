# -*- coding: utf-8 -*-

"""Console script for py_tilt."""
import sys
import click
from bluetooth._bluetooth import hci_open_dev

from py_tilt.main import hci_le_set_scan_parameters, hci_enable_le_scan, monitor_tilt


@click.command()
def main(args=None):
    """Console script for py_tilt."""
    dev_id = 0

    try:
        sock = hci_open_dev(dev_id)
        print('Starting pytilt logger')
    except:
        print('error accessing bluetooth device...')
        sys.exit(1)

    hci_le_set_scan_parameters(sock)
    hci_enable_le_scan(sock)
    monitor_tilt(sock)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
