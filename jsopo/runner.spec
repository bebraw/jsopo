def process(self, op, op_name):
    runner.process('a = b ' + op + ' c;') == 'a = ' + op_name + '(b, c);'
    runner.process('a ' + op + '= b;') == 'a = ' + op_name + '(a, b);'

def process_unary(self, op, op_name):
    runner.process('a' + op + op + ';') == 'a = ' + op_name + '(a, 1);'

processes addition
    process(self, '+', 'add')
    process_unary(self, '+', 'add')

processes subtraction
    process(self, '-', 'sub')
    process_unary(self, '-', 'sub')

processes multiplication
    process(self, '*', 'mul')

processes division
    process(self, '/', 'div')

processes modulo
    process(self, '%', 'mod')

processes without match
    runner.process('foobar') == 'foobar'

processes globals
    runner.process('a = b + c;') == 'a = add(b, c);'

processes locals
    runner.process('var a = b + c;') == 'var a = add(b, c);'

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
