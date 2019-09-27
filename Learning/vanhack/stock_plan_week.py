def openAndClosePrices(firstDate, lastDate, weekDay):
    from datetime import datetime, timedelta
    import re
    import requests
    d = {}
    d['Monday'] = 0
    d['Tuesday'] = 1
    d['Wednesday'] = 2
    d['Thursday'] = 3
    d['Friday'] = 4
    d['Saturday'] = 5
    d['Sunday'] = 6
    # weekDay = 'Monday'
    d1 = datetime.strptime(str(firstDate), '%d-%B-%Y').date()
    d2 = datetime.strptime(str(lastDate), '%d-%B-%Y').date()

    weekday = d[weekDay]
    days_ahead = weekday - d1.weekday()

    if days_ahead <= 0:
        days_ahead += 7
    d1 = d1 + timedelta(days_ahead)

    delta = abs(d2 - d1)  # timedelta
    li = []
    result = []
    result1 = []
    result2 = []
    p = requests.get('https://jsonmock.hackerrank.com/api/stocks/').json()
    for i in range(len(p['data'])):
        for j in range(0, delta.days + 1, 7):
            dt = datetime.strptime(str(d1 + timedelta(j)), '%Y-%m-%d')
            li.append(dt.strftime('%d-%B-%Y'))
            s = p['data'][i]['date']
            if len(re.sub(r'-.*', '', s)) < 2:
                if dt.strftime('%d-%B-%Y') == '0' + p['data'][i]['date']:
                    result.append(p['data'][i]['date'])
                    result1.append(p['data'][i]['open'])
                    result2.append(p['data'][i]['close'])
            if dt.strftime('%d-%B-%Y') == p['data'][i]['date']:
                result.append(p['data'][i]['date'])
                result1.append(p['data'][i]['open'])
                result2.append(p['data'][i]['close'])


    # print(dt.strftime('%d-%B-%Y'))


    # for i in range(len(p['data'])):
    #     l2.append(datetime.strptime(str(p['data'][i]['date']), '%Y-%m-%d').date())
    # for i in range(len(p['data'])):
    #     for j in range(len(li)):
    #         s = p['data'][i]['date']
    #         if len(re.sub(r'-.*', '', s)) < 2:
    #             if li[j] == '0' + p['data'][i]['date']:
    #                 result.append(p['data'][i]['date'])
    #                 result1.append(p['data'][i]['open'])
    #                 result2.append(p['data'][i]['close'])
    #         if li[j] == p['data'][i]['date']:
    #             result.append(p['data'][i]['date'])
    #             result1.append(p['data'][i]['open'])
    #             result2.append(p['data'][i]['close'])

    print(result2)
    for i in range(len(result)):
        print(result[i], result1[i], result2[i])

openAndClosePrices('1-January-2000', '22-February-2000', 'Monday')