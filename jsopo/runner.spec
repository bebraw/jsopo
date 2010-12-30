# helper funcs

def process_line(self, op, op_name):
    runner.process_line('a = b ' + op + ' c;') == 'a = ' + op_name + '(b, c);'
    runner.process_line('a ' + op + '= b;') == 'a = ' + op_name + '(a, b);'

def process_line_unary(self, op, op_name):
    runner.process_line('a' + op + op + ';') == 'a = ' + op_name + '(a, 1);'


# op specific cases

processes addition
    process_line(self, '+', 'add')
    process_line_unary(self, '+', 'add')

processes subtraction
    process_line(self, '-', 'sub')
    process_line_unary(self, '-', 'sub')

processes multiplication
    process_line(self, '*', 'mul')

processes division
    process_line(self, '/', 'div')

processes modulo
    process_line(self, '%', 'mod')


# bracket specific cases

processes simple brackets
    runner.process_line('a = (b + c);') == 'a = add(b, c);'

processes multiple brackets
    runner.process_line('a = (a + (b - c));') == 'a = add(a, sub(b, c));'


# more general cases

processes without match
    runner.process_line('foobar') == 'foobar'

processes globals
    runner.process_line('a = b + c;') == 'a = add(b, c);'

processes locals
    runner.process_line('var a = b + c;') == 'var a = add(b, c);'

processes function calls
    runner.process_line('concat(a, b)') == 'concat(a, b)'

evaluates simple js
    given_js = '''
var a = new Point(2, 2);
'''
    expected_js = given_js

    runner.evaluate(given_js) == expected_js

evaluates js
    given_js = '''
var a = new Point(2, 2);
var b = new Point(1, 3);
var c = a + b;
'''
    expected_js = '''
var a = new Point(2, 2);
var b = new Point(1, 3);
var c = add(a, b);
'''

    runner.evaluate(given_js) == expected_js
