def clear():
    import os
    import  sys


    f_handler = open('out.log','w')
    oldstdout = sys.stdout
    sys.stdout = f_handler
    os.system("clear")

    sys.stdout=oldstdout

