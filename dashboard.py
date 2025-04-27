import customtkinter as ctk
from PIL import Image, ImageTk
root = ctk.CTk()
root.title("Telecom customers Dash board")  
root.geometry("1300x750")  

frame = ctk.CTkFrame(root, width=1300, height=750, fg_color="#7c7cbc")
frame.pack(fill="both", expand=True)
frame.pack_propagate(True)  
frame.pack()
header_label = ctk.CTkLabel(root, text="Subscriber Behavior Dashboard", font=("Arial", 22),text_color="#051a3e",bg_color='#c0c5cd'
)
header_label.place(x=15, y=10)
net_label = ctk.CTkLabel(frame, text="internet", font=("Arial", 12), text_color="#003366")
net_label.place(x=335, y=14) 

frame1 = ctk.CTkFrame(
    frame,
    width=300,
    height=400,
    fg_color="white",
    border_width=2,      
   border_color="#17171a" 
) 
corner_radius=20
frame1.place(x=1200, y=100)

net_label = ctk.CTkLabel(frame1, text="Total number of clients :       7043 ", font=("Arial", 18), text_color="#003366")
net_label.place(x=20, y=14) 


net_label = ctk.CTkLabel(frame1, text="Unsubscription rate :        ", font=("Arial", 18), text_color="#003366")
net_label.place(x=20, y=20) 








image_path = 'heatmap.png'  
image = Image.open(image_path)  

image = image.resize((450, 450))
photo = ImageTk.PhotoImage(image)

image_label = ctk.CTkLabel(frame, image=photo)
image_label.place(x=20, y=60)

image_path2 = 'lineplot.png'  
image = Image.open(image_path2)  

image = image.resize((500, 500))
photo = ImageTk.PhotoImage(image)

image_label = ctk.CTkLabel(frame, image=photo)
image_label.place(x=450, y=200)

image_path3 = 'pie.png'  
image = Image.open(image_path3)  

image = image.resize((450, 450))
photo = ImageTk.PhotoImage(image)

image_label = ctk.CTkLabel(frame, image=photo)
image_label.place(x=20, y=450)


models_button = ctk.CTkButton(
    frame,
    text="Models",
    font=("Arial", 16),
    text_color="white",
    fg_color="#003366",
    hover_color="#001f4d",
    corner_radius=8,
    width=120,
    height=40
)

models_button.place(x=1400, y=20)
def open_models():
    print("Models button clicked!")

models_button.configure(command=open_models)


root.mainloop()

