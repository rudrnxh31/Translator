from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    source_lang = source_language_combobox.get()
    target_lang = target_language_combobox.get()
    source_text = source_textbox.get("1.0", END).strip()

    if not source_text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    if source_lang == "Select Source Language" or target_lang == "Select Target Language":
        messagebox.showwarning("Selection Error", "Please select both source and target languages.")
        return

    try:
        translator = Translator()
        translated_text = translator.translate(source_text, src=get_language_code(source_lang), dest=get_language_code(target_lang)).text
        target_textbox.config(state=NORMAL)
        target_textbox.delete("1.0", END)
        target_textbox.insert(END, translated_text)
        target_textbox.config(state=DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred during translation:\n{str(e)}")

def get_language_code(language):
    for code, lang in LANGUAGES.items():
        if lang == language:
            return code
    return "en"  # Default to English

def clear_text():
    source_textbox.delete("1.0", END)
    target_textbox.config(state=NORMAL)
    target_textbox.delete("1.0", END)
    target_textbox.config(state=DISABLED)
    source_language_combobox.set("Select Source Language")
    target_language_combobox.set("Select Target Language")

def copy_to_clipboard():
    target_text = target_textbox.get("1.0", END).strip()
    if target_text:
        root.clipboard_clear()
        root.clipboard_append(target_text)
        root.update()
        messagebox.showinfo("Copied", "Translated text copied to clipboard.")
    else:
        messagebox.showwarning("Copy Error", "No text to copy.")

# Main window setup
root = Tk()
root.title("Advanced Language Translator")
root.geometry("700x800")
root.config(bg="#e6f2ff")

# Title label
title_label = Label(root, text="Advanced Language Translator", font=("Arial", 30, "bold"), bg="#00509e", fg="white")
title_label.pack(pady=20, fill=X)

# Source text section
source_label = Label(root, text="Source Text", font=("Arial", 14, "bold"), bg="#e6f2ff")
source_label.pack(pady=5)

source_textbox = Text(root, font=("Arial", 12), wrap=WORD, height=8, width=60)
source_textbox.pack(pady=10)

# Source language combobox
source_language_combobox = ttk.Combobox(root, values=["Select Source Language"] + list(LANGUAGES.values()), font=("Arial", 12), state="readonly")
source_language_combobox.set("Select Source Language")
source_language_combobox.pack(pady=5)

# Target language combobox
target_language_combobox = ttk.Combobox(root, values=["Select Target Language"] + list(LANGUAGES.values()), font=("Arial", 12), state="readonly")
target_language_combobox.set("Select Target Language")
target_language_combobox.pack(pady=5)

# Buttons frame
button_frame = Frame(root, bg="#e6f2ff")
button_frame.pack(pady=15)

translate_button = Button(button_frame, text="Translate", font=("Arial", 14, "bold"), bg="#00509e", fg="white", command=translate_text)
translate_button.grid(row=0, column=0, padx=10)

clear_button = Button(button_frame, text="Clear", font=("Arial", 14, "bold"), bg="#ff4d4d", fg="white", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

copy_button = Button(button_frame, text="Copy", font=("Arial", 14, "bold"), bg="#34a853", fg="white", command=copy_to_clipboard)
copy_button.grid(row=0, column=2, padx=10)

# Target text section
target_label = Label(root, text="Translated Text", font=("Arial", 14, "bold"), bg="#e6f2ff")
target_label.pack(pady=5)

target_textbox = Text(root, font=("Arial", 12), wrap=WORD, height=8, width=60, state=DISABLED)
target_textbox.pack(pady=10)

# Footer branding
footer_label = Label(root, text="Developed by Rudransh Kumar", font=("Arial", 10), bg="#e6f2ff", fg="#00509e")
footer_label.pack(side=BOTTOM, pady=10)

# Run the main loop
root.mainloop()

