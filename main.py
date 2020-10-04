import datetime
import csv

def convert_utc_durham(val):
    date = datetime.datetime.strptime(val, "%Y-%m-%dT%H:%M:%SZ")
    year = (str(date.year))
    if date.month < 10:
        month = str(date.month).zfill(2)
    else:
        month = (str(date.month)) 

    if date.day < 10:
        day = str(date.day).zfill(2)
    else: day = (str(date.day))
    hour = convert_hour(int(date.hour))
    
    date_string = year + "-" + month + "-" + day + " " + str(hour) + ":00:00"
    
    return year + "-" + month

def convert_hour(hour):
    val = int(hour)

    if val == 0:
        return 20
    elif val == 1:
        return 21
    elif val == 2:
        return 22
    elif val == 3:
        return 23
    elif val == 4:
        return 0

    return (val - 4)

def pollutant_data(lines, pol):
    data_dict = {}
    days_dict = {}

    for i in range(len(lines)):
        line = lines[i].split(',')
        if i > 0 and line[5] == pol:
            date = convert_utc_durham(line[3])

            if days_dict.get(date) == None:
                days_dict[date] = 1
            else:
                curr_val = int(days_dict[date])
                days_dict[date] = curr_val + 1

            if data_dict.get(date) == None:
                data_dict[date] = float(line[6])
            else:
                curr_val = float(data_dict[date])
                data_dict[date] = curr_val + float(line[6])
    
    return {
        "data": data_dict,
        "days": days_dict
    }

def avg_data(data_dict, days_dict):
    fields = ['Date', 'Average']
    rows = []
    for d in sorted(data_dict.keys()):

        val = float(data_dict[d])
        samples = float(days_dict[d])
        avg = float(val/samples)
        row = []
        row.extend([str(d), str(avg)])
        rows.append(row)
        print(str(d) + " " + str(avg) + "\n")
    
    filename = "csv_data.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def test():
    durham_file = open('/Users/Shayan/Desktop/CDC/OpenAQDurham.csv', 'r')

    lines = durham_file.read().split('\n')

    # print("-----Carbon Monoxide-----\n")
    # co = pollutant_data(lines, "co")
    # avg_data(co.get("data"), co.get("days"))
    # print("-------------------------\n")

    # print("-----Sulphur Dioxide-----\n")
    # so2 = pollutant_data(lines, "so2")
    # avg_data(so2.get("data"), so2.get("days"))
    # print("-------------------------\n")

    # print("-----Nitrogen Dioxide-----\n")
    # no2 = pollutant_data(lines, "no2")
    # avg_data(no2.get("data"), no2.get("days"))
    # print("-------------------------\n")

    # print("-----PM10-----\n")
    # pm10 = pollutant_data(lines, "pm10")
    # avg_data(pm10.get("data"), pm10.get("days"))
    # print("-------------------------\n")

    # print("-----PM2.5-----\n")
    # pm2_5 = pollutant_data(lines, "pm25")
    # avg_data(pm2_5.get("data"), pm_25.get("days"))
    # print("-------------------------\n")

    print("-----o3-----\n")
    o3 = pollutant_data(lines, "o3")
    avg_data(o3.get("data"), o3.get("days"))
    print("-------------------------\n")

#durham_data()

test()
