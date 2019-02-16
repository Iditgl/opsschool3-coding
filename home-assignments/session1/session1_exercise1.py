import json
import yaml


with open('my_list.json') as json_file:
    data = json.load(json_file)
 #   print(data)
  #  print(data['buckets'])
    bucket_list = data['buckets']
    people_list = data['ppl_ages']
 #   print(bucket_list)
    bucket_list.sort()
#    print(bucket_list[0])
    list1 = []
    list2 = []
    list3 = []
    list4 = []


    for p in people_list:
        x=people_list[p]
        if(x>=bucket_list[0] and x<=bucket_list[1]):
            list1.append(p)

    for p in people_list:
        x=people_list[p]
        if(x>=bucket_list[2] and x<=bucket_list[3]):
            list2.append(p)

    for p in people_list:
        x=people_list[p]
        if(x>=bucket_list[1] and x<=bucket_list[2]):
            list3.append(p)

    for p in people_list:
        x=people_list[p]
        if(x>=bucket_list[3]):
            list4.append(p)

dict = {}
dict["11-20: "] = list1
dict["25-40: "] = list2
dict["20-25: "] = list3
dict["40-102: "] = list4
#print(dict)

with open('my_list.yml', 'w') as outfile:
    yaml.dump(dict, outfile, default_flow_style=False)










