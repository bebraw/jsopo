def process(self, p, op, op_name):
    p.process('a = b ' + op + ' c;') == 'a = ' + op_name + '(b, c);'
    p.process('a ' + op + '= b;') == 'a = ' + op_name + '(a, b);'

def process_unary(self, p, op, op_name):
    p.process('a' + op + op + ';') == 'a = ' + op_name + '(a, 1);'

set up
    p = runner.Processor()

processes addition
    process(self, p, '+', 'add')
    process_unary(self, p, '+', 'add')

processes subtraction
    process(self, p, '-', 'sub')
    process_unary(self, p, '-', 'sub')

processes multiplication
    process(self, p, '*', 'mul')

processes division
    process(self, p, '/', 'div')

processes modulo
    process(self, p, '%', 'mod')

processes without match
    p.process('foobar') == 'foobar'
