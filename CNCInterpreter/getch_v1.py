from pynput import keyboard

def on_press(key):
    try:
        a = key
        print('key pressed: {0}'.format(a))
    
    except AttributeError:
        a = key
        print('key pressed: {0}'.format(a))
        
    
def on_release(key):
    a = key
    print('key released: {0}'.format(a))
    
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
