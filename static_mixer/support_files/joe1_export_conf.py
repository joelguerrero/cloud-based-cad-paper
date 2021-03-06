'''
exportstl
===

You should give the following information:

	- did (str): Document ID
	- wid (str): Workspace ID
	- eid (str): Element ID

'''

from apikey.client import Client

# stacks to choose from
stacks = {
    'cad': 'https://cad.onshape.com'
}

# create instance of the onshape client; change key to test on another stack
c = Client(stack=stacks['cad'], logging=True)



# get features for doc
#did = raw_input('Enter document ID: ')
#wid = raw_input('Enter workspace ID: ')
#eid = raw_input('Enter element ID: ')

did = 'a87bc0dccf9793fd588c9b5d'
wid = 'cb521c3ed58531b582af2110'
eid = '60f61aff8df2a1a52f5bf5d7'


configuration = {
'units': 'meter',
'scale': 1.0,
'configuration' : 
#	'anglepipe=45+deg;dia1=0.75+m;dia2=1+m'
	'anglepipe=90+deg;'
	'dia1=1+m;'
	'dia2=1+m'
}

# get the STL export
stl = c.part_studio_stl_conf(did, wid, eid, configuration)



# print to the console some info - optional
print(" ")
print("End of request for STL output using configurations")
print("***************************************************************")
#print stl.text



#Write the STL output in the file test.stl
file = open('test.stl', 'w')
file.write(stl.text)
file.close()
