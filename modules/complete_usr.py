import os

path = '/home/riya/usrproginst/modules/'
scripts=[
    f"{path}main_sent.py",
    f"{path}concept_row_mod.py",
    f"{path}indexing_module.py", 
    f"{path}sem_cat_module.py",
    f"{path}morpho_sem_module.py", 
    f"{path}dependency_module.py",
    f"{path}discourse_module.py",
    f"{path}spk_view_module.py", 
    f"{path}scope_module.py",
    f"{path}sent_type_module.py",
    f"{path}construction_module.py"
]

def run_script(script_name):
    try:
        command=f"python3 {script_name}"
        os.system(command)
    except Exception as e:
        print(f"Error running script: {e}")

for script in scripts:
    run_script(script)
