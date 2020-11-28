#Although hash tables come built-in in the form of dictionaries in Python,
#here we'll try to implement our own hash table

class hash_table():
    def __init__(self,size): #We initialize the size of our hash table(no. of buckets) with the size given to the class object
        self.size = size
        self.data = [None]*self.size #We initialize an array of size 'size' with None


    def __str__(self): #As in the array implementation, this method is used to print the attributes of the class object in a dictionary format
        return str(self.__dict__)

    def _hash(self, key): #Our custom hash function
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i])*i) % self.size #ord(key[i]) gives the unicode code point of the character key[i]
        return hash #The hash value obtained after applying the hash function to the key is returned

    def get(self,key): #Function to return the value of the key entered by the user
        hash = self._hash(key) #Hash value of the key is calculated by passsing the key to the _hash function
        if self.data[hash]: #Multiple items may exist in the position of the hash value returned by the hash function, so we have to chceck all of them
            for i in range(len(self.data[hash])): #We loop over the entire list of lists that may be present in the 'hash' position of the data array
                if self.data[hash][i][0] == key: #For every list in the list of lists(extracted by 'i'), we match the first element of the list with the given key
                    return self.data[hash][i][1] #If we get a match, we return the second element of that list, which is the value
        return None #If we don't find the key, we return None

    def set(self, key, value): #Function to insert a new key, value pair
        hash = self._hash(key) #Hash value of the key is calculated using the _hash function
        if not self.data[hash]: #If the 'hash' position of the data array is empty, we insert the key, value pair as a list
            self.data[hash] = [[key,value]]
        else: #If the 'hash' position is not empty, implying a collision, we simply append the list of key,value pair to the lists already present
            self.data[hash].append([key, value])
        print(self.data)

    def keys(self): #Function to return all the keys
        keys_array = [] #Array to hold the keys
        for i in range(self.size): #We loop over the entire table
            if self.data[i]: #If we find a non-empty bucket, we go in and loop over all the key,value pairs that might be in it
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])): #Looping over all the lists(key,value pairs) in the current bucket
                        keys_array.append(self.data[i][j][0]) #Adding the key of each list to the keys_array
                else:
                    keys_array.append(self.data[i][0][0])
        return keys_array

    def values(self): #Function to return all the values, with exactly the same logic as the keys function
        values_array = []
        for i in range(self.size):
            if self.data[i]:
                for j in range(len(self.data[i])):
                    values_array.append(self.data[i][j][1])  #Only difference from the keys function is instead of appending the first element, we are appending the last element of each list
        return values_array


new_hash = hash_table(2)
print(new_hash)
#{'size': 2, 'data': [None, None]}

new_hash.set('one',1)
new_hash.set('two',2)
new_hash.set('three',3)
new_hash.set('four',4)
new_hash.set('five',5)
print(new_hash)
#{'size': 2, 'data': [[['one', 1], ['five', 5]], [['two', 2], ['three', 3], ['four', 4]]]}

print(new_hash.get('one'))
#1

print(new_hash.keys())
#['one', 'five', 'two', 'three', 'four']
print(new_hash.values())
#[1, 5, 2, 3, 4]


#Now although there are some for loops running in the class hash,
#the time complexity is not O(n).
#This is because n stands for the size of the input, which corresponds to number of key,value pairs in the table
#But the for loop in the _hash function runs only for the length of the key, which would be insignificantly small in comparison to the number of entries in general.
#Also, the for loop in the get function runs for the length of the collisioned array, which in most cases, won't be too long
#Atleast nowhere near to the number of total entries, hence the time complexity remains way less than O(n), even less than O(log n) in most cases
#The keys and values methods are slightly worse than O(n) though, as we have to loop over the entire size of the table once,
#And loop over all the lists in the buckets which have collision
