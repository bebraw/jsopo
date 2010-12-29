# -*- coding: utf-8 -*-
from __future__ import with_statement

import os
import re
import sys
from optparse import OptionParser

import version

def process(line):
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
    return '\n'.join(map(lambda line: process(line), code.split('\n')))

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
