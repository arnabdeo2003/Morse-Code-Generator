import tkinter as tk

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '   '  # Three spaces between words
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        morse_code += MORSE_CODE_DICT.get(char, '') + ' '
    return morse_code

def convert():
    input_text = entry.get()
    result = text_to_morse(input_text)
    output_label.config(text=result)

# Create main window
root = tk.Tk()
root.title("Morse Code Generator")

# Create input entry widget
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

# Create convert button
convert_button = tk.Button(root, text="Convert to Morse Code", command=convert)
convert_button.pack(pady=5)

# Label for showing output
output_label = tk.Label(root, text="", font=("Courier", 14), wraplength=500)
output_label.pack(padx=10, pady=10)

root.mainloop()
