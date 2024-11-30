import os


scripts=[
    "/home/lc4eu/LC/usrproginst/modules/main_sent.py",
    "/home/lc4eu/LC/usrproginst/modules/concept_row_mod.py",
    "/home/lc4eu/LC/usrproginst/modules/indexing_module.py", 
    "/home/lc4eu/LC/usrproginst/modules/sem_cat_module.py",
    "/home/lc4eu/LC/usrproginst/modules/morpho_sem_module.py", 
    "/home/lc4eu/LC/usrproginst/modules/dependency_module.py",
    "/home/lc4eu/LC/usrproginst/modules/discourse_module.py",
    "/home/lc4eu/LC/usrproginst/modules/spk_view_module.py", 
    "/home/lc4eu/LC/usrproginst/modules/scope_module.py",
    "/home/lc4eu/LC/usrproginst/modules/sent_type_module.py",
    "/home/lc4eu/LC/usrproginst/modules/construction_module.py"
]

def run_script(script_name):
    try:
        command=f"python3 {script_name}"
        os.system(command)
    except Exception as e:
        print(f"Error running script: {e}")

for script in scripts:
    run_script(script)
