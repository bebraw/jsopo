def parse(line):
    ret = {}
    cur, prev = ret, None
    for chr in line:
        if chr.strip():
            if 'op' in cur:
                cur['r_value'] = chr
            elif 'l_value' in cur:
                cur['op'] = chr
            elif 'r_value' in cur:
                prev = cur
                cur = {}
                cur['l_value'] = prev['r_value']
                prev['r_value'] = cur
            else:
                cur['l_value'] = chr

    return ret

    # TODO
    # keep track of ()'s found (stack?)
    create_node = False
    for chr in line:
        if chr:
            if create_node:
                pass

            if chr == '(':
                create_node = True

    return ret
