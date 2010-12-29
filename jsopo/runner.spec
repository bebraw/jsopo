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
