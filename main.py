from tkinter import *
from tkinter import ttk

# Create top window
window = Tk()
window.title('MIDI CLOCK')

# Create frame layout
top_frame = Frame(window)
middle_frame = Frame(window)
bottom_frame = Frame(window)

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
send_button = Button(top_frame, text='SEND', command=send)
play_pause_button = Button(middle_frame, text='PLAY', command=play_pause)
rewind_button = Button(middle_frame, text='REWIND', command=rewind)
bpm_slider = Scale(bottom_frame, from_=40, to=300, orient=HORIZONTAL)

# Pack things
top_frame.pack(fill=X, padx=5, pady=2)
top_frame.columnconfigure(0, weight=1)
top_frame.columnconfigure(1, weight=1)
live_radio.grid(row=0, column=0, padx=10, pady=(5, 0), sticky='w')
onsend_radio.grid(row=1, column=0, padx=10, pady=5, sticky='w')
send_button.grid(row=0, column=1, rowspan=2, padx=10, sticky='e')
middle_frame.pack(fill=X, padx=5, pady=2)
middle_frame.columnconfigure(0, weight=1)
middle_frame.columnconfigure(1, weight=1)
play_pause_button.grid(row=0, column=0, padx=10, sticky='w')
rewind_button.grid(row=0, column=1, padx=10, sticky='e')
bottom_frame.pack(fill=X,padx=5, pady=2)
bpm_slider.pack(fill=X, padx=10)
window.mainloop()
