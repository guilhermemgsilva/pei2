import graph
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import tkinter as tk
# from tkinter import ttk 
from tkinter import ttk

window = tk.Tk()
window.title('Dashboard de Arquivos Deletados')
window.geometry('1200x550')
window.iconbitmap('./icone.ico')

#theme
window.tk.call('source', './Azure/azure.tcl')
window.tk.call("set_theme", "light")

#variables
number_of_data_configured = tk.IntVar(value=5)
graph_types = ('bar')
kind_of_graph = tk.StringVar(value=graph_types[0])

#frame principal divido em dois a parte do gráfico e configurações e a parte da tabela e informações
main_frame = ttk.Frame(window)
main_frame.rowconfigure(0, weight=1)
main_frame.columnconfigure((0), weight=6)
main_frame.columnconfigure((1), weight=1)


#frame de configurações que ficerá acima do gráfico
left_side_frame = ttk.Frame(main_frame)
left_side_frame.rowconfigure(0,weight=1)
left_side_frame.rowconfigure(1,weight=5)
left_side_frame.columnconfigure(0, weight=1)

#posicionamento do left side
left_side_frame.grid(row=0, column=0, sticky='nswe')

#frame de configuarações do gráfico

configurations_frame = ttk.Frame(left_side_frame)
configurations_frame.rowconfigure((0,1,2), weight=1)

configurations_frame.columnconfigure(0, weight=1)

#posicionamento da label de escolha
#selection para selcionar o tipo de gráfico
select_graph_type_label = ttk.Label(configurations_frame, text="")
select_graph_type_label.grid(row=0, column=0,sticky='nswe', padx=20)


#label de instrução do slider
select_graph_number_label = ttk.Label(configurations_frame, text="Escolha o número dias que deseja vizualizar",font=('Cascadia Code',16), foreground="#8c8c8c")
select_graph_number_label.grid(row=1, column=0,sticky='nswe', padx=20)
#posicionamento do slider
number_of_selected = ttk.Scale(configurations_frame, 
                               from_ = 1, 
                               to=graph.number_of_data_to_show(),
                               variable=number_of_data_configured,
                               )
number_of_selected.grid(row=2, column=0,sticky='we', padx=10) 

configurations_frame.grid(row=0,column=0,sticky='nswe')

#Posicionamento do gráfico


updated_graph = graph.choose_graph(number_of_data_configured.get())

canvas = FigureCanvasTkAgg(updated_graph, master=left_side_frame)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, sticky='nswe', pady=10, padx=10)



def update_graph():
    data = number_of_data_configured.get()
    updated_graph = graph.choose_graph(data)  
    
    canvas.draw()

number_of_selected.config(command=lambda value : update_graph())


#frame do right side onde ficará a tabela de informações
right_side = ttk.Frame(main_frame)
right_side.rowconfigure(0,weight=1)
right_side.columnconfigure(0,weight=1)


#posicionamento da tabela de informações



table = ttk.Treeview(right_side, columns=("date", "deletados"),show='headings') 
table.heading("date", text="Data de Execução")
table.heading('deletados', text="Número de Arquivos Deletados")
table.grid(row=0, column=0, sticky='nswe',padx=10, pady=10)

for chave, valor in (graph.sorted_datas().items()):
    data = (chave, valor)
    table.insert('', index= 0, values=data)

right_side.grid(row=0, column=1, sticky='nswe')

#posicionametno do main frame no window
main_frame.pack(expand=True, fill='both')

window.mainloop()
