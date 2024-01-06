import os


scripts=[
    "run_script.py",
    "indexing_module.py", 
    "sem_cat_module.py",
    "morpho_sem_module.py", 
    "dependency_module.py",
    "discourse_module.py",
    "spk_view_module.py", 
    "scope_module.py",
    "sent_type_module.py",
    "construction_module.py"
]

def run_script(script_name):
    try:
        command=f"python3 {script_name}"
        os.system(command)
    except Exception as e:
        print(f"Error running script: {e}")

for script in scripts:
    run_script(script)
