def oops():
    raise IndexError

def catch_oops():
    try:
        oops()
    except IndexError:
        print("Gotcha)")
    
catch_oops()
# Відповідь буде KeyError і програма не завершится.         