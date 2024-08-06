from pypdf import PdfReader
import pyttsx3
import os
import customtkinter as ctk
from customtkinter import filedialog
# from gtts import gTTS

# creating a pdf reader object
app = ctk.CTk()
app.geometry("600x600")
app.title("PDF to Audio Book")
ctk.set_default_color_theme("green")
ctk.set_appearance_mode("dark")

engine = pyttsx3.init()

def get_text(file,x):

    pages = []
    reader = PdfReader(file)
    for page in reader.pages:
        text = page.extract_text()
        pages.append(text)
        page = ". ".join(pages)

    engine.save_to_file(page, f"{x}.mp3")
    engine.runAndWait()
    engine.stop()



        # self.language = 'en'
        # self.audio = gTTS(text=page, lang=language, slow=False)





def get():
    file_path = filedialog.askopenfilename()
    # turn it into a list
    folder = file_path.split("/")
    # get only the lastone
    file_name = file_path.split("/")[-1]
    # remove it
    folder.remove(file_name)

    x = []
    for i in folder:
        # then append it into another list using for loop
        x.append(i+"\\")
    # join it into a string
    save_dir = r" ".join(x)
    #  I need you to find a way to remove space from strings
    s = save_dir.replace(" ", "")

    print(s)
    print(f"{s}{file_name}")
    dir = f"{s}{file_name}"
    def listen():
        os.system(f"{s}{file_name}.mp3")
    get_text(file_path,file_name)
    intro2 = ctk.CTkLabel(app, text="Audio Ready", font=("Arial", 40), text_color="green")
    intro2.pack(pady=30, padx=30)

    btn2 = ctk.CTkButton(app, text="Listen", width=60, height=60, font=("Arial", 15), command=listen)
    btn2.pack(pady=30, padx=30)

intro = ctk.CTkLabel(app,text="Turn Your PDF Into An Audio Book ",font=("Arial", 30))
intro.pack(pady=30,  padx=30)
btn = ctk.CTkButton(app, text="Select PDF", width=60, height=60, font=("Arial", 15), command=get)
btn.pack(pady=30, padx=30)
if __name__ == "__main__":
    app.mainloop()



