import PySimpleGUI as sh
import os,time
import itertools
files=[]
list=[]
list1=[]

layout=[[sh.Text("FIle Explorer",text_color="blue",background_color="sky blue")],
        [sh.Text("Enter the Directory:",text_color="blue",background_color="sky blue"),sh.InputText("",key="direc"),sh.Text("Enter the type of file:",background_color="sky blue",text_color="blue"),sh.InputText("",size=(5,1),key="type")],
        [sh.Listbox("",size=(20,10),key="box2"),sh.Listbox("",key="box",size=(50,10)),sh.Listbox("",size=(20,10),key="box1")],
        [sh.Button("Submit"),sh.Button("Exit")]


        ]
window=sh.Window("FILE EXPLORER",layout,background_color="sky blue")


while True:


    button,value=window.Read()
    path = str(value["direc"])


    def file_size(file_path):
        for i in file_path:
            if os.path.isfile(i):
                file_info = os.path.getsize(i)
                modTimesinceEpoc = os.path.getmtime(i)

                # Convert seconds since epoch to readable timestamp
                modificationTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
            list.append(file_info)
            list1.append(modificationTime)

        #for i in list:
           # print(i)


    def bro():
        tope = str(value["type"])
        for r, d, f in os.walk(path):
            for file in f:

                if tope in file:
                    files.append(os.path.join(r, file))


    if button=="Submit":
        bro()
        file_size(files)
        window.FindElement("box").Update(files)
        window.FindElement("box1").Update(list)
        window.FindElement("box2").Update(list1)

    elif button=="Exit":
        break
