# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
#
# # temp_list = data['temp'].to_list()
# # print(temp_list)
# #
# # print(f"the average value of temp: {data['temp'].mean()}")
# # print(f"the max value of temp: {data['temp'].max()}")
# #
# # # Get Data in column
# # print(data["condition"])
# # print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
#
# # Get row data which has max temp
# print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# # convert temp on monday to fahrenheit
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 1.8 + 32
# print(f"fahrenheit : {monday_temp_f} ")
#
# # create dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

# Challenge
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data.Primary_Fur_Color == "Gray"])
cinnamon_squirrels_count = len(data[data.Primary_Fur_Color == "Cinnamon"])
black_squirrels_count = len(data[data.Primary_Fur_Color == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")
