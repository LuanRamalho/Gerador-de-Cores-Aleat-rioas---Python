import tkinter as tk
from tkinter import messagebox
import random

# Função para gerar uma cor aleatória em hexadecimal
def random_color():
    hex_chars = "0123456789abcdef"
    return "#" + ''.join(random.choice(hex_chars) for _ in range(6))

# Função para gerar o gradiente de cores
def generate_gradient():
    color_one = random_color()
    color_two = random_color()
    angle = random.randint(0, 360)
    gradient_code = f"background: linear-gradient({angle}deg, {color_one}, {color_two});"
    
    # Atualiza a interface com o gradiente e o código
    output_color.config(bg=color_one)
    output_code.config(state='normal')
    output_code.delete(0, tk.END)
    output_code.insert(0, gradient_code)
    output_code.config(state='readonly')

# Função para copiar o código para o clipboard
def copy_code():
    root.clipboard_clear()
    root.clipboard_append(output_code.get())
    messagebox.showinfo("Copied", "Code Copied To Clipboard")

# Criação da interface principal
root = tk.Tk()
root.title("Gradient Color Generator")
root.geometry("500x400")
root.config(bg="#f7f9fd")

# Estilo e estrutura dos elementos
wrapper = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
wrapper.place(relx=0.5, rely=0.5, anchor="center")

output_color = tk.Frame(wrapper, width=400, height=200, bg="#ffffff", relief="solid", bd=1)
output_color.pack(pady=10)

output_code = tk.Entry(wrapper, width=45, font=("Poppins", 10), state='readonly')
output_code.pack(pady=20)

btn_container = tk.Frame(wrapper, bg="#ffffff")
btn_container.pack(pady=10)

generate_btn = tk.Button(btn_container, text="Generate", command=generate_gradient, bg="#587ef4", fg="#ffffff",
                         font=("Poppins", 10), width=15, relief="raised")
generate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_container, text="Copy", command=copy_code, bg="#587ef4", fg="#ffffff",
                     font=("Poppins", 10), width=15, relief="raised")
copy_btn.grid(row=0, column=1, padx=10)

# Gerar um gradiente inicial ao abrir o programa
generate_gradient()

root.mainloop()
