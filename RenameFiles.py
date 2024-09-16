import os

#This script changes the file name of each pdf in a directory. Use this after a batchplot
#Place the file directory in the "directory" variable, and keep the lowercase "r" there
#Place the next rev numeber under "rev" variable

directory = r'C:\Users\Nikolas.Hayes\Desktop\FOR ISSUANCE\240087 P&IDs - Aug 14'
rev = "P2"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        if "Layout1" in f:
            if f.endswith('.pdf'):
                old_name = f
                f = f.split("-")
                new_name = (f[0] + "-" +f[1]+"-"+f[2]+" "+rev+".pdf")
                os.rename(old_name, new_name)
        else:
            print("use a fresh batch")
    