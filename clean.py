import glob
import re

for i in glob.glob("*/*/*.gt.txt"):
    with open(i, 'r') as f:
        data = f.read()
    
    data = re.sub(r'[\u000A\u001A\n]', "", data)
    
    with open(i, "w") as f:
        f.write(data)    

