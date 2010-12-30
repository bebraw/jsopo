parses empty line
    tree.parse('') == {}

parses single character
    tree.parse('a') == {'l_value': 'a'}

parses single character and op
    tree.parse('a +') == {'l_value': 'a', 'op': '+'}

parses simple calculation
    tree.parse('a + b') == {'l_value': 'a', 'op': '+', 'r_value': 'b'}

parses simple line
    tree.parse('a = b + c') == {'l_value': 'a', 'op': '=', 'r_value': {'l_value': 'b', 'op': '+', 'r_value': 'c'}}

parses simple bracket
    tree.parse('(a + b)') == {'l_value': {'l_value': 'a', 'op': '+', 'r_value': 'b'}}

parses right bracket
    tree.parse('a + (b - c)') == {'l_value': 'a', 'op': '+', 'r_value': {'l_value': 'b', 'op': '-', 'r_value': 'c'}}

parses left bracket
    tree.parse('(a + b) - c') == {'l_value': {'l_value': 'a', 'op': '+', 'r_value': 'b'}, 'op': '-', 'r_value': 'c'}
