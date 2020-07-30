alin_0 = {'color':'green','points':'5'}
print(alin_0['color'])
print(alin_0['points'])

alin_0 = {}
alin_0['color'] = 'green'
alin_0['point'] = 5
print(alin_0)

alin_0 = {'color':'green'}
print('The alien is ' + alin_0['color'] + '.')
alin_0['color'] = 'yellow'
print('The alien is now ' + alin_0['color']  + ".")

alin_0 = {'color':'yellow',"point":"5"}
del alin_0['point']
print(alin_0)



favorite_languages = {
    'jen':"python",
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
# for name,language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")
#
# for a in favorite_languages.keys():
#     print('我现在就只想知道他们的名字:' + a.title())
#
# for b in favorite_languages.values():
#     print('我现在就只想知道他们学的语言：' + b.title())

assholes = ['jen','phil']
for asshole in favorite_languages.keys():
    print(asshole.title())

    if asshole in assholes:
        print('Hi the asshole ' + asshole.title() + ' like ' + favorite_languages[asshole].title())


my_friends = {
    'wulijia':'male',
    'lulu':'female',
    'ale':'male',
    'nana':'female'
}

assholes = ['ale','wulijia']
for asshole in assholes:
    print(asshole.title())

    if asshole in my_friends.keys():
        print(asshole + ' is asshole.')

# for my_friend in sorted(my_friends.keys()):
#     print(my_friend.title())
#
# for value in my_friends.values():
#     print(value)
#
# aliens = []
#
# for new_alien in range(30):
#     new_alien ={'color':"grenn","points":'5','speed':'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:5]:
#     print(alien)
# print('...')

pets = []
pet1 = {'name':'ale1','animal':'dog','master':"wenzhi"}
pet2 = {'name':'ale2','animal':'cat','master':'wenzhi'}
for pet in pet1.values():
    pets.append(pet)
print(pets)

for pet in pet2.values():
    pets.append(pet)
print(pets)

for pet in pets:
    print(pets)

families = {
    'father':'wenjinhong',
    'mother':'dengxingying',
    'son':'wenzhi',
    'daughter':'wenruosi',
}

for a,b in families.items():
    print(a)
    print(b)

