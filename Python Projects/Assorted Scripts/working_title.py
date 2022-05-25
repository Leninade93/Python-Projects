import sys, subprocess, os

## PURPOSED IDEAS: ######################################################################################################
# idea would be to create a loop that runs through a directory sorting files into
# folders based on file type

# folders would need to be created based upon file extension. Need to check if that folder
# already exists so it isn't overwritten?

# 4/25/22 Read in file types and create folders for each of those desginated file types. Compare that 
# already named directories to avoid overwriting exisitng directories.
# From there it should be just moving the files to their corresponding directories.
#########################################################################################################################

home_dir = os.getenv('HOME')
working_dir = home_dir + '/Downloads/Test Directory'
files = subprocess.check_output(['ls', working_dir]).decode('utf-8').splitlines()
 
def File_Type_Lookup():
    count = 1
    print('\nFiles detetected: ')
    for n in files:
        print(str(count) + ': ' + n, end =' || ')
        count += 1

        if ('.jpg' or '.png') in n:
            print ('Image')
        elif '.ttf' in n:
            print('Font')
        elif ('.mp4' or '.mp3') in n:
            print('Video')
        elif '.run' in n:
            print('Executable')
        elif '.docx' in n:
            print('Word Document')
        else:
            print('Undefined file type detected.')                                                                                                                                                                                                  


def Directory_Sort():
    shell_cmd = 'ls ' + working_dir + ' -l'
    files = subprocess.check_output(shell_cmd, shell = True).decode('utf-8').splitlines()
    
    count = 1
    directories = []
    print('\nDirectories detected: ')
    for n in files:
        if str(n[0]) == 'd':
            directories.append(n)
            print(str(count) + ': ' + n)
        else:
            continue
    

def case_test():
    count = 1
    for n in files:
        print(str(count) + ': ' + n, end = (' || '))
        ... # Seems to only have implmentation for python3.10 and above
            # https://docs.python.org/3.10/whatsnew/3.10.html#pep-634-structural-pattern-matching

# Run
File_Type_Lookup()
Directory_Sort()


