# Download dataset using wget

# Parameters to be used with wget
username=''
password=''
webpage='https://www.isip.piconepress.com/projects/tuh_eeg/downloads/tuh_eeg_seizure/v1.5.0/'

# Import libraries
from datetime import datetime
import os

# Create target directory with current date and time
folder_name=datetime.now().isoformat()
os.mkdir(folder_name)
os.chdir(folder_name)

# wget
wget_command='wget --recursive --level=0 --no-parent --reject "index.html*" --user='+username+' --password='+password+' '+webpage
os.system(wget_command)
print('\n')
print('Folder \"'+folder_name+'\" created in path \"'+os.getcwd()+'\"')
