
class Shifts:
    def keygen(self, key):
        result = dict(
            a_key = [*key][0] + [*key][1],
            b_key = [*key][1] + [*key][2],
            c_key = [*key][2] + [*key][3],
            d_key = [*key][3] + [*key][4]
            )
        return result

    def offsetgen(self, date):
        date_squared = int(date) ** 2
        last_four = str(date_squared)[-4:]
        result = dict(
            a_offset = [*last_four][0],
            b_offset = [*last_four][1],
            c_offset = [*last_four][2],
            d_offset = [*last_four][3]
            )
        return result

    def final_shifts(self, key, date):
        keys = self.keygen(key)
        offsets = self.offsetgen(date)
        result = dict(
            a_shift = int(keys["a_key"]) + int(offsets["a_offset"]),
            b_shift = int(keys["b_key"]) + int(offsets["b_offset"]),
            c_shift = int(keys["c_key"]) + int(offsets["c_offset"]),
            d_shift = int(keys["d_key"]) + int(offsets["d_offset"])
            )
        import ipdb; ipdb.set_trace()
        return result

wip = Shifts()
key = "02715"
date = "040895"
final_shifts = wip.final_shifts(key, date)

