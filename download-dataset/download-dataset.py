# Download dataset using wget

# Import libraries
from datetime import datetime
import os

# Parameters to be used with wget
username='nedc_tuh_eeg'
password='nedc_tuh_eeg'
webpage='https://www.isip.piconepress.com/projects/tuh_eeg/downloads/tuh_eeg_seizure/v1.5.0/'

# Create target directory with current date and time
folder_name=datetime.now().isoformat()
os.mkdir(folder_name)

# wget
wget_command='wget --user='+username+' --password='+password+' '+webpage
print(wget_command)
os.system(wget_command)
print('Folder \"'+folder_name+'\" created in path \"'+os.getcwd()+'\"')