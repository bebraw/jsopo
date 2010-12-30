def parse(line):
    def recursion(i):
        ret = {}

        r_value_i = None
        while i < len(line):
            char = line[i].strip()

            if char:
                if char is '(':
                    if 'l_value' in ret:
                        pass
                    else:
                        ret['l_value'] = recursion(i + 1)

                        break
                elif char is ')':
                    pass # ok???
                elif 'r_value' in ret:
                    # XXX (this fails in (a+b)-c at b) -> check next char
                    ret['r_value'] = recursion(r_value_i)

                    break
                elif 'op' in ret:
                    ret['r_value'] = char
                    r_value_i = i
                elif 'l_value' in ret:
                    ret['op'] = char
                else:
                    ret['l_value'] = char

            i += 1

        return ret

    return recursion(0)
