from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image processing
import sounddevice as sound  # pip install sounddevice
from scipy.io.wavfile import write  # pip install scipy
import time
import wavio as wv  # pip install wavio

# Initialize root
root = Tk()
root.geometry("600x700+400+80")
root.resizable(False, False)
root.title("Voice Recorder")
root.configure(background="#4a4a4a")

# Function to record audio
def Record():
    try:
        freq = 44100  # Sampling frequency
        dur = int(duration.get())  # Retrieve duration from the entry box
        if dur <= 0:
            raise ValueError("Duration must be a positive number.")
        
        recording = sound.rec(dur * freq, samplerate=freq, channels=2)

        # Timer countdown
        temp = dur
        while temp > 0:
            timer_label.config(text=f"{temp}")  # Update countdown timer
            root.update()
            time.sleep(1)
            temp -= 1

        sound.wait()  # Wait for recording to finish
        write("recording.wav", freq, recording)  # Save the recording
        timer_label.config(text="Done!")
        messagebox.showinfo("Voice Recorder", "Recording saved successfully!")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid duration (positive integer).")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Icon
image_icon = PhotoImage(file="record.png")
root.iconphoto(False, image_icon)

# Logo (resized)
original_image = Image.open("Record.png")
resized_image = original_image.resize((150, 150))  # Resize to 150x150 pixels
photo = ImageTk.PhotoImage(resized_image)
myimage = Label(image=photo, background="#4a4a4a")
myimage.pack(padx=5, pady=5)

# Name
Label(
    text="Voice Recorder",
    font="arial 30 bold",
    background="#4a4a4a",
    fg="white"
).pack()

# Entry box for duration
duration = StringVar()
entry = Entry(root, textvariable=duration, font="arial 30", width=15)
entry.pack(pady=10)
Label(
    text="Enter time in seconds",
    font="arial 15",
    background="#4a4a4a",
    fg="white"
).pack()

# Countdown timer label
timer_label = Label(root, text="", font="arial 40", width=4, background="#4a4a4a", fg="white")
timer_label.place(x=240, y=590)

# Record button
record_button = Button(
    root,
    font="arial 20",
    text="Record",
    bg="#111111",
    fg="white",
    border=0,
    command=Record
)
record_button.pack(pady=30)

# Run the application
root.mainloop()
