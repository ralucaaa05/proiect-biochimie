class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

message_backup = f"""{bcolors.OKGREEN}LIST COMMANDS{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Lists all available commands
{bcolors.OKGREEN}LIST PATIENTS{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Lists all available patients
{bcolors.OKGREEN}LIST GROUPS{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Lists all available patient groups
{bcolors.OKGREEN}GET PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Prints all analysis values of the selected patient
{bcolors.OKGREEN}GET PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKGREEN}ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"Analysis-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Prints the selected analysis value of the patient
{bcolors.OKGREEN}GET GROUP{bcolors.ENDC} {bcolors.OKCYAN}"Group-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Prints all available analysis values and stdevs of the group 
{bcolors.OKGREEN}SET PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKGREEN}ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"Analysis-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Replaces the analysis value of the selected patient
{bcolors.OKGREEN}ADD PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Adds a new patient with all the given analysis values
{bcolors.OKGREEN}DELETE PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Deletes the selected patient from the excel
{bcolors.OKGREEN}COMPARE GROUP1{bcolors.ENDC} {bcolors.OKCYAN}"Group_name"{bcolors.ENDC} {bcolors.OKGREEN}GROUP2{bcolors.ENDC} {bcolors.OKCYAN}"Group_name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} T-test between the 2 selected groups and prints the p-value
{bcolors.OKGREEN}PLOT ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"Analysis-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Plots a bar graph with the selected analysis values from the all available groups"""

message = f"""{bcolors.OKGREEN}LIST COMMANDS{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Lists all available commands
Example: LIST COMMANDS

{bcolors.OKGREEN}LIST PATIENTS{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Lists all available patients
Example: LIST PATIENTS

{bcolors.OKGREEN}LIST GROUPS{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Lists all available patient groups
Example: LIST GROUPS

{bcolors.OKGREEN}GET PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Prints all analysis values of the selected patient
Example: GET PATIENT {bcolors.OKCYAN}"John Doe"{bcolors.ENDC}

{bcolors.OKGREEN}GET PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKGREEN}ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"Analysis-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Prints the selected analysis value of the patient
Example: GET PATIENT {bcolors.OKCYAN}"John Doe"{bcolors.ENDC} {bcolors.OKGREEN}ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"HDL"{bcolors.ENDC}

{bcolors.OKGREEN}GET GROUP{bcolors.ENDC} {bcolors.OKCYAN}"Group-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Prints all available analysis values and stdevs of the group 
Example: GET GROUP {bcolors.OKCYAN}"Group A"{bcolors.ENDC}

{bcolors.OKGREEN}SET PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKGREEN}ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"Analysis-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Replaces the analysis value of the selected patient
Example: SET PATIENT {bcolors.OKCYAN}"John Doe"{bcolors.ENDC} {bcolors.OKGREEN}ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"HDL"{bcolors.ENDC}

{bcolors.OKGREEN}ADD PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Adds a new patient with all the given analysis values
Example: ADD PATIENT {bcolors.OKCYAN}"Jane Smith"{bcolors.ENDC}

{bcolors.OKGREEN}DELETE PATIENT{bcolors.ENDC} {bcolors.OKCYAN}"Patient-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Deletes the selected patient from the excel
Example: DELETE PATIENT {bcolors.OKCYAN}"John Doe"{bcolors.ENDC}

{bcolors.OKGREEN}COMPARE GROUP1{bcolors.ENDC} {bcolors.OKCYAN}"Group_name"{bcolors.ENDC} {bcolors.OKGREEN}GROUP2{bcolors.ENDC} {bcolors.OKCYAN}"Group_name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} T-test between the 2 selected groups and prints the p-value
Example: COMPARE GROUP1 {bcolors.OKCYAN}"Group A"{bcolors.ENDC} GROUP2 {bcolors.OKCYAN}"Group B"{bcolors.ENDC}

{bcolors.OKGREEN}PLOT ANALYSIS{bcolors.ENDC} {bcolors.OKCYAN}"Analysis-name"{bcolors.ENDC} {bcolors.OKBLUE}==>{bcolors.ENDC} Plots a bar graph with the selected analysis values from the all available groups
Example: PLOT ANALYSIS {bcolors.OKCYAN}"HDL"{bcolors.ENDC}"""
