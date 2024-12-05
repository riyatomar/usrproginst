import os
from set_path import PATH

scripts=[
    f"{PATH}/modules/main_sent.py",
    f"{PATH}/modules/concept_row_mod.py",
    f"{PATH}/modules/indexing_module.py", 
    f"{PATH}/modules/sem_cat_module.py",
    f"{PATH}/modules/morpho_sem_module.py", 
    f"{PATH}/modules/dependency_module.py",
    f"{PATH}/modules/discourse_module.py",
    f"{PATH}/modules/spk_view_module.py", 
    f"{PATH}/modules/scope_module.py",
    f"{PATH}/modules/sent_type_module.py",
    f"{PATH}/modules/construction_module.py"
]

def run_script(script_name):
    try:
        command=f"python3 {script_name}"
        os.system(command)
    except Exception as e:
        print(f"Error running script: {e}")

for script in scripts:
    run_script(script)
