"""
2022-02-26T14:55:35+00:00 501 6.191.20.203
find top 2 IPs per 5xx error code
"""

path = "C:\\Users\\XX\\XX\\XX\\5xx.txt"
with open(path, "r+") as f:
    list1 = f.readlines()

error_code_dict = {}        # key=error_code. value=[IP1, IP2,..]

for i in range(len(list1)):
    list1[i] = list1[i].split()
    error_code = list1[i][1]
    IP = list1[i][2]
    if error_code[0] == '5':
    #create a dict ---> key=error_code. value=[IP1, IP2,..]
        if error_code not in error_code_dict.keys():
            error_code_dict[error_code] = [IP]
        else:
            error_code_dict[error_code].append(IP)


dict1 = {}
freq = []

#iterate through the error code dict
for error_code, IP_list in error_code_dict.items():

    #create a dict per error code. key=IP, value=occurance
    for IP in IP_list:
        if IP not in dict1.keys():
            dict1[IP] = 1
        else:
            dict1[IP] += 1

    freq = list(dict1.items())          # freq = [(IP,occurance), ...]
    freq.sort(key=lambda x:x[1], reverse=True)          # sorted in decending order
    print(error_code, freq[0], freq[1])

    
""" 
########## INPUT ############

2022-02-26T14:55:35+00:00 501 6.191.20.203
2022-02-26T14:55:35+00:00 501 6.191.20.203
2022-02-26T14:55:35+00:00 501 6.191.20.203
2022-02-26T14:55:35+00:00 203 155.80.11.146
2022-02-26T14:55:35+00:00 500 218.122.175.69
2022-02-26T14:55:35+00:00 502 153.188.15.192
2022-02-26T14:55:35+00:00 501 210.84.82.56
2022-02-26T14:55:35+00:00 203 183.42.111.186
2022-02-26T14:55:35+00:00 201 199.35.211.130
2022-02-26T14:55:35+00:00 502 6.191.20.203
2022-02-26T14:55:35+00:00 500 9.126.119.77
2022-02-26T14:55:35+00:00 500 218.122.175.69
2022-02-26T14:55:35+00:00 203 3.82.155.50
2022-02-26T14:55:35+00:00 202 24.109.82.117
2022-02-26T14:55:35+00:00 501 6.191.20.203
2022-02-26T14:55:35+00:00 500 218.122.175.69
2022-02-26T14:55:35+00:00 201 15.240.32.22
2022-02-26T14:55:35+00:00 204 33.145.145.175


########## OUTPUT ############

501 ('6.191.20.203', 4) ('210.84.82.56', 1)
500 ('6.191.20.203', 4) ('218.122.175.69', 3)
502 ('6.191.20.203', 5) ('218.122.175.69', 3)
"""
