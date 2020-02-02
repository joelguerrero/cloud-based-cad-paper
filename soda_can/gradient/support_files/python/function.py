import json

with open('total_surface.json') as json_file:
    total_surface = json.load(json_file)

with open('volume.json') as json_file:
    volume = json.load(json_file)
    
ts  = 10000*total_surface['result']['message']['value']
vol = 1000000*volume['result']['message']['value']

#ts  = 1*total_surface['result']['message']['value']
#vol = 1*volume['result']['message']['value']

f = open('output1.txt', 'w')

f.write(str(ts))
f.write("\n")
f.write(str(vol))
f.write("\n")
f.close() 
