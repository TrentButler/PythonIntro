import os

current_dir = os.listdir(os.getcwd())
_input = raw_input('DESIRED NAME: ')
counter = 0

for thing in current_dir:
    if thing.endswith('.py'):
        continue
    extension = os.path.splitext(thing)[1]
    os.rename(thing, str(counter) + "_" +  _input + extension)
    counter += 1
    
print 'SUCCESS'