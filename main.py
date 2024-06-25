import pandas as pd
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


def get_sheets():
    global patient_data
    sheets = os.listdir("data")
    for name in sheets:
        if name.endswith(".xlsx"):
            if "codes" in name:
                patient_data = pd.read_excel(f"data/{name}").set_index("Name")
            if "group" in name:
                group_dict[name.replace(".xlsx", "").replace("group", "").strip()] = pd.read_excel(f"data/{name}").set_index("Patient Code")


def input_parser(command):
    command = command.split()
    new_args = []
    tmp = ""
    for i in range(len(command)):
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
    
    
    if command_str_list[0] in commands_map.keys():
        commands_map[command_str_list[0]](patient_data, group_dict, *command_str_list[1:]) #if comm is "LIST" => list_comm(arg)
    else:
        print("Error! Command is not valid or there is a typo :)")

if __name__ == "__main__":
    input_parser(input("gimme command:"))