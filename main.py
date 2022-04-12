import tkinter as tk
import random
import smtplib
from email.message import EmailMessage
from tkinter import Toplevel
from tkinter import messagebox
import webbrowser


import segredos

# Ideia do programa:
# 1: Ter login e senha.
# 2: Fazer upload de determinados arquivos.
# 3: Mandar esses arquivos em uma determinada data.

# Configurando a janela inicial de login

janela = tk.Tk()
janela.title('Feito por Marco Túlio')
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=4)
janela.geometry('300x180')

# Término da configuração da janela inicial



# Configuração e posicionamento de Widgets

menuzin = tk.Menu(janela)
submenuz = tk.Menu(menuzin)
sobre = tk.Menu(menuzin)

menuzin.add_cascade(label='Ajuda', menu=submenuz)
submenuz.add_command(label='Cadastrar', command=lambda: cadastro())
submenuz.add_command(label='Sair', command=lambda: quit())
menuzin.add_cascade(label='Sobre', menu=sobre)
sobre.add_command(label='Github', command=lambda: webbrowser.open('https://github.com/Tylogree/memory') )

janela.config(menu=menuzin)


label_email = tk.Label(janela, text='E-mail:')
label_email.grid(row=1, column=1, ipady=20)

label_senha = tk.Label(janela, text='Senha:')
label_senha.grid(row=2, column=1)

entry_email = tk.Entry(width=25)
entry_email.grid(row=1, column=2, pady=20)

entry_senha = tk.Entry(show='*', width=25)
entry_senha.grid(row=2, column=2, pady=5, padx=5)

# Término da criação e posicionamento de Widgets



# Função para verificar se o e-mail e a senha estão corretos

def funcao_botao():
    email = entry_email.get()
    senha = entry_senha.get()
    logado = False
    for line in open('data.txt'):
        spl = line.split(';;')
        spl[1] = spl[1].replace('\n', '')
        print(spl)
        if spl[0] == email and spl[1] == senha:
            print('Baita achado!')
            tk.messagebox.showinfo('Login', f'Logado com sucesso como {email}')
            logado = True

        else: print('Mais uma linha sem nada...')

    if logado != True:
        tk.messagebox.showerror('Erro', 'Login ou senha incorretos')

# Término da função de verificação de e-mail e senha



# Função para analisar se o endereço de e-mail é válido

def em(email):
    for line in open('data.txt'):
        linesa = line.split(';;')
        if linesa[0] == email:
            messagebox.showwarning('Erro', 'Esse e-mail já está registrado.')
            return False
        else:
            return True

# Término da função de verificação de e-mail válido



# Função para analisar se duas variáveis são iguais

def ig(a, b):
    if a == b: return True
    else:
        tk.messagebox.showerror('Erro', 'As senhas não coincidem')
        return False

# Término da função para ver se duas variáveis são iguais



# Função para abrir a janela de cadastro

def cadastro():
    # cad = janela de cadastro (email, senha, confirmação de senha)
    # Configuração da janela de cadastro cad

    cad = tk.Toplevel()
    cad.columnconfigure(0, weight=1)
    cad.columnconfigure(1, weight=2)

    # Término da configuração da janela cad



    # Criação e posicionamento de Widgets na janela cad

    eml = tk.Label(cad, text='Endereço de e-mail:')
    eml.grid(row=1, column=1, padx=5, pady=5)

    se1l = tk.Label(cad, text='Senha da conta:')
    se1l.grid(row=2, column=1, padx=5, pady=5)

    se2l = tk.Label(cad, text='Confirmar senha:')
    se2l.grid(row=3, column=1, padx=5, pady=5)

    eme = tk.Entry(cad)
    eme.grid(row=1, column=2, padx=5, pady=5)

    se1e = tk.Entry(cad)
    se1e.grid(row=2, column=2, padx=5, pady=5)

    se2e = tk.Entry(cad)
    se2e.grid(row=3, column=2, padx=5, pady=5)

    def volt():
        cad.destroy()

    voltar = tk.Button(cad, text='< Voltar', command=volt )
    voltar.grid(row=4, column=1, padx=10, pady=10)
    # Término do posicionamento de widgets na janela cad



    # Começo da função para verificar o e-mail

    def cadcon():
        if em(eme.get()) == True and ig(se1e.get(), se2e.get()) == True:

            # Mandando o e-mail

            codigo = random.randint(10000000, 99999999)
            msg = EmailMessage()
            msg['Subject'] = 'Confirmação de Conta'
            msg['From'] = segredos.email
            msg['To'] = eme.get()
            msg.set_content(f'Olá, seu token de verificação é: {str(codigo)}')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(segredos.email, segredos.senha)
                smtp.send_message(msg)


            # kalango = janela de verificação do e-mail (token)
            # Configuração da janela kalango

            kalango = tk.Toplevel()
            kalango.columnconfigure(0, weight=1)
            kalango.columnconfigure(1, weight=3)

            # Término da configuração da janela kalango



            # Criação e posicionamento de widgets na janela kalango

            mensa = tk.Label(kalango, text=f'O token de verificação foi mandado\npara {eme.get()}')
            mensa.grid(row=1, column=2, padx=5, pady=5)
            confe = tk.Label(kalango, text='Token de confirmação da conta:')
            confe.grid(row=2, column=1, padx=10, pady=10)
            eks = tk.Entry(kalango)
            eks.grid(row=2, column=2, padx=10, pady=10)

            # Término da criação e posicionamento de widgets na janela kalango



            # Função para verificação de token de e-mail e escritura do login no banco de dados
            # (É uma função sendo declarada dentro de outra função)

            def confir():
                if str(codigo) == eks.get():
                    oq = open('data.txt', 'a')
                    oq.write(f'{eme.get()};;{se1e.get()}\n')
                    oq.close()
                    tk.messagebox.showinfo(f'Conta confirmada', f'Sua conta de email {eme} foi criada')
                    kalango.destroy()
                    cad.destroy()

                else:
                    tk.messagebox.showerror('Erro', 'Token de confirmação incorreto')

            botaodecon = tk.Button(kalango, text='Confirmar conta', command=confir )
            botaodecon.grid(row=3, column=2, padx=10, pady=10)

        else:
            tk.messagebox.showerror('Erro', 'Algo deu errado')


    confirmbt = tk.Button(cad, text='Confirmar cadastro', command=cadcon )
    confirmbt.grid(row=4, column=2, pady=10, padx=10)


botao_verificar = tk.Button(janela, text='Verificar', command=funcao_botao )
botao_verificar.grid(row=3, column=2, padx=10, pady=20)

janela.mainloop()