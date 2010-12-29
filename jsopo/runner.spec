def process(p, op, op_name):
    p.process('a = b ' + op + ' c;') == 'a = ' + op_name + '(b, c);'
    p.process('a ' + op + '= b;') == 'a = ' + op_name + '(a, b);'

def process_unary(p, op, op_name):
    p.process('a' + op + op + ';') == 'a = ' + op_name + '(a, 1);'

set up
    p = runner.Processor()

processes addition
    process(p, '+', 'add')
    process_unary(p, '+', 'add')

processes subtraction
    process(p, '-', 'sub')
    process_unary(p, '-', 'sub')

processes multiplication
    process(p, '*', 'mul')

processes division
    process(p, '/', 'div')

processes modulo
    process(p, '%', 'mod')
