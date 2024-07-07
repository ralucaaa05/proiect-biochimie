from docs import message
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt
# NOTE: test = analiza 


def list_comm(patient_data, groups_dict, arg): 
    """
     Functia listeaza diferite informatii în functie de argumentul `arg`:
    - "COMMANDS": Afiseaza un mesaj predefinit (care se gaseste in docs.py)
    - "PATIENTS": Deoarece patient_data e un DataFrame, .index.value iti listeaza/returneaza "valorile" din index.
    - "GROUPS": Afiseaza toate grupurile (cheile din `groups_dict`).
    """
    if arg == "COMMANDS":
        print(message)
    if arg == "PATIENTS":
        print(patient_data.index.values)
    if arg == "GROUPS":
        print([key for key in groups_dict.keys()])  

# 
def get_comm(patient_data, groups_dict: dict, *args):
    """ 
    Functia aceasta afiseaza datele pentru un pacient sau un grup specificat în `args`.
    - "PATIENT": Afiseaza datele pentru un pacient specificat.
    - "GROUP": Afiseaza deviatia standard pentru un grup specificat.
    """
    test_set = set([x for group in groups_dict.values() for x in list(group.columns)]) # Proprietatea .columns iti returneaza o lista cu denumirea coloanelor, mai putin a index ului (vezi in util varianta extinsa, fara list comprehension)
    if args[0] == "PATIENT":
        patient_code = patient_data.loc[args[1].replace('"', "")]["Patient Code"] # args[1] reprezinta numele pacientului; .loc returneaza "obiectul" corespondent randului din pacient_data; ["Pacient Code"] iti returneaza valoarea coloanei "Patient Code" din randul accesat anterior (.loc)
        if len(args) == 2:
            for k, v in groups_dict.items(): # k=key si v=value
                try:
                    print(f"Group: {k}\n {v.loc[patient_code]}")
                except KeyError: # Pentru a nu da eroare in cazul in care "Patient Code"-ul nu se gaseste in toate DataFrame 
                    pass
            return

        test_name = args[-1].replace('"', "") 
        for test in test_set:
            if test_name in test:
                for k, v in groups_dict.items():
                    try:
                        print(f"Group: {k}\n {test}: {v.loc[patient_code][test]}") # [patient_code][test]=[rand][coloana]
                    except KeyError:
                        pass
        return
    if args[0] == "GROUP":
        group = args[1].replace('"', "")
        if group in groups_dict.keys():
            if len(args) == 2:
                print(groups_dict[group].std()) # Datorita pandas, ai metoda .std() care iti calculeaza direct std-ul pe DataFrame ul ales
                return
            test_name = args[-1].replace('"', "")
            for test in test_set:
                    if test_name in test:    
                        print(f"{groups_dict[group][test]} \n Standard deviation: {groups_dict[group][test].std()}")
                        return

def set_comm(patient_data, groups_dict, *args):
    """    Functia actualizeaza valoarea unui test pentru un pacient specificat.
    """
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    patient_code = patient_data.loc[args[1].replace('"', "")]["Patient Code"]
    test_name = args[3].replace('"', "")
    
    for test in test_set:
        if test_name in test:
            for k, v in groups_dict.items():
                try:
                    patient_name = args[1].replace('"', "")
                    print(f"The current value of {test} for {patient_name} in the {k} Group is: {v.loc[patient_code][test]}")
                    v.at[patient_code, test] = float(input(f"Enter the new value for {test}: ")) # .at e proprietatea de a atribui
                    print(f"The new value of {test} for {patient_name} the {k} Group is: {v.loc[patient_code][test]}") # Confirmare ca s-a efectuat schimbarea valorii
                except KeyError:
                    pass



def add_comm(patient_data, groups_dict, *args):
    """ Functia adauga un nou pacient si datele aferente in `patient_data` si `groups_dict`.
    """
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    patient_name = args[1].replace('"', "")
    if patient_name in patient_data.index.values:
        print("Patient already in the database!")
        return
    new_data = {}
    patient_code = patient_data["Patient Code"].max() + len(patient_name)
    
    print("Please enter patient details:\n")
    for col in patient_data.columns.values:
        if col == "Patient Code":
            new_data[col] = patient_code
            continue
        new_data[col] = input(f"{col}: ")
    patient_data.append(pd.Series(new_data, name=patient_name)) # "name" este un parametru din pd.Series; name=patient_name odata apend uit devine index in DataFrame; Series devine astfel un nou rand in DataFrame
    
    print("Please enter patient Analysis/test data:\n")
    test_data = {}
    for test in test_set:
        test_data[test] = float(input(f"{test}: "))
    group = input(f"\nIn which group should this patient be added? (available groups: {[k for k in groups_dict.keys()]})\n")

    try:
        groups_dict[group].append(pd.Series(test_data, name=patient_code))
    except KeyError:
        print(f"{group} is not a valid option")
        return
    

def delete_comm(patient_data, groups_dict, *args):
    """    Functia iti sterge un pacient si datele aferente din `patient_data` si `groups_dict`.
"""
    patient_name = args[1].replace('"', "")
    patient_code = patient_data.loc[args[1].replace('"', "")]["Patient Code"]
    patient_data.drop(patient_name)
    for group in groups_dict.values():
        try:
            group.drop(patient_code)
        except KeyError:
            pass
    


def compare_comm(patient_data, groups_dict, *args):
    """     Functia iti compara două grupuri specificate în `args` folosind testul t.
"""
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    group1 = groups_dict[args[1].replace('"',"")]
    group2 = groups_dict[args[3].replace('"',"")]
    
    ttest_results = pd.DataFrame({c: ttest_ind(group1[c], group2[c], equal_var=False) for c in test_set},
                    index=['statistic', 'pvalue'])
    
    print(ttest_results)


def plot_comm(patient_data, groups_dict, *args):
    """     Plotează deviatia standard a unui test specificat pentru toate grupurile.
"""
    test_name = args[-1].replace('"', "")
    
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    for test in test_set:
        if test_name in test:
            to_plot = pd.Series({k:v[test].std() for k, v in groups_dict.items()}, copy=False)
            print(to_plot)
            plot = to_plot.plot(kind="bar", title=f"Standard deviaton for {test_name}", ylabel=test.split()[-1]) #  test.split()[-1] reprezinta unitatea de masura a analizei cerute :o
            
            plt.show()
    
