import tkinter as tk

o = tk.Tk()

lb = tk.Label(o, text='Sexo edição 2', font=('Ubuntu', 50), bg='blue', fg='pink')
lb.pack(fill='y', pady=20)
bt = tk.Button(o, text='JOGAR!', font=('Ubuntu', 70), bg='red', fg='white')
bt.pack(fill='y', pady=20)
o['bg'] = 'pink'

o.mainloop()
