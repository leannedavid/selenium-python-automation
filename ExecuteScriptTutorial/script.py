import subprocess

# Subprocess library a library that allows our python scripts to interact with the CLI or shell
# Check call function executes an executable in terminal and waits for that processs to finish
for i in range (0, 5):
    subprocess.check_call(['python', 'test.py'])
