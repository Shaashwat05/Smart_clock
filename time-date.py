from datetime import datetime



def dt():

    # datetime object containing current date and time
    now = datetime.now()
    print(type(now))
    # dd/mm/YY H:M:S
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    print("date and time =", time)	


dt()