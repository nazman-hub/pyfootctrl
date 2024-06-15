from collections import defaultdict

from transforms import *
from behaviours import null_behaviour, toggle_behaviour, tap_tempo_behaviour, keyboard_behaviour

behaviour = defaultdict(null_behaviour)

"""
Define the desired behaviours per preset slot here:
"""

behaviour['1A'] = toggle_behaviour(channel=0, control=0, off_cc_value=1)
behaviour['1B'] = toggle_behaviour(channel=0, control=1, off_cc_value=1)
behaviour['1C'] = toggle_behaviour(channel=0, control=2, off_cc_value=1)
behaviour['1D'] = toggle_behaviour(channel=0, control=3, off_cc_value=1)

behaviour['2A'] = toggle_behaviour(channel=0, control=4, off_cc_value=1)
behaviour['2B'] = toggle_behaviour(channel=0, control=5, off_cc_value=1)
behaviour['2C'] = toggle_behaviour(channel=0, control=6, off_cc_value=1)
behaviour['2D'] = toggle_behaviour(channel=0, control=7, off_cc_value=1)

behaviour['3A'] = toggle_behaviour(channel=0, control=8, off_cc_value=1)
behaviour['3B'] = toggle_behaviour(channel=0, control=9, off_cc_value=1)
behaviour['3C'] = toggle_behaviour(channel=0, control=10, off_cc_value=1)
behaviour['3D'] = toggle_behaviour(channel=0, control=11, off_cc_value=1)

behaviour['4A'] = toggle_behaviour(channel=0, control=12, off_cc_value=1)
behaviour['4B'] = toggle_behaviour(channel=0, control=13, off_cc_value=1)
behaviour['4C'] = toggle_behaviour(channel=0, control=14, off_cc_value=1)
behaviour['4D'] = toggle_behaviour(channel=0, control=15, off_cc_value=1)

behaviour['5A'] = toggle_behaviour(channel=0, control=16, off_cc_value=1)
behaviour['5B'] = toggle_behaviour(channel=0, control=17, off_cc_value=1)
behaviour['5C'] = toggle_behaviour(channel=0, control=18, off_cc_value=1)
behaviour['5D'] = toggle_behaviour(channel=0, control=19, off_cc_value=1)

behaviour['6A'] = toggle_behaviour(channel=0, control=20, off_cc_value=1)
behaviour['6B'] = toggle_behaviour(channel=0, control=21, off_cc_value=1)
behaviour['6C'] = toggle_behaviour(channel=0, control=22, off_cc_value=1)
behaviour['6D'] = toggle_behaviour(channel=0, control=23, off_cc_value=1)

behaviour['7A'] = toggle_behaviour(channel=0, control=24, off_cc_value=1)
behaviour['7B'] = toggle_behaviour(channel=0, control=25, off_cc_value=1)
behaviour['7C'] = toggle_behaviour(channel=0, control=26, off_cc_value=1)
behaviour['7D'] = toggle_behaviour(channel=0, control=27, off_cc_value=1)

behaviour['8A'] = toggle_behaviour(channel=0, control=28, off_cc_value=1)
behaviour['8B'] = toggle_behaviour(channel=0, control=29, off_cc_value=1)
behaviour['8C'] = toggle_behaviour(channel=0, control=30, off_cc_value=1)
behaviour['8D'] = toggle_behaviour(channel=0, control=31, off_cc_value=1)

# behaviour['1D'] = tap_tempo_behaviour(channel=0, control=23, reset_after=4.001, transform=seconds_to_byod_delay_midi_cc)

# behaviour['2A'] = keyboard_behaviour('r', ctrl=True)