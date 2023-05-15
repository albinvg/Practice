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
