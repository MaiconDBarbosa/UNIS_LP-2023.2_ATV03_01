import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertendo altura para metros
        imc = peso / (altura ** 2)

        resultado = f"IMC: {imc:.2f} - {classificar_imc(imc)}"

        # Atualizando o rótulo de resultado
        label_resultado.config(text=resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")


def classificar_imc(imc):
    if imc < 16.00:
        return "Magreza Grau III"
    elif 16.00 <= imc < 16.99:
        return "Magreza Grau II"
    elif 17.00 <= imc < 18.49:
        return "Magreza Grau I"
    elif 18.50 <= imc < 24.99:
        return "Normal"
    elif 25.00 <= imc < 29.99:
        return "Sobrepeso"
    elif 30.00 <= imc < 34.99:
        return "Obesidade Grau I"
    elif 35.00 <= imc < 39.99:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"


def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    label_resultado.config(text="Resultado")


# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Criando os widgets
label_nome = tk.Label(root, text="Nome do Paciente:")
entry_nome = tk.Entry(root)

label_endereco = tk.Label(root, text="Endereço Completo:")
entry_endereco = tk.Entry(root)

label_altura = tk.Label(root, text="Altura (cm):")
entry_altura = tk.Entry(root)

label_peso = tk.Label(root, text="Peso (Kg):")
entry_peso = tk.Entry(root)

label_resultado = tk.Label(root, text="Resultado")

botao_calcular = tk.Button(root, text="Calcular", command=calcular_imc)
botao_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar)
botao_sair = tk.Button(root, text="Sair", command=root.destroy)

# Posicionando os widgets na grade
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_endereco.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

label_altura.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
entry_altura.grid(row=2, column=1, padx=10, pady=5)

label_peso.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
entry_peso.grid(row=3, column=1, padx=10, pady=5)

label_resultado.grid(row=4, column=0, columnspan=2, pady=10)

botao_calcular.grid(row=5, column=0, pady=10)
botao_reiniciar.grid(row=5, column=1, pady=10)
botao_sair.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciando o loop principal da interface gráfica
root.mainloop()
