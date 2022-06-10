# Import the following modules
import os
import time
import shutil
import datetime
import glob


# Change the directory and jump to the location
# where you want to arrange the files
os.chdir(r"/Volumes/Backup2/Photos/0Sort/2019Images4")
# List the directories and make a list
all_files = list(os.listdir())
outputs = os.getcwd()

# Run a loop for traversing through all the
# files in the current directory
for files in all_files:
    try:

        # Jump to the directories files
        inputs = glob.glob(files+"\\*")

        # Now again run a loop for traversing through
        # all the files inside the folder
        for ele in inputs:

            # Now, move the files one-by-one
            shutil.move(ele, outputs)

        # After extracting files from the folders,
        # delete that folder
        shutil.rmtree(files)
    except:
        pass

# Again run a loop for traversing through all the
# files in the current directory
for files in os.listdir('.'):

    # Get all the details of the file creation
    # and modification
    time_format = time.gmtime(os.path.getmtime(files))

    # Now, extract only the Year, Month, and Day
    datetime_object = datetime.datetime.strptime(str(time_format.tm_mon), "%m")

    # Provide the number and find the month
    full_month_number = datetime_object.strftime("%m")
    day = str(time_format.tm_mday)
    if len(day) == 1:
        day = '0' + day

    # Give the name of the folder
    dir_name = str(time_format.tm_year) + '.' + full_month_number + '.' + day + '.activity'
    print(dir_name)


    # Check if the folder exists or not
    if not os.path.isdir(dir_name):

        # If not then make the new folder
        os.mkdir(dir_name)
    dest = dir_name

    # Move all the files to their respective folders
    shutil.move(files, dest)

print("successfully moved...")
