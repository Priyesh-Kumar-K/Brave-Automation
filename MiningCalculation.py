# monthlyInvest = 30000
# monthlyReturnPercent = 10
gpuCount = 0
noOfMonths = 36
balance=0
totalReturn =0

for i in range(0,noOfMonths):
    gpuCount+=1
    monthlyReturn=gpuCount*3000
    totalReturn = totalReturn + monthlyReturn + balance
    if(totalReturn>=30000):
        balance=totalReturn%30000
        totalReturn/=30000
        gpuCount+=int(totalReturn)
        totalReturn=0
    print("GPU Count : ",gpuCount)
    print("Monthly Return on month ", i+1," : " ,monthlyReturn)
    print("Balance : ", balance)