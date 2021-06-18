import os
import csv
dir_info_list = []

path = input('Please enter directory path: ')
for root, dirs, files in os.walk(path):
    for file in files:
        if 'PtTrace.TXT' not in file and 'Debug.TXT' not in file:
            dir_info_list.append(os.path.join(root,file))

with open('directory_info.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['File Path'])
    for item in dir_info_list:
        writer.writerow([item])
print('CSV with directory info has been placed in folder that contains .py file')


