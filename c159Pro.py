from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.title("Country Flags")
root.geometry("800x800")
root.configure(background="cyan")
input_box=Entry(root)
label_show=Label(root)

india_map=ImageTk.PhotoImage(Image.open("india.png"))
america_map=ImageTk.PhotoImage(Image.open("america.jpg"))
canada_map=ImageTk.PhotoImage(Image.open("canada.jpg"))

map_dictionary={"india":india_map,"america":america_map,"canada":canada_map}
def ShowFlags():
    try:
        get_country_name=input_box.get()
        print(get_country_name)
        label_show['image']=map_dictionary[get_country_name]
    except:
        messagebox.showinfo("Error","Sorry, this country flag is not present in our system")
    



btn=Button(root,text="Show Country Flag",bg="black",fg="white",command=ShowFlags)
input_box.place(relx=0.5,rely=0.2,anchor=CENTER)
label_show.place(relx=0.5,rely=0.6,anchor=CENTER)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()

