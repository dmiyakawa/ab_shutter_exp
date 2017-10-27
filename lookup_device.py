#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# on Ubuntu 16.04, only Python 2 seems to have python-bluez
#
# https://shkspr.mobi/blog/2016/02/cheap-bluetooth-buttons-and-linux/
#

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import bluetooth
from logging import DEBUG, getLogger, StreamHandler, Formatter

try:
    from logging.handlers import NullHandler
except Exception:
    from logging import Handler

    class NullHandler(Handler):
        def handle(self, record):
            pass

        def emit(self, record):
            pass

        def createLock(self):
            self.lock = None

import sys
import time

null_logger = getLogger("null")
null_logger.propagate = False
null_logger.addHandler(NullHandler())


def lookup_device(device, timeout, logger=null_logger):
    result = bluetooth.lookup_name(device, timeout)
    logger.debug('Lookup result: {}'.format(result))
    return result is not None


def main():
    parser = ArgumentParser(description=(__doc__),
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('device',
                        help='Specify device address')
    parser.add_argument('-t', '--timeout', type=int, default=5,
                        help='Lookup timeout')
    parser.add_argument('--log', default='INFO',
                        help=('Set log level.'
                              ' NOTSET, DEBUG, INFO, WARN, ERROR, CRITICAL'
                              ' is available'))
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Same as --log DEBUG')
    parser.add_argument('-s', '--silent', action='store_true',
                        help='No message will be shown.')

    args = parser.parse_args()
    logger = getLogger(__name__)
    handler = StreamHandler()
    logger.addHandler(handler)
    if args.debug:
        logger.setLevel(DEBUG)
        handler.setLevel(DEBUG)
    handler.setFormatter(Formatter('%(asctime)s %(levelname)7s %(message)s'))
    logger.debug('Start runnind on {}'.format(
        time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())))
    logger.debug('device: {}, timeout: {}'
                 .format(args.device, args.timeout))
    result = lookup_device(device=args.device,
                           timeout=args.timeout,
                           logger=logger)

    ret = 2
    if result:
        if not args.silent:
            print('Device detected')
        ret = 0
    else:
        if not args.silent:
            print('Device NOT detected')
        ret = 1
    logger.debug('Finish runnind on {}'.format(
        time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())))
    return ret


if __name__ == '__main__':
    sys.exit(main())
