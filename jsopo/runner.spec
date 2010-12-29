def process_line(self, op, op_name):
    runner.process_line('a = b ' + op + ' c;') == 'a = ' + op_name + '(b, c);'
    runner.process_line('a ' + op + '= b;') == 'a = ' + op_name + '(a, b);'

def process_line_unary(self, op, op_name):
    runner.process_line('a' + op + op + ';') == 'a = ' + op_name + '(a, 1);'

process_linees addition
    process_line(self, '+', 'add')
    process_line_unary(self, '+', 'add')

process_linees subtraction
    process_line(self, '-', 'sub')
    process_line_unary(self, '-', 'sub')

process_linees multiplication
    process_line(self, '*', 'mul')

process_linees division
    process_line(self, '/', 'div')

process_linees modulo
    process_line(self, '%', 'mod')

process_linees without match
    runner.process_line('foobar') == 'foobar'

process_linees globals
    runner.process_line('a = b + c;') == 'a = add(b, c);'

process_linees locals
    runner.process_line('var a = b + c;') == 'var a = add(b, c);'

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
