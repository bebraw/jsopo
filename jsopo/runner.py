# -*- coding: utf-8 -*-
from __future__ import with_statement

import glob
import os
import re
import sys
from optparse import OptionParser

import version

def process_line(line):
    line = line.strip()
    ops = {'+': 'add', '-': 'sub', '/': 'div', '*': 'mul', '%': 'mod', }

    def split_line(op):
        return re.split('(\\' + op + ')', line)

    splits = map(lambda op: split_line(op), ops.keys())
    matches = filter(lambda a: len(a) == 3, splits)

    if len(matches) == 1:
        l_part, op, r_part = matches[0]
        op_name = ops[op]

        l_split = l_part.split('=')

        if len(l_split) == 2:
            l_value1 = l_split[0].strip()
            l_value2 = l_split[1].strip()
            r_value = r_part.strip(' ;')

            return l_value1 + ' = ' + op_name + '(' + l_value2 + ', ' + \
                r_value + ');'
        else:
            l_value = l_part.strip()
            r_value = r_part.strip(' =;')

            return l_value + ' = ' + op_name + '(' + l_value + ', ' + \
                r_value + ');'

        return matches[0], l_split

    unary_ops = {'++': 'add', '--': 'sub'}

    matches = filter(lambda a: line.endswith(a + ';'), unary_ops.keys())

    if matches:
        op = matches[0]
        op_name = unary_ops[op]
        value = line.strip(' +-;')

        return value + ' = ' + op_name + '(' + value + ', 1);'

    return line

def evaluate(code):
    return '\n'.join(map(lambda line: process_line(line), code.split('\n')))

def output_js(option, opt, output_dir, parser):
    got_all = False

    for js_name in glob.glob('*.js'):
        with open(js_name) as f:
            lines = f.read()

        new_code = evaluate(lines)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        new_file = os.path.join(output_dir, js_name)

        def write_file():
            print('Writing ' + new_file)

            with open(new_file, 'w') as f:
                f.write(new_code)

        if os.path.exists(new_file):
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
                        js_name + ')?\n' + opts)

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
