# -*- coding: utf-8 -*-
from __future__ import with_statement

import os
import sys
from optparse import OptionParser

import version

def get_base_name(a):
    return os.path.splitext(a)[0]

def output_js(option, opt, output_dir, parser):
    # TODO!!!
    got_all = False

    for spec_name in get_specs():
        with open(spec_name) as f:
            lines = f.readlines()

        base_name = get_base_name(spec_name)
        processor = SpecificationProcessor(base_name)
        spec_code = processor.process(lines)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        py_file_name = 'test_' + base_name + '.py'
        py_file = os.path.join(output_dir, py_file_name)

        def write_file():
            print('Writing ' + py_file)

            with open(py_file, 'w') as f:
                f.write(spec_code)

        if os.path.exists(py_file):
            def do_nothing():
                print('Doing nothing.')

            possible_answers = {
                'Y': write_file,
                'N': do_nothing,
                'A': None
            }
            opts = '/'.join(possible_answers.keys())
            answer = None

            while answer not in possible_answers:
                if got_all:
                    answer = 'Y'
                else:
                    answer = raw_input('Are you sure you want to override file (' +
                        py_file_name + ')?\n' + opts)

                    if answer == 'A':
                        got_all = True
                        answer = 'Y'

            possible_answers[answer]()
        else:
            write_file()

def show_version(*args):
    print("jsopo %s" % version.get())
    sys.exit(0)

def main():
    usage = """usage: %prog command [args] [options]"""

    description = """Brief Description:
jsopo is a JavaScript precompiler. It provides a naive way to use operator overloading in the language."""

    epilog = """\nLong Description:
TODO"""

    class MyParser(OptionParser):
        def format_epilog(self, formatter):
            return self.epilog

    parser = MyParser(usage=usage, description=description, epilog=epilog)
    parser.add_option("-v", "--version", action="callback",
        callback=show_version,
        help="show program's version number and exit")
    parser.add_option("-o", "--output", action="callback",
        dest="output_folder", type="string",
        callback=output_js,
        help="output generated JavaScript files to given folder")

    parser.parse_args()

if __name__ == '__main__':
    main()
