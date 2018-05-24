
time_list = [["9.00",True], ["9.15" ,True], ["9.30", True],["9.45",True],["10.00", True],["10.15",True],["10.30",True]]
schdule={"May-1":time_list}
for i in range(len(time_list)):
    if time_list[i][0] == "10.00" and time_list[i][1] == True:
        if i + 6 < len(time_list):
            for j in range(i,i+6):
                time_list[j][1] = False
        else:
            for j in range(i,len(time_list)):
                time_list[j][1] = False
print(time_list)


