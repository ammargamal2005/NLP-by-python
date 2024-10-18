from deep_translator import GoogleTranslator
import customtkinter as ctk 


def tra():
     sou = ent.get()
     trag = ent1.get()
     text_To_translate = text.get("0.0","end")
     x=text2.insert("end",GoogleTranslator(source=sou, target=trag).translate(text_To_translate))
     return x

app = ctk.CTk()                       #app is object from class CTK
app.geometry("600x600")               #Dimensions  
app.title("test")                     #name of app
ctk.set_appearance_mode("system")     #color mode screen
ctk.set_default_color_theme("blue")  #color mode button

# Entry language
ent = ctk.CTkEntry(app ,placeholder_text="source",height=30,width=200)
ent.place(x=50,y=100)
ent1 = ctk.CTkEntry(app ,placeholder_text="target",height=30,width=200)
ent1.place(x=350,y=100)

#button
bt1= ctk.CTkButton(app,text="Translate", width=100 ,height=50 ,hover_color="green",command=tra )
bt1.place(x=250, y=500)
# fram
fram= ctk.CTkFrame(app,width=200 , height= 300 )
fram.place(x=50, y=150)
fram= ctk.CTkFrame(app,width=200 , height= 300 )
fram.place(x=350, y=150)

# textbox
text= ctk.CTkTextbox(app , height=290, width=190)
text.place(x=55,y=155)

text2= ctk.CTkTextbox(app , height=290, width=190)
text2.place(x=355,y=155)

label= ctk.CTkLabel(app , text="Hello in my translator"  , font=("Perpetua Titling MT",12, "bold"))
label.place(x=200,y=50)

label= ctk.CTkLabel(app , text="Programming by Ammar Gamal"  , font=("Perpetua Titling MT",9, "bold"))
label.place(x=400,y=500)

app.mainloop()