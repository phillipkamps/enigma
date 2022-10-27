# class Shifts:
def keygen(key):
    # result = dict(
    #     a_key = [*key][0] + [*key][1],
    #     b_key = [*key][1] + [*key][2],
    #     c_key = [*key][2] + [*key][3],
    #     d_key = [*key][3] + [*key][4]
    # )
    # result = {
    #     "a_key": [*key][0] + [*key][1],
    #     "b_key": [*key][1] + [*key][2],
    #     "c_key": [*key][2] + [*key][3],
    #     "d_key": [*key][3] + [*key][4]
    # }
    # return result
    return {
        x: key[x] + key[x + 1]
        for x in range(0, len(key) - 1)
    }

def offsetgen(date):
    date_squared = int(date) ** 2
    last_four = str(date_squared)[-4:]
    result = dict(
        a_offset = [*last_four][0],
        b_offset = [*last_four][1],
        c_offset = [*last_four][2],
        d_offset = [*last_four][3]
        )
    return result

def final_shifts(key, date):
    if len(key) > 9:
        raise RuntimeError(f"Value of key cannot exceed 9 characters, {key}")
    keys = {
        x: key[x] + key[x + 1]
        for x in range(0, len(key) - 1)
    }
    last_n = str(int(date) ** 2)[-(len(key) - 1):]
    offsets = dict(enumerate(last_n))
    result = {
        x: int(keys[x]) + int(offsets[x])
        for x in range(0, len(key) - 1)
    }
    return result
