from tkinter import *
from tkinter import ttk

# Create top window
window = Tk()
window.title('MIDI CLOCK')
window.geometry('300x150')

# Create frame layout
top_frame = Frame(window, bg='cyan')
top_left_frame = Frame(top_frame, bg='cyan')
middle_frame = Frame(window, bg='blue')
bottom_frame = Frame(window, bg='yellow')

# Event variables
is_live = BooleanVar(value=True)
is_playing = BooleanVar(value=False)

# Event functions
def change_mode():
  pass

def play_pause():
  pass

def rewind():
  pass

def send():
  pass

# Create widgets
live_radio = Radiobutton(top_frame, variable=is_live, text='LIVE', value=True, command=change_mode)
onsend_radio = Radiobutton(top_frame, variable=is_live, text='ONSEND', value=False, command=change_mode)
send_button = Button(top_left_frame, text='SEND', command=send)
play_pause_button = Button(middle_frame, text='PLAY', command=play_pause)
rewind_button = Button(middle_frame, text='REWIND', command=rewind)
bpm_slider = Scale(bottom_frame, from_=40, to=300, orient=HORIZONTAL)


window.mainloop()
