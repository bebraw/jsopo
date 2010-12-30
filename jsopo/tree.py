def parse(line):
    def recursion(i):
        ret = {}

        r_value_i = None
        while i < len(line):
            char = line[i].strip()

            if char:
                if 'r_value' in ret:
                    ret['r_value'] = recursion(r_value_i)

                    break
                if 'op' in ret:
                    ret['r_value'] = char
                    r_value_i = i
                elif 'l_value' in ret:
                    ret['op'] = char
                else:
                    ret['l_value'] = char

            i += 1

        return ret

    return recursion(0)
