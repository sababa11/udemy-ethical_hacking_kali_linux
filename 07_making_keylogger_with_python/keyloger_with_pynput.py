from pynput.keyboard import Key, Listener, KeyCode


def get_key_name(key):
    if isinstance(key, KeyCode):
        return key.char
    else:
        return str(key)

def on_press(key):
    key_name = get_key_name(key)
    print("Key %s pressed" % key_name)

def on_release(key):
    key_name = get_key_name(key)
    print("Key %s released" % key_name)
    if key == Key.esc:
        print("Exiting")
        return False
    return None

def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == '__main__':
    main()
