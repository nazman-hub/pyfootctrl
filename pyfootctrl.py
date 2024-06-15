import time

import rtmidi # https://spotlightkid.github.io/python-rtmidi/

from config import behaviour
from chocolate import display

import psutil

import subprocess
import os

# For windows, get loop midi at https://www.tobias-erichsen.de/software/loopmidi.html
# midiberry for BLE https://apps.microsoft.com/store/detail/midiberry/9N39720H2M05?hl=pt-br&gl=br

midi_in = rtmidi.MidiIn()
in_ports_by_name = midi_in.get_ports()

midi_out = rtmidi.MidiOut()
out_ports_by_name = midi_out.get_ports()

def run_shortcut(shortcut_path):
    if os.path.exists(shortcut_path):
        subprocess.Popen(shortcut_path, shell=True)
        print(f"Opening {shortcut_path}")
    else:
        print(f"Shortcut {shortcut_path} does not exist")

def is_program_running(program_name):
    # Check if there is any running process that contains the program name.
    for proc in psutil.process_iter(['name']):
        try:
            if program_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def display_midi_ports():
    print("Available MIDI IN ports:", '\n'.join([ f'{number} -> {name}' for number,name in enumerate(in_ports_by_name)]), sep='\n')
    print()
    print("Available MIDI OUT ports:", '\n'.join([ f'{number} -> {name}' for number,name in enumerate(out_ports_by_name)]), sep='\n')
    print()

def user_input_midi_ports():
    in_port = int(input("Input port number:"))
    out_port = int(input("Output port number:"))
    print(f"Input: {in_ports_by_name[in_port]} | Output: {out_ports_by_name[out_port]}")
    return in_port, out_port

def match_device_name(expected_name_parts, device_name):
    for expected_name_part in expected_name_parts:
        if expected_name_part in device_name:
            return True
    return False

def default_midi_ports():
    """
    Return the default MIDI ports indexes, with MIDI IN as USB-Midi and MIDI OUT as loopMIDI
    """

    DEFAULT_MIDI_IN_PORT_NAMES = ['FootCtrl','USB-Midi']
    DEFAULT_MIDI_OUT_PORT_NAMES = ['Midi Through','loopMIDI']
    in_port_index = None
    out_port_index = None
    for index, port_name in enumerate(in_ports_by_name):
        if match_device_name(DEFAULT_MIDI_IN_PORT_NAMES, port_name):
            in_port_index = index
            break
    else:
        print("MIDI input device not found")
    for index, port_name in enumerate(out_ports_by_name):
        if match_device_name(DEFAULT_MIDI_OUT_PORT_NAMES, port_name):
            out_port_index = index
            break
    else:
        print("MIDI output device not found")
    return in_port_index, out_port_index

def start_midi_loop(midi_in, midi_out): 
    print("Starting MIDI message processing loop...")
    while True:
        message = midi_in.get_message()
        
        if message:
            try:
                ([midi_msg_type, midi_msg_data], delta_seconds) = message
                footswitch = display(midi_msg_data)
                print(f"{footswitch} | {midi_msg_type} | {midi_msg_data} | {delta_seconds:0.000f}s")
                behaviour[footswitch](midi_out, delta_seconds)
                
            except ValueError as e:
                print(e)
                print(message)
        time.sleep(0.001)


if __name__ == '__main__':
    shortcut_path = 'loopmidi.lnk'
    run_shortcut(shortcut_path)

    program_name = "loopMIDI.exe"  # The program to wait for

    print(f"Waiting for {program_name} to start...")
    
    # Use a while loop to wait until the program is detected
    while not is_program_running(program_name):
        time.sleep(1)  # Wait for 1 second before checking again

    print(f"{program_name} detected. Running the script.")





    in_port, out_port = default_midi_ports()
    midi_in.open_port(in_port)
    midi_out.open_port(out_port)
    try:
        start_midi_loop(midi_in, midi_out)
    except KeyboardInterrupt:
        print("Bye!")
        exit(0)

