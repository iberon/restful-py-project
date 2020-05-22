#!/usr/bin/env python3

import os
from sys import stdout
import argparse

from models.file_helper import FileHelper
from models.http_rest import HttpRest

parser = argparse.ArgumentParser()
# Adding Positional Arguments
parser.add_argument("method", choices=["get", "post"], help="Request method")
parser.add_argument("endpoint", help="Request endpoint URI fragment")
# Adding Options
parser.add_argument("-o", "--output", help="Output to .json or .csv file (default: dump to stdout)")
parser.add_argument("-d", "--data", help="Data to send with request")

# Parsing
args = parser.parse_args()
method = args.method
endpoint = args.endpoint
data = args.data
output = None
ext = None
file_helper = None

if args.output:
    choices = ("csv", "json")
    output = args.output
    # Check if has the correct extension
    ext = os.path.splitext(output)[1][1:]
    if ext not in choices:
        parser.error("file doesn't end with one of {}".format(choices))
    else:
        file_helper = FileHelper(output, ext)

# Perform request
rest = HttpRest()
response = rest.call(method, endpoint, data)

# Return information
if file_helper is not None:
    file_helper.download(response.json())
else:
    stdout.write(rest.parse_response(response))

# Always show the status
stdout.write("Status code: " + str(response.status_code))
