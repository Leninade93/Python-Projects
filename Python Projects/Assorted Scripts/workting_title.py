import sys, subprocess

# idea would be to create a loop that runs through a directory sorting files into
# folders based on file type

# folders would need to be created based upon file extension. Need to check if that folder
# already exists so it isn't overwritten?



# a way to read in all file names and then search each slice of that list for extension. directory could be passed
# as a system argument to make code modular
files = subprocess.check_output(['ls', '/home/leninade/Downloads']).decode('utf-8').splitlines()
count = 1
for n in files:
    print(str(count) + ': ' + n)
    count += 1

    if '.jpg' in n:
        print ('image!')
    elif '.ttf' in n:
        print('font!')
    # so now we can parse those strings for specifi cfile types
    # how do we want to handle moving? probably in this loop 

# movement of those files into subsequent folders

# something like ls >> some type of storage. then mkdir $EXTENSION. mv OR cp $DIRECTORY


