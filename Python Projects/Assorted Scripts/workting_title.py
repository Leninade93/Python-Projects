import sys, subprocess, os

# idea would be to create a loop that runs through a directory sorting files into
# folders based on file type

# folders would need to be created based upon file extension. Need to check if that folder
# already exists so it isn't overwritten?



# a way to read in all file names and then search each slice of that list for extension. directory could be passed
# as a system argument to make code modular

home_dir = os.getenv('HOME')
working_dir = home_dir + '/Downloads'
files = subprocess.check_output(['ls', working_dir]).decode('utf-8').splitlines()
count = 1

# change this to a case block. 
for n in files:
    print(str(count) + ': ' + n, end=' || ')
    count += 1

    if '.jpg' in n:
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
    # so now we can parse those strings for specifi cfile types
    # how do we want to handle moving? probably in this loop 

# movement of those files into subsequent folders

# something like ls >> some type of storage. then mkdir $EXTENSION. mv OR cp $DIRECTORY


