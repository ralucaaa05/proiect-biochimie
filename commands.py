from docs import message
import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt


def list_comm(patient_data: pd.DataFrame, groups_dict: dict, arg):
    if arg == "COMMANDS":
        print(message)
    if arg == "PATIENTS":
        print(patient_data.index.values)
    if arg == "GROUPS":
        print([key for key in groups_dict.keys()])


def get_comm(patient_data: pd.DataFrame, groups_dict: dict, *args):
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    if args[0] == "PATIENT":
        patient_code = patient_data.loc[args[1].replace('"', "")]["Patient Code"]
        if len(args) == 2:
            for k, v in groups_dict.items():
                try:
                    print(f"Group: {k}\n {v.loc[patient_code]}")
                except KeyError:
                    pass
            return

        test_name = args[-1].replace('"', "")
        for test in test_set:
            if test_name in test:
                for k, v in groups_dict.items():
                    try:
                        print(f"Group: {k}\n {test}: {v.loc[patient_code][test]}")
                    except KeyError:
                        pass
        return
    if args[0] == "GROUP":
        group = args[1].replace('"', "")
        if group in groups_dict.keys():
            if len(args) == 2:
                print(groups_dict[group].std())
                return
            test_name = args[-1].replace('"', "")
            for test in test_set:
                    if test_name in test:    
                        print(f"{groups_dict[group][test]} \n Standard deviation: {groups_dict[group][test].std()}")
                        return

def set_comm(patient_data: pd.DataFrame, groups_dict: dict, *args):
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    patient_code = patient_data.loc[args[1].replace('"', "")]["Patient Code"]
    test_name = args[3].replace('"', "")
    
    for test in test_set:
        if test_name in test:
            for k, v in groups_dict.items():
                try:
                    tmp = args[1].replace('"', "")
                    print(f"The current value of {test} for {tmp} the {k} Group is: {v.loc[patient_code][test]}")
                    v.at[patient_code, test] = float(input(f"Enter the new value for {test}: "))
                    print(f"The new value of {test} for {tmp} the {k} Group is: {v.loc[patient_code][test]}")
                except KeyError:
                    pass



def add_comm(patient_data: pd.DataFrame, groups_dict: dict, *args):
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
    patient_data.append(pd.Series(new_data, name=patient_name))
    
    print("Please enter patient Analysis/test data:\n")
    test_data = {}
    for test in test_set:
        test_data[test] = input(f"{test}: ")
    group = input(f"\nIn which group should this patient be added? (available groups: {[k for k in groups_dict.keys()]})\n")

    try:
        groups_dict[group].append(pd.Series(test_data, name=patient_code))
    except KeyError:
        print(f"{group} is not a valid option")
        return
    
# NOTE: NOT TESTED!
def delete_comm(patient_data: pd.DataFrame, groups_dict: dict, *args):
    patient_name = args[1].replace('"', "")
    patient_code = patient_code = patient_data.loc[args[1].replace('"', "")]["Patient Code"]
    patient_data.drop(patient_name)
    for group in groups_dict.values():
        try:
            group.drop(patient_code)
        except KeyError:
            pass
    


def compare_comm(patient_data: pd.DataFrame, groups_dict: dict, *args):
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    group1 = groups_dict[args[1].replace('"',"")]
    group2 = groups_dict[args[3].replace('"',"")]
    
    ttest_results = pd.DataFrame({c: ttest_ind(group1[c], group2[c], equal_var=False) for c in test_set},
                    index=['statistic', 'pvalue'])
    
    print(ttest_results)


def plot_comm(patient_data: pd.DataFrame, groups_dict: dict, *args):
    test_name = args[-1].replace('"', "")
    
    test_set = set([x for column in groups_dict.values() for x in list(column.columns)])
    for test in test_set:
        if test_name in test:
            to_plot = pd.Series({k:group[test].std() for k, group in groups_dict.items()}, copy=False)
            print(to_plot)
            plot = to_plot.plot(kind="bar", title=f"Standard deviaton for {test_name}", ylabel=test.split()[-1])
            
            plt.show()
    pass
