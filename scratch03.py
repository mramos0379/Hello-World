

#define a function to determine the winning percentage of a player




import pickle

def rate_of_winning(dict,player):
    rate=dict[player][1]/dict[player][0]
    return print("the rate of winning for player",player,'is',round(rate,2))

#key = name of player, value is a tuple(# games played,#of victories)
history = {'Archy':(12,4),'Betty':(10,6)}

# create a file a write on it


# open the historypickle file and read from it

file_p3=open('historypickle,p','rb')
history=pickle.load(file_p3)
file_p3.close()
# print(history)
# history['cora']=(100,80)
# print(history)
# file_p3=open('historypickle,p','wb')
# pickle.dump(history,file_p3)
# file_p3.close()

for key in history.keys():
    rate_of_winning(history,key)