from tkinter import *
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from numpy.random import normal
from PIL import ImageTk, Image
#from qbstyles import mpl_style
#mpl_style(dark=True)

model = load_model('generator_modelKaggle-17.h5')

output_data = []

def generaator():
    global output_data
    noise = normal(0, 1, (1, 100))
    output_data=(model.predict(noise))
    
    img = Image.fromarray(output_data[0, :, :, 0]*255)
    photo = ImageTk.PhotoImage(img)

    # Display the PhotoImage object in the output_image_label widget
    output_image_label.config(image=photo)
    output_image_label.image = photo
def display():
    try:  
        global output_data
        plt.style.use('dark_background')
        plt.axis('off')

        plt.get_current_fig_manager().window.iconbitmap("logo.ico")
        plt.get_current_fig_manager().set_window_title('GENERAATOR')

        plt.imshow(output_data[0, :, :, 0], cmap='gray')
        plt.show()
    except:
        generaator()
        display()

def salvesta():
    try:            
        global output_data
        img = Image.fromarray(output_data[0, :, :, 0]*255)
        img = img.convert('L')
        img.save('generated_image.png')
        print('aa')
    except:
        generaator()
        salvesta()
        
root=Tk()
root.title('Generaator')
root.geometry('350x400+700+250')
root['background']='#444444'
root.wm_iconbitmap('logo.ico')

# Btn
# fonts: OCR A Extended, Bauhaus 93, Miriam/+Fixed  Magneto
# Genereeri
button=Button(root, text='Generate', font=("OCR A Extended", 25),
              command=generaator, bg='#5fa99b', activebackground='#f7b025')
button.pack(pady=5)
# Kuva
button2=Button(root, text='Display', font=("OCR A Extended", 25),
               command=display, bg='#5fa99b', activebackground='#f7b025')
button2.pack(pady=5)
# Salvesta
button3=Button(root, text='Save', font=("OCR A Extended", 25),
               command=salvesta, bg='#5fa99b', activebackground='#f7b025')
button3.pack(pady=5)

output_image_label = Label(width=128, height=128)
output_image_label.config(bg="#444444")
output_image_label.pack()

root.mainloop()
