import os

my_flag = os.getenv('MY_FLAG')
if my_flag and my_flag.lower() == 'true':
    print('Executing code...')
    print('hello jenkins!!!!')
else:
    print('Skipping code execution.')
    print('FEATURE FLAG VALUE PASSED WAS FALSE')
