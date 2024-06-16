import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)

midiin = rtmidi.MidiIn()
available_ports = midiin.get_ports()

print(available_ports)