import datetime
def picoPlaca(checkDate,checkPlate,checkTime):
    constrainedPlates=[[1,2],[3,4],[5,6],[7,8],[9,0],[],[]] 
    lastDigit=int(checkPlate[-1]) 
    checkDate=checkDate.split('-')
    checkDate=datetime.date(int(checkDate[2]),int(checkDate[1]),int(checkDate[0]))
    dayOfWeek=checkDate.weekday()

    if lastDigit in constrainedPlates[dayOfWeek]:
        #definition of times to compare
        hour7=datetime.time(7) 
        hour9_30=datetime.time(9,30)
        hour16=datetime.time(16)
        hour19_30=datetime.time(19,30)

        checkTime=checkTime.split('-')
        checkTime=datetime.time(int(checkTime[0]),int(checkTime[1]))
        if checkTime>hour7 and checkTime<hour9_30:
            return "the car can't be on the road"
        elif checkTime>hour16 and checkTime<hour19_30:
            return "the car can't be on the road"
        else:
            return 'the car can be on the road'
    else:
        return 'the car can be on the road'
