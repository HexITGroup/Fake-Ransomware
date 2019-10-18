#Totally Fake "Bad Rabbit" 2.0
#Great for pranking people who don't know how to restore explorer
#Decent for helping people understand what ransomware sometimes visually looks like, terrible for helping people understand how it actually works
#Tested in a corporate setting for fun
#Use with the caution that you could get reprimanded
#This is my first Python Project so mind the errors.
#Much of what you see here was learned from the books "Python Crash Course" and "Automate the Boring stuff with Python"
#take note of the tic mark comments that give you sub instructions.

import wmi
import os
import ctypes
from tkinter import *
import datetime

print("Присоединенный к 192.168.45.6...")#Connecting to 192.168.45.6...

def greet_user(username):
    #Здравствуйте
    print("Здравствуйте " + username.title() + "!")

greet_user('sdejulio')

print("Перевод файлов")

# kill explorer.exe
for process in wmi.WMI().Win32_Process():
    if process.Name == 'explorer.exe':
        os.system('c:\windows\system32\cmd.exe /c c:/windows/system32/taskkill.exe /F /IM explorer.exe')

# set desktop wallpaper to built in black image

SPI_SETDESKWALLPAPER = 20 # According to http://support.microsoft.com/default.aspx?scid=97142

SPIF_SENDCHANGE = 3

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C://Users//jbond//PycharmProjects//Sandyransomware//badrabbit2.bmp" , SPIF_SENDCHANGE)

print(ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C://Users//jbond//PycharmProjects//Sandyransomware//badrabbit2.bmp" , SPIF_SENDCHANGE))


# begin coding the window where the bulletin board is

# window height and width
canvas_width = 501
canvas_height = 250

# set the window's required root to the tkinter library with the title and background.
# then set the releife mode the "ridge" meaning border placement and the background to red, in case the image processor ever bleeds through
root = Tk()
root.title("                                                                                                                         YOUR COMPUTER HAS BEEN ENCRYPTED")
root.configure(background='black')


canvas = Canvas(root,
                width=canvas_width,
                height=canvas_height,
                background = "red",
                relief = 'ridge',
                bd = 0,
                highlightthickness=0
                )


# begin the canvas pack library by setting the prime photo to the desired directory right after defining it as "photoimage"
canvas.pack()

photo = PhotoImage(file="C://Users//jbond//PycharmProjects//Sandyransomware//badrabbit.gif")
canvas.create_image(250,150, image=photo)

# insert the labels that the see when the ransomware is activated in the window. Include font color and size
Label(text="OOPS! Your files have been encrypted.", bg='black', fg = 'red', font=("courier", 25)).pack()
Label(text="TIME LEFT TO PAY RANSOM:", bg='black', fg = 'red', font=("courier", 20)).pack()


# import tkinter again and define it as tk so the program can be recognized in the latest python being 3.4 and above
# import the datetime function which allows a clock to be put in place and configured as a widget.
# credit the GitHub's Technomancer for showing me how to do this after wasting a ton of time myself.


# import countdown class to configure date time function as a backwards clock.
class Countdown(tk.Frame):
    '''A Frame with label to show the time left, an entry to input the seconds to count
    down from, and a start button to start counting down.'''

# NOTE.... they removed the master slave terminology as of August 2017 so DO NOT think this will work over an circuit board. Please adjust accordingly******
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()

    def create_widgets(self):


# Configure the clock to be set in minutes: seconds: microseconds and center it so it looks pretty using the justify clause under the tk.entry motif
        self.label = tk.Label(self, text="00:00:00", bg='black', fg = 'red', font=("courier", 25))
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()

# insert docstring event, define countdown, and program the label to self update meaning work on its own be telling it to use the timer function at -=1
# that last part means the value is equal to a minus one factor
    def countdown(self):
        '''Update label based on the time left.'''
        self.label['text'] = self.convert_seconds_left_to_time()

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)

# start AS SOON as the program is opened. Do not delay.
        else:
            self._timer_on = True

# define the start button as the programs own initiation
    def start_button(self):
        '''Start counting down. Change time Accordingly'''
        self.time_set = 3600
        self.seconds_left = int(self.time_set)   # 1. time is set above
        self.stop_timer()                           # 2. to prevent having multiple
        self.countdown()                            #    timers at once
                                                    # 3. lol do not mess with this unless you want a broken timer (personal note to future self)

  # the next few lines tell you that unless you want it to do something, this timer is only a means of making the viewer panic

    def stop_timer(self):
        '''Stops after schedule from executing.'''
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):

        return datetime.timedelta(seconds=self.seconds_left)

# set to root as countdown so the program knows where to look and appropriate the function
if __name__ == '__main__':
    root.resizable(False, False)

    countdown = Countdown(root)
    countdown.pack()
    countdown.start_button()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

# more jargon labels to scare the user
# credit goes to ransomware, Bad Rabbit

Label(text="If you see this text, your files are no longer accessible. ", bg='black', fg = 'red', font=("courier", 15)).pack()
Label(text="You might have been looking for a way to recover your files. ", bg='black', fg = 'red', font=("courier", 15)).pack()
Label(text="Don't waste your time. No one will be able to recover them without our decrytion service.", bg='black', fg = 'red', font=("courier", 15)).pack()


separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

Label(text="We guarantee that you can recover all your files safely. All you need to do is submit the payment and get the decryption password")


# Disable ability to close program by telling function to pass


def close_program():
    root.destroy()


# delete this line if you want the program to close but that makes it less fun.
def disable_event():
    pass

root.protocol("WM_DELETE_WINDOW", disable_event)

def callback():
    print ("user clicked pay ransom")

# this is how I made the window self populate like many viruses do.
# feel free to copy this stuff if you want to learn how to do it yourself in your own programs.
# I myself learned it from the book "Automate the Boring Stuff with Python"

def create_window():
    top = tk.Toplevel()
    top.title("Payment Info")

    msg = Message(top, text="Enter Payment Info")
    msg.pack()

    group = LabelFrame(top, text="Enter Bank Account #", padx=10, pady=10)
    group.pack(padx=10, pady=10)

    w = Entry(group)
    w.pack()

    group = LabelFrame(top, text="Enter Routing #", padx=10, pady=10)
    group.pack(padx=10, pady=10)

    w = Entry(group)
    w.pack()

    group = LabelFrame(top, text="Enter Email Address (Your Encryption Key will be sent here)", padx=10, pady=10)
    group.pack(padx=10, pady=10)

    w = Entry(group)
    w.pack()

    button = Button(top, text="Send", command=top.destroy)
    button.pack()


# does nothing but looks legitimate
b = tk.Button(root, text="Pay Ransom Now", command=create_window)
b.pack()

group = LabelFrame(root, text="Enter Encryption Key Here", padx=5, pady=5)
group.pack(padx=10, pady=10)

w = Entry(group)
w.pack()


# always end your prgram with a loop function so the damn thing actually knows how to run the code in the order given and on repeat until the person figures out how to kill it.
root.mainloop()


root.mainloop()
