import os
import subprocess
import time
import tkinter as tk
from tkinter import messagebox

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)

def open_shortcut(shortcut_path):
    """Open a shortcut file (.lnk)."""
    subprocess.Popen(shortcut_path, shell=True)

def execute_exe(exe_path):
    """Execute an executable file (.exe)."""
    subprocess.Popen(exe_path)

if __name__ == "__main__":
    # Example paths (replace with your actual paths)
    loopMIDI_path = r'C:\Program Files (x86)\Tobias Erichsen\loopMIDI\loopMIDI.exe'
    exe_path = r'C:\VSCode\pyfootctrl\dist\pyfootctrl.exe'

    # Open the shortcut
    execute_exe(loopMIDI_path)

    
    # Execute the executable
    execute_exe(exe_path)
