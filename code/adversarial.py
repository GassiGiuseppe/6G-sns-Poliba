# THIS PYTHON FILE IS USED DURING TEST PHASE 
# its objective is append every x seconds a blob data ( incremental ),
# into the fake log file

from pathlib import Path
import time
import yaml

print('adversarial started with success')

# number of appends to execute
N = 30                                                                  

# log file path
file_path = yaml.safe_load(open(Path('code/settings.yml')))['log_file']
file_path = Path(file_path)     

for i in range(N):
    input_string = 'blablabla' + str(i)

    with open(file_path, 'a') as file:
        file.write(input_string + '\n')

    time.sleep(1)
