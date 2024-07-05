import pandas as pd #
from commands import *
import os

group_dict = {}

commands_map = {
    "LIST": list_comm,
    "GET": get_comm,
    "SET": set_comm,
    "ADD": add_comm,
    "DELETE": delete_comm,
    "COMPARE": compare_comm,
    "PLOT": plot_comm,
}
# functia asta se ocupa de transformarea excelurilor in DataFrame si modificarea indexilor
def get_sheets():
    global patient_data
    sheets = os.listdir("data") # os.listdir iti creaza o lista cu fisierele din directorul/folderul "data"
    for name in sheets:
        if name.endswith(".xlsx"):
            if "codes" in name:
                patient_data = pd.read_excel(f"data/{name}").set_index("Name") # aici se creaza DataFrame pt excelul Pacient Codes si se seteaza indexul la coloana "Name"
            if "group" in name:
                group_dict[name.replace(".xlsx", "").replace("group", "").strip()] = pd.read_excel(f"data/{name}").set_index("Patient Code") # la fel ca mai sus

# functia asigura gasirea pacientului dupa nume si 
def input_parser(command: str):
    command = command.split() #.split iti creaza o lista cu fiecare string in parte, avand ca delimitator "backspace-ul"
    new_args = []
    tmp = ""
    for i in range(len(command)): # acest for face posibila cautarea pacientului dupa nume (ex: comanda .split ar fi despartit numele in ["John, Doe", "Alex, Garcia"], iar comenzile de mai jos iti despart corect numele => " ["John Doe","Alex Garcia"] "
        if command[i].startswith('"') and not command[i].endswith('"'):
            tmp += command[i] + " "
        elif command[i].endswith('"') and not command[i].startswith('"'):
            tmp += command[i]
            new_args.append(tmp)
            tmp = ""
        else:
            new_args.append(command[i])
    command_str_list = new_args    
    
    
    get_sheets()
    
    #
    if command_str_list[0] in commands_map.keys():
        commands_map[command_str_list[0]](patient_data, group_dict, *command_str_list[1:]) #if comm is "LIST" => list_comm(arg)
    else:
        print("Error! Command is not valid or there is a typo :)")

if __name__ == "__main__":
    input_parser(input("Please enter the command:"))