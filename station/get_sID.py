import subprocess
import re

shell = subprocess.run(['hostname'],stdout=subprocess.PIPE)
result = str(shell.stdout)
sID = re.sub("[^0-9]", "", result)
print(sID)

