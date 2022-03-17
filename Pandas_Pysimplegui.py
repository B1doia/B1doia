import PySimpleGUI as sg
import pandas as pd

sg.theme('Dark Amber')     #1- exibe caixa de mensagem para inicar a busca!
layout = [  [sg.Text("Clique em 'Ok' para escolher o arquivo!")],
                     [sg.Button('Ok')] ]
window = sg.Window('Window Title', layout)
event, values = window.read()
window.close()

if event or values == 1:
            #2- seleciona o arquivo!
    filename = sg.popup_get_file('Escolha o caminho do Arquivo!!' )
            #3- lê o arquivo no caminho escolhido acima!
    df = pd.read_excel(filename)
            #4- adiciona 100 espaços a direita de todos os dados da coluna 'Proprietário'
    df['Proprietário'] = df['Proprietário'] + " " * 100
            #5- salva em csv!
    #df.to_csv('G:/Publica/Lucas-vermelha/ARQUIVO_ESPAÇO/TESTANDOOOO.csv')
            #6- exibe o caminho que foi salvo!
    sg.popup('Arquivo Editado esta em:', 'G:/Publica/Lucas-vermelha/ARQUIVO_ESPAÇO/Arquivo_alterado.csv')
            #7- exibe a coluna editada!
    sg.popup('     Coluna que será editada com 100 espaços a direita!', df['Proprietário'])
else:
        layout = [  [sg.Text("BYE!!")],
                              ]
        window = sg.Window('Window Title', layout)
        event, values = window.read()
        window.close()
