import os

current_dir = os.listdir(os.getcwd())
get_extension = raw_input('enter file extension to rename ')
second_input = raw_input('1. replace entire name\n2. prepend name ')
desired_name = raw_input('enter desired name ')
counter = 0

if second_input == '1':    
    for thing in current_dir:
        if thing.endswith('.py'):
            continue
        if thing.endswith(get_extension) is False:
            continue
        extension = os.path.splitext(thing)[1]
        os.rename(thing, desired_name + "_" + str(counter) +  extension)
        counter += 1

if second_input is '2':
    for thing in current_dir:
        if thing.endswith('.py'):
            continue
        if thing.endswith(get_extension) is False:
            continue
        fname = os.path.splitext(thing)[0]
        extension = os.path.splitext(thing)[1]        
        os.rename(thing, desired_name + "@" + fname + extension)     
