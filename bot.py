import requests
import json
import time
import math

api_url="https://api.iex.cloud/v1/fx/latest?symbols=USDEUR,USDJPY,USDGBP,USDCNH,USDAUD,USDCAD,USDCHF,USDHKD,USDNZD,EURUSD,EURJPY,EURGBP,EURCNH,EURAUD,EURCAD,EURCHF,EURHKD,EURNZD,JPYGBP,JPYCNH,JPYAUD,JPYCAD,JPYCHF,JPYHKD,JPYNZD,JPYUSD,GBPCNH,GBPAUD,GBPCAD,GBPCHF,GBPHKD,GBPNZD,GBPUSD,CNHAUD,CNHCAD,CNHCHF,CNHHKD,CNHNZD,CNHUSD,AUDCAD,AUDCHF,AUDHKD,AUDNZD,AUDUSD,CADCHF,CADHKD,CADNZD,CADUSD,CHFHKD,CHFNZD,CHFUSD,HKDNZD&token=pk_445fd1f161ba4718ada8b1186513e820"
response=requests.get(api_url).json()
base_currency=[]
quote_currency=[]
log_currency=[]
rate=[]
logs=[]

print("Base      Quote    Rate")

    
for i in response:
    base_currency.append(i['symbol'][:3])
    #log_currency.append(math.log(i['rate']))
    quote_currency.append(i['symbol'][3:])
    rate.append(i['rate'])
    logs.append(math.log(i['rate']))
for k in range(len(rate)):
    print(base_currency[k]+"       "+quote_currency[k]+"      "+str(rate[k]))
        
#when investing in pairs, first ticker (base) is what you are investing in appreciating or becoming stronger
#e.g. If I invest in CADUSD, I want the rate to appreciate via the CAD becoming stronger and/or USD becoming weaker

#ex=rate[0]
#a=0
#index=0
#for j in range(len(rate)):
#    if quote_currency[a]==base_currency[j]:
#        for n in range(9):
#            if quote_currency[n]==quote_currency[j]:
#                if ex*rate[j]>rate[n]:
#                    ex=ex*rate[j]
#                    print(base_currency[j]+quote_currency[j])
        
            
        
        #if ex*rate[j]
        #ex=ex*rate[j]
#        a=j
#print("USD"+quote_currency[a])
#print(ex)
#growth=0
#for z in range(9):
#    if quote_currency[a]==quote_currency[z]:
#        growth=(ex/rate[z])*100
#print(str(growth)+"%")



cycles=[]
path=[]




def findCycles(start,c):
    
    path=[]
    indicator=start
    path.append(base_currency[start]+quote_currency[start])
    #for z in range(len(rate)):
        #if base_currency[z]==quote_currency[indicator]:
            
    for k in range(len(rate)-1):
        if base_currency[k]==quote_currency[indicator]:
            if len(path)==1 and base_currency[k]==base_currency[k+1]:
                path.append(base_currency[k]+quote_currency[k+c])
                indicator=k+c
            elif len(path)<5:
                    
                path.append(base_currency[k]+quote_currency[k])
                
                indicator=k
            elif len(path)==5:
                path.append(quote_currency[indicator]+base_currency[start])
    if path not in cycles and len(path)==6:
        cycles.append(path)
    #elif path in cycles:  
     #   findCycles(start,1)
    start=+1
    
    
   

for i in range(9):
    for x in range(3):
        findCycles(i,x)
print(cycles)



for k in range(len(cycles)):
    summation=0
    ex=1
    for z in range(6):
        for i in response:
            if cycles[k][z]==i['symbol']:
                summation+=math.log(i['rate'])
                ex=ex*i['rate']
                #print(cycles[k][z]+": "+str(i['rate']))
    if summation>0:
        print(str(cycles[k])+" has returned a "+str((ex*100)-100)+"% return")
        #print(str((ex*100)-100)+"%")
    
    

            


    
