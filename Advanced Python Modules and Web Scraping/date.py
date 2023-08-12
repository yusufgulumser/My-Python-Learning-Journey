from datetime import datetime
noww= datetime.now()
result=datetime.now()
result=noww.now()
result=noww.year
result=noww.month
result=noww.hour
print(result)
############
result=datetime.ctime(noww)    # 'ctime' prints the current time more clearly
result=datetime.strftime(noww,'%Y')   # prints just year
result=datetime.strftime(noww,'%X')   # prints just time
result=datetime.strftime(noww,'%d')   # prints just day
print(result)
###########
result=datetime.timestamp(noww)        #shows the time with seconds
result=datetime.fromtimestamp(result)  # seconds to datetime
print(result)


##########
from datetime import timedelta

result= noww + timedelta(days=10)  #add 10 days to today
print(result)