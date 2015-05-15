import time
from robobrowser import RoboBrowser
from datetime import datetime

"""FOR EDUCATION PURPOSE ONLY"""
'''This script will extract weather data from AccuWeather page. It will took about 15 sec (depends on your network).
Everything is stored into text file but you can easily paste contents to excel file'''

browser = RoboBrowser()

year = '2014' #year which you are interested. AccuWeather provide you only one year back

links =[ #here are stored urls with weather data
    
('http://www.accuweather.com/pl/pl/warsaw/274663/january-weather/274663?monyr=1/1/' + year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/february-weather/274663?monyr=2/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/march-weather/274663?monyr=3/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/april-weather/274663?monyr=4/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/may-weather/274663?monyr=5/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/june-weather/274663?monyr=6/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/july-weather/274663?monyr=7/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/august-weather/274663?monyr=8/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/september-weather/274663?monyr=9/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/october-weather/274663?monyr=10/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/november-weather/274663?monyr=11/1/'+ year +'&view=table'),
('http://www.accuweather.com/pl/pl/warsaw/274663/december-weather/274663?monyr=12/1/'+ year +'&view=table')
    ]


f = open(str(year)+'.txt', 'w')
f.write('Data\tTemp.Max.\tTemp.Min.\tOpady Deszczu\tOpady Sniegu\tŚr.wysokie\tŚr. niskie\n') # This is Polish version for english replace it with \
                                                                    # ('Date\tHigh.\tLow.\tRain\tSnow\tAvg. Hi\tAvg. Lo\n')
f.close()

for url in links:
    f = open(str(year)+'.txt', 'a') #creating file with year
    browser.open(url) #browser will open url
    days = browser.find_all('tr', {'class':'pre'})

    for item in days:
            f.write(item.find('th').text[-10:]+'\t')#date
            for c in item.find_all('td')[:1]:
                    f.write(item.find_all('td')[0].text+'\t')#temp
                    f.write(item.find_all('td')[1].text+'\t')#temp
                    f.write(item.find_all('td')[2].text+'\t')#rain
                    f.write(item.find_all('td')[3].text+'\t')#snow  #at 
                    f.write(item.find_all('td')[5].text+'\t')#Avg temp Hi.
                    f.write(item.find_all('td')[6].text+'\n')#Avg temo Lo.
    f.close()

print("DONE")

