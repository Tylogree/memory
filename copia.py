import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
to = tk.Tk()
to.geometry('650x600')

fonte = 'Ubuntu mono'
tamanhe = 15

to.title('Novo Arquivo')
caraio = tk.Text(to, font=(fonte, tamanhe), height=100, width=100)
print(caraio['bg'])
caraio.pack(anchor='nw', fill='both')
scrollzao = tk.Scrollbar(to, orient='vertical', command=caraio.yview)

quilombo = ''

def abrirarq(event=None):
    try:
        jq = tk.filedialog.askopenfilename()
        quilombo = jq
        i = 0
        for line in open(jq):
            print(line)
            caraio.insert(f'{i}.0', line)
        a = jq.split('/')
        to.title(a[-1])
    except:
        messagebox.showerror('Erro', 'Arquivo não selecionado')

menuzin = tk.Menu(to)
submenuz = tk.Menu(to, tearoff=0)
sobre = tk.Menu(to)

def limpa(event=None):
    caraio.delete(1.0, 'end')
    to.title('Novo Arquivo')

def salvar(event=None):
    try:
        jq = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[
            ('Arquivos de Texto', '.txt'), ('Arquivos Python', '.py')])
        quilombo = jq.name
        sdd = str(caraio.get(1.0, 'end'))
        jq.write(sdd)
        to.title(jq)
        print(jq.name)
        coroso = jq.name.split('/')
        to.title(coroso[-1])
        o = jq
        jq.close()
        jq = o
    except:
        messagebox.showerror('Erro', f'Arquivo "{to.title()}" não foi salvo')

def salvounico(event=None):
    print(quilombo)
    if quilombo == '':
        salvar()
    else:
        mini = caraio.get(1.0, 'end')
        msa = str(mini)
        jq = open(quilombo, 'w')
        jq.write(msa)
        jq.close()
        messagebox.showinfo('Salvo', f'Arquivo "{to.title}" salvo com sucesso.')

def tab():
    caraio.insert(caraio.index('insert'), '   ')

los = 'br'

def t(tema, coisa, cor):
    if tema == 'ng':
        coisa['bg'] = cor
    else:
        pass

def tema(coisa, cor):
    print('s')

def temaixx():

    def negao():
        caraio['bg'] = '#01002b'
        caraio['fg'] = '#dbdbdb'
        caraio['insertbackground'] = '#dbdbdb'

    def brancao():
        caraio['bg'] = '#ffffff'
        caraio['fg'] = 'black'
        caraio['insertbackground'] = 'black'


    masaa = tk.Toplevel(to)
    masaa.geometry('200x150')
    colores = ['Branco', 'Negro']

    labu = tk.Label(masaa, text='Tema:', pady=5, padx=30)
    labu.pack()

    bumbum = ttk.Combobox(masaa, values=colores)
    bumbum.set('Selecione um tema')
    bumbum.pack()

    labus = tk.Label(masaa, text='Inserir fonte:', pady=5)
    labus.pack()

    entrada = tk.Entry(masaa)
    entrada.pack()

    def lucasegay():
        lucas = bumbum.get()
        if lucas == 'Branco':
            brancao()
        elif lucas == 'Negro':
            negao()
        else: pass

        if entrada.get() == '': pass
        else:
            try:
                caraio['font'] = entrada.get()
                tk.messagebox.showinfo('Fonte', f"Fonte alterada com sucesso para '{entrada.get()}'.")

            except:
                tk.messagebox.showerror('Erro', 'Nome da fonte incorreta')

    passos = tk.Button(masaa, text='Confirmar', command=lucasegay)
    passos.pack(fill='x', side='bottom')

def tamanco():
    cateto = tk.Toplevel(to)
    xcala = tk.Scale(cateto, from_=7, to=40, orient='horizontal')
    cas = tk.Label(cateto, text='Escolher tamanho da fonte:')
    cas.pack()
    xcala.pack()


    def aplicarss():
        hipotenusa = tk.Toplevel(cateto)
        sexaa = tk.Label(hipotenusa, text='A fonte ficará do seguinte tamanho:', pady=5)
        sesso = tk.Label(hipotenusa, text='Feito por\nMarco', font=(fonte, xcala.get()), pady=15)
        confirmm = tk.Label(hipotenusa, text='Deseja aplicar as alterações?')
        def posi():
            caraio['font'] = ('Ubuntu mono', xcala.get())
            messagebox.showinfo('Fonte', 'Fonte modificada com sucesso')
            hipotenusa.destroy()
            cateto.destroy()
        def nego():
            hipotenusa.destroy()
        simonao = tk.Button(hipotenusa, pady=15, text='Aplicar', padx=15, command=posi)
        naoosum = tk.Button(hipotenusa, pady=15, text='Voltar', padx=15, command=nego)
        sexaa.pack()
        sesso.pack()
        simonao.pack(side='right', anchor='s')
        naoosum.pack(side='left', anchor='s')
    bossal = tk.Button(cateto, text='Aplicar', command=aplicarss )
    bossal.pack(fill='x')

formatasa = tk.Menu(menuzin)

menuzin.add_cascade(label='Arquivo', menu=submenuz)
submenuz.add_command(label='Abrir', accelerator='Ctrl+O', command=abrirarq)
submenuz.add_command(label='Salvar Como', accelerator='Ctrl+Shift+S', command=salvar)
submenuz.add_command(label='Salvar', accelerator='Ctrl+S', command=salvounico)
submenuz.add_command(label='Novo', accelerator='Ctrl+N', command=limpa)
menuzin.add_cascade(label='Formatação', menu=formatasa)
formatasa.add_command(label='Tamanho da fonte', command=tamanco)
formatasa.add_command(label='Aparência', command=temaixx)
to.config(menu=menuzin)
to.bind_all('<Control-o>', abrirarq)
to.bind_all('<Control-n>', limpa)
to.bind_all('<Control-Shift-s>', salvar)
to.bind_all('<Control-s>', salvounico)
to.bind_all('<Tab>', tab)

def meter():
    caraio.insert(2.0, 'opa')

to.mainloop()