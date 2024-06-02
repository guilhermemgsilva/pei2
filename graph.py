from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure
from data import Deleted_Files 

# primary_color = "#272727"
# secondary_color = "#FFFFFF"
# line_color = "#3e3e93"

primary_color = "#fff"
secondary_color = "#000"
line_color = "#3e3e93"

deleted_files = Deleted_Files()
dados = dict(deleted_files.all_data())
fig = Figure(figsize=(0.5, 0.5), dpi=100, facecolor=primary_color, edgecolor=secondary_color)
ax = fig.add_subplot()



def number_of_data_to_show():
    return len(dados)

def sorted_datas():
    return dados

def define_number_of_showable_data(number_of_data):
    sorted_majors = {}
    majors = dict(list(dados.items())[-number_of_data:])

    for chave, valor in reversed(majors.items()):
        sorted_majors[chave] = valor
    
    return sorted_majors

def choose_graph(number_of_data=5):
    datas_to_graph = define_number_of_showable_data(number_of_data)
    dados_x = datas_to_graph.keys()
    dados_y = datas_to_graph.values()
    ax.clear()
    ax.bar(dados_x, dados_y, color=line_color)
    
    ax.set_facecolor(primary_color)
    ax.set_title(f'Arquivos deletados nos últimos {number_of_data} dias', color=secondary_color)
    ax.set_xlabel("Data de Execução", color=secondary_color)
    ax.set_ylabel("Número de arquivos deletados", color=secondary_color)
    
    ax.spines['bottom'].set_color(secondary_color)
    ax.spines['top'].set_color(secondary_color)
    ax.spines['left'].set_color(secondary_color)
    ax.spines['right'].set_color(secondary_color)
    ax.yaxis.set_tick_params(color=secondary_color,labelcolor=secondary_color)
    ax.xaxis.set_tick_params(color=secondary_color,labelcolor=secondary_color)    
    
    return fig
