def parse(line):
    return {}

    ret = {}

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
