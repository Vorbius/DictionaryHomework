# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''

outfile=open('retail_space1.csv','w')


datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}
num=0
outfile.write('room-number,use,sq-ft,price'+f'\n')
medical = datastore["medical"]
for length in range(5):
    room=medical[num]["room-number"]
    use=(medical[num]["use"])
    sqft=(medical[num]["sq-ft"])
    price=(medical[num]["price"])
    num+=1
    print(room, use, sqft, price)
    outfile.write(str(room)+','+use+','+str(sqft)+','+str(price)+f'\n')
outfile.close()

#actual code 
#outfile=open('retail_space.csv','w')
#outfile.write('room-number,use,sq-ft,price\n)
#list_of_dictionaries = datastore["medical"]
#for a_dictionary in list_of_dictionaries:
#   room = a_dictionary['room-number]
# use = a_dictionary['use']
# sqft = a_dictionary['sq-ft']
# price = a_dictionary ['price']
# outfile.write(f"{room},{use},{sqft},{price}\n)
#outfile.close()