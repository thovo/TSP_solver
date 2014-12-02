import json
#f = open("first_love.txt","r")
#x = json.load(f)
#print x[1]
#f.close()
x = [[1,2,3,[1,2,3]], [6,7,8,[8,9,0]]]
f = open("koko.json", 'w')
json.dump(x,f)
f.close()				