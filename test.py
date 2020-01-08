import random
import picoPlaca
import string

for k in range(0,100):
    date= str(random.randint(1,28))+'-'+str(random.randint(1,12))+'-'+str(random.randint(2015,2025))
    plate=random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.digits)+random.choice(string.digits)+random.choice(string.digits)
    time= str(random.randint(0,23))+'-'+str(random.randint(0,59))

    print('with plate:'+plate+' on date:'+date +' at time:'+time +' '+ picoPlaca.picoPlaca(date,plate,time)  )