person1={'name':'james','address':'ulsan','email':'ojscom@hanmail.net'}
print(person1)
print(person1['name'])
print(person1['email'])
print(person1.items())
for key, value in person1.items():
    #print('\nkey :  '+key)
    #print('\nvalue :'+value)
    # print('\nkey \\  '+"'"+key+"'")
    # print('\nvalue \\'+"'"+value+"'")
    print('\nkey \\  '+'"'+key+'"')
    print('\nvalue \\'+'"'+value+'"')
    person1['name']='jang'