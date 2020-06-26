#!/usr/bin/env python3
# sort calendar
# pick dayID's of dates in between the input dates
# count number of details of those daID's only
import sys
import json
from datetime import datetime
import glob


user_logs = []

def active(d1, d2):
    result = []
    datas = read(d1, d2)
    for data in datas:
        if data['count'] >= 5:
            result.append(data["user_id"])
    print(result)

def superactive(d1, d2):
    result = []
    datas = read(d1, d2)
    for data in datas:
        if data['count'] > 10:
            result.append(data["user_id"])
    print(result)

def bored(d1, d2):
    result = []
    datas = read(d1, d2)
    for data in datas:
        if data['count'] < 5:
            result.append(data["user_id"])
    print(result)



def read(d1, d2):

    user_data = {
        "user_id": "",
        "count": 0,
    }
    json_files = glob.glob("../data/*.json")
    for json_file in json_files:
        user_data['user_id'] = json_file
        # print(user_id)

        with open(json_file) as json_file:
            
            dates = []
            data = json.load(json_file)
            
            dates = []
            for key in data['calendar']['dateToDayId']:
                dates.append(key)
            
            dates.sort()

            dates_in_parameter = []
            for date in dates:
                if date >= d1 and date <= d2:
                    dates_in_parameter.append(date)
            # print(dates_in_parameter)

            dayIds_in_parameter = []
            for date in dates_in_parameter:
                dayIds_in_parameter.append(
                    data['calendar']['dateToDayId'][date])
                # print(data['calendar']['dateToDayId'][date])

            # print(data['calendar']['daysWithDetails'])
            hadMealDayID = []
            for dayId in data['calendar']['daysWithDetails']:
                hadMealDayID.append(data['calendar']['daysWithDetails'][dayId]['day']['id'])
                user_data['user_id'] = data['calendar']['daysWithDetails'][dayId]['day']['userId']
                # print(dayId)

        count = len(
            [value for value in hadMealDayID if value in dayIds_in_parameter])
        user_data['count'] = count
        #print(user_data)
        user_logs.append(dict(user_data))

    return user_logs



if __name__ == '__main__':

    function = ""
    if len(sys.argv) < 3:
        print('check arguments again')
    else:
        function = getattr(sys.modules[__name__], sys.argv[1])
        d1 = sys.argv[2]
        d2 = sys.argv[3]
        function(d1, d2)
