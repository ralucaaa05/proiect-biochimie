from docs import message
import pandas as pd

def list_comm(patient_data:pd.DataFrame,groups_dict:dict,arg):
    if arg == "COMMANDS":
        print(message)
    if arg == "PATIENTS":
        print(patient_data.index.values)
    if arg == "GROUPS":
        print([key for key in groups_dict.keys()])


def get_comm(patient_data:pd.DataFrame,groups_dict:dict,*args):
    new_args = []
    tmp = ""
    for i in range(len(args)):
        if args[i].startswith('"'):
            tmp += args[i] + " "
        elif args[i].endswith('"'):
            tmp += args[i]
            new_args.append(tmp)
            tmp = ""
        else:
            new_args.append(args[i])
    args = new_args
    if args[0] == "PATIENT":
        patient_code = patient_data.loc[args[1].replace('"',"")]["Patient Code"]
        if len(args) == 2:
            for k,v in groups_dict.items():
                try:
                    print(f"Group: {k}")
                    print(v.loc[patient_code])
                except:
                    pass
        
def set_comm():
    pass

def add_comm():
    pass

def delete_comm():
    pass

def compare_comm():
    pass

def plot_comm():
    pass
