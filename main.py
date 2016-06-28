#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

import converter

# Main parser
parser = argparse.ArgumentParser(
    description='Convert PluXML files to Markdown')

parser.add_argument(
    'filename',
    type=open,
    help='File to import')

parser.set_defaults(
    func=converter.convert)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)  # call the default function
