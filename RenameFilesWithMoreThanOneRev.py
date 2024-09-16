#HOW TO USE:
#1. Two directories will be used: the 502 issued drawings folder for the project, and the folder containing
#your fresh batch plot. Paste in the address to each below. TBI_directory is for your new batch of drawings,
#and prev_issued_directory is for the project's 502 folder (flowsheets or P&ID folder) DO NOT USE THE TBI FOLDER 
#IN THE PROJECT ITSELF. THIS CONTAINS OTHER DISCIPLINE'S DRAWINGS THAT WE CAN NOT FIX IF SOMETHING GOES WRONG.

#2. When this script is started, it will ask a question about the rev title. Answer "p" if the drawings are 
#preliminary, and "r" if they have been stamped.

#3. This script only works if the drawings have already been issued. If they haven't, then you don't have 
#a previously issued directory, and can't fill out the second variable you need. Use the other script for an
#initial issuance. It's easier anyway.

#4. If the script prints out a list of drawing numbers, it means you need to review the name. Might be that the 
#drawing was in the previously issued folder but not in your to be issued folder.

import os

TBI_directory = r'C:\Users\Nikolas.Hayes\Desktop\Projects\240062 Bagdad Lime\PIDs for issuance Sep 4 2024'
prev_issued_directory = r'C:\Users\Nikolas.Hayes\Desktop\prev_issue'

TBI_dict = {}
prev_dict = {}
answer = input('Are these preliminary or revs? (p/r)').lower()
if answer == 'p':
    rev = " P"
elif answer == 'r':
    rev = " Rev "
else:
    print('Please answer with p or r')


#generate dictionary from the TBI directory
for f in os.listdir(TBI_directory):
    f = f.split('-')
    key = ''
    value = ''
    for part in f:
        if part != 'Layout1.pdf':
            key += part + '-'
        elif part == 'Layout1.pdf':
            value = 'Layout1'
    key = key[:-1]
    TBI_dict[key] = value


#generate dictionary from the prev_issued directory
for f in os.listdir(prev_issued_directory):
    f = f.split()
    value = f[1][:-4]
    value = value[1:]
    f = f[0].split('-')
    key = ''
    for part in f:
        key += part + '-'
    key = key[:-1]
    prev_dict[key] = value

#function to change value of TBI key to the next iteration of the rev
def change_value(key):
    TBI_dict[key] = rev + str((int(prev_dict[key]) + 1))
    return

#change TBI_dict values to the correct rev number
for key in TBI_dict:
    if key in prev_dict:
        change_value(key)
    else:
        TBI_dict[key] = (rev + '1')

#create empty list for files that need manual review
manual_review = []

for filename in os.listdir(TBI_directory):
    f = os.path.join(TBI_directory, filename)
    if os.path.isfile(f):
        old_name = f
        f = f.split('\\')
        fsplit = f[len(f) - 1]
        fsplit = fsplit.split('-')
        filekey = ''
        for part in fsplit:
            if part != 'Layout1.pdf':
                filekey += part + '-'
        filekey = filekey[:-1]
        new_name = filekey + str(TBI_dict[filekey]) +'.pdf'
        new_name_path = os.path.join(TBI_directory, new_name)
        try:
            os.rename(old_name, new_name_path)
        except FileNotFoundError as e:
            manual_review.append(new_name)

for key in prev_dict:
    if key not in TBI_dict:
        manual_review.append(key)

print('Please review the following files:')
print(manual_review)