from weakref import proxy
from ..lib.shifts import Shifts

key = "02715"
date = "040895"
wip = Shifts()

def test_keygen():
    key_dict = wip.keygen(key)
    assert key_dict is not None
    assert type(key_dict) is dict
    assert key_dict == {'a_key': '02', 'b_key': '27', 'c_key': '71', 'd_key': '15'}

def test_offsetgen():
    offset_dict = wip.offsetgen(date)
    assert offset_dict is not None
    assert type(offset_dict) is dict
    assert offset_dict == {'a_offset': '1', 'b_offset': '0', 'c_offset': '2', 'd_offset': '5'}

def test_final_shifts():

    final_shifts = wip.final_shifts(key, date)

    assert final_shifts is not None
    assert type(final_shifts) is dict
    assert final_shifts == {'a_shift': 3, 'b_shift': 27, 'c_shift': 73, 'd_shift': 20}