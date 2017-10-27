#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os

import bluetooth
from flask import Flask


def lookup_device(device, timeout):
    result = bluetooth.lookup_name(device, timeout)
    return result is not None


app = Flask(__name__)


@app.route('/')
def root():
    device = os.environ.get('BUTTON_DEVICE', None)
    print(device)
    if not device:
        return 'Specify BUTTON_DEVICE env variable'
    elif lookup_device(device, 3):
        return 'Device {} detected'.format(device)
    else:
        return 'Hello World'


app.run(host='0.0.0.0')
