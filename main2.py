import tkinter as tk

def draw_watermark(canvas):
    # Load the watermark image
    watermark_image = tk.PhotoImage(file="sarapuí.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=watermark_image)
    # Ensure the watermark image is garbage-collected
    canvas.watermark_image = watermark_image

janelaprincipal = tk.Tk()
janelaprincipal.title("Projeto Pedala Sarapuí")
janelaprincipal.geometry("340x480")
janelaprincipal.configure(bg="white")

# Create a canvas widget covering the entire window
canvas = tk.Canvas(janelaprincipal, width=340, height=480, bg="white", highlightthickness=0)
canvas.pack()

# Draw the watermark on the canvas
draw_watermark(canvas)

# Rest of your code...
# (Including labels, buttons, and other widgets)

janelaprincipal.mainloop()
