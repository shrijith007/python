from typing import List, Any

import PySimpleGUI as sg
import file

lis = []
completed = []
lis = file.readFile()
completed = file.readCompleted()
layout = [[sg.Text("TODO LIST")],[sg.Text("New Entry : "),sg.InputText("",key = "entry")],
          [sg.Listbox(values=lis,key = "list",size=(40,6), enable_events=True), sg.Listbox(values=completed,key = "complete",size=(40,6), enable_events=True)],
          [sg.CalendarButton("Choose Date", target="dateDisp", key='date',button_color =("red","white")),sg.InputText("",key = "dateDisp", disabled=True ,do_not_clear=False)],
          [sg.Slider(range=(5,1,-1),default_value=5,orientation="horizontal",key="priority")],
          [sg.Button("add",button_color =("red","white") ),sg.Button("delete",button_color =("red","white")),sg.Button("prioritize",button_color =("red","white")),sg.Button("completed",button_color =("red","white")),sg.Exit()],
          [sg.Text("", auto_size_text=False, key="tell")]]

window = sg.Window("my first GUI ", layout)

while True:
    event, entries = window.Read()
    print(event, entries)
    if event is None or event == "Exit":
        break

    elif (event == "add"):
        if(entries["dateDisp"] == ""):
            window.Element("tell").Update("Please input a date")
            continue

        x = entries["entry"]+" "+entries["dateDisp"]+" "+str(int(entries["priority"]))
        lis.append(x)
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item added")
        file.writeToFile(lis) #working

    elif( event == "delete"):
        lis.remove(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("item deleted")
        file.writeToFile(lis) #working

    elif( event == "prioritize"):
        for i in range(len(lis)):
            min = i
            for j in range(i+1, len(lis)):
                if(lis[min][-1] > lis[j][-1]):
                    min = j
            lis[i],lis[min] = lis[min],lis[i]
        window.FindElement("list").Update(lis)
        window.Element("tell").Update("prioritized")
        file.writeToFile(lis) #working

    elif( event == "completed"):
        lis.remove(''.join(entries["list"]))
        completed.append(''.join(entries["list"]))
        window.FindElement("list").Update(lis)
        window.FindElement("complete").Update(completed)
        window.Element("tell").Update("item completed")
        file.writeToCompleted(completed) #working



window.Close()