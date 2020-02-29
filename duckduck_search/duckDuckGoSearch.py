import ddg3


searchQuery = input()

r = ddg3.query(searchQuery)
print(r.type)

if(r.type == 'disambiguation'):
    print("Here are the first couple results related to what you said:")
    
    print(r.related[0].text)
    print(r.related[1].text)

elif(r.type == 'answer'):
    print(r.abstract.text)
elif(r.type == 'nothing'):
    print("Here are some results related to your search:")
    print(r.related)

