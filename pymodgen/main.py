# This is a simple mod generator for Star Wars Empire at War: Forces of Corruption
# that will speed up the process of creating mods.

import os, sys
import argparse
 
# error messages
INVALID_NAME_MSG = "Invalid mod name! Make sure there are no spaces in the name. Please try again."

mod_structure = [
    '{mod_name}\\Data',
    '{mod_name}\\Data\\Art',
    '{mod_name}\\Data\\Art\\Models',
    '{mod_name}\\Data\\Art\\Textures',
    '{mod_name}\\Data\\Scripts',
    '{mod_name}\\Data\\Scripts\\AI',
    '{mod_name}\\Data\\Scripts\\FreeStore',
    '{mod_name}\\Data\\Scripts\\GameObject',
    '{mod_name}\\Data\\Scripts\\Library',
    '{mod_name}\\Data\\Scripts\\Miscellaneous',
    '{mod_name}\\Data\\Scripts\\Story',
    '{mod_name}\\Data\\Text',
    '{mod_name}\\Data\\XML',
]

def create_mod(mod_name):
    os.mkdir(mod_name)
    for dirs in mod_structure:
        os.makedirs(dirs.format(mod_name=mod_name), exist_ok=True)

def validate_modname(mod_name):
    '''
    checks if the mod name is valid
    '''
    if " " in mod_name:
        print(INVALID_NAME_MSG)
        sys.exit(1)
    

def main():
    parser = argparse.ArgumentParser(prog="modgen", usage="%(prog)s [options]", description="a mod generator for Star Wars Empire at War: Forces of Corruption")
    parser.add_argument("-n", "--name", type=str, help="the name of the mod you want to generate")

    args = parser.parse_args()

    if args.name:
        validate_modname(args.name)
        create_mod(args.name)
        print("Mod created successfully!")
    else:
        parser.print_help()
        sys.exit(1)
    

if __name__ == "__main__":
    main()
