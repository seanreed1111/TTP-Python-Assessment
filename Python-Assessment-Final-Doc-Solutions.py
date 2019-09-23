
# coding: utf-8

# In[ ]:


''' #1
Write a function called 'addBetween'.

Given 2 integers, "addBetween" returns the sum 
of all numbers between the two given integers, 
beginning at num1, and excluding num2.


If num2 is not greater than num1, the function should return 0.
output = addBetween(3, 7)
print(output) # --> 18
'''


# In[4]:


def addBetween(num1, num2):
    sum = 0
    for i in range(num1,num2):
        sum += i
    return sum

output = addBetween(3, 7)
print(output) # --> 18


# In[5]:


#alternative solution
def addBetween2(num1, num2):
    return sum([i for i in range(num1,num2)]) #here I made a list that I didn't really need just to use list comprehension syntax.

output = addBetween2(3, 7)
print(output) # --> 18


# In[ ]:


''' #2
write a function called 'combine'

Given two lists, combine returns a new list
with all elements of both lists, sorted

lst1 = ['b', 'c','a','f']
lst2 = ['d','e','g']

output = combine(lst1,lst2)
print(output) # -> ['a','b','c','d','e','f', 'g']


# In[7]:


def combine(list1, list2):
    return sorted(list1 + list2) 

lst1 = ['b', 'c','a','f']
lst2 = ['d','e','g']
output = combine(lst1,lst2)
print(output)


# In[10]:


dir(list)


# In[13]:


#alternative solution
def combine2(list1, list2):
    new_list = []
    new_list.extend(list1)
    new_list.extend(list2)
    return sorted(new_list)
    
    
lst1 = ['b', 'c','a','f']
lst2 = ['d','e','g']
output = combine2(lst1,lst2)
print(output)


# In[ ]:


''' #3
write a function called 'switch'
Given a dictionary, the function switch returns a new dictionary
with the keys and values reversed

d = {'cat': 1, 'dog':2, 'parrot':3, 'raptor':4, 'snake':5}
output = switch(d)
print(output) # -> {1:'cat', 2:'dog', 3:'parrot', 4:'raptor', 5:'snake'}

'''


# In[18]:


def switch(dictionary):
    new_dict = {}
    for k in dictionary:
        new_dict[dictionary[k]] = k
    return new_dict

d = {'cat': 1, 'dog':2, 'parrot':3, 'raptor':4, 'snake':5}
output = switch(d)
print(output)
        


# In[16]:


#ADVANCED ALTERNATIVE SOLUTION
def switch2(dictionary):
    return {dictionary[k]:k for k in dictionary} #dictionary comprehension!! (we never discussed this!)

d = {'cat': 1, 'dog':2, 'parrot':3, 'raptor':4, 'snake':5}
output = switch2(d)
print(output)


# In[ ]:


''' #4
Write a function called 'isSameLength'.

Given two words, "isSameLength" returns whether the given 
words have the same length.

output = isSameLength('words', 'super')
print(output) # --> True
'''


# In[19]:


def isSameLength(word1, word2):
    return len(word1) == len(word2)

output = isSameLength('words', 'super')
print(output)


# In[ ]:


''' #5
write a function called 'stringToWords'
given a string with two sentences, stringToWords
separate the sentences into two lists of words, one for each sentence.

string1 = "This was a sentence. And it's now a list."
output = stringToWords(string1)
print(output) ->  ['This', 'was', 'a', 'sentence'],['And', "it's", 'now', 'a', 'list']

'''


# In[24]:


string1 = "This was a sentence. And it's now a list."
string1.split()


# In[25]:


string1 = "This was a sentence. And it's now a list."
string1.split('.')


# In[26]:


# note I neglected to put the parentheses around the final result in my description
#of the problem, so we will be really liberal in grading this.

def stringToWords(string1):
    lst = string1.split('.')
    sentence1 = lst[0]
    sentence2 = lst[1]
    return sentence1.split(), sentence2.split()
            
output = stringToWords(string1)
print(output)       


# In[ ]:


''' #6
write a function called 'bigSixSmall'

given a list of numbers, bigSixSmall returns a new list:
if the number from the list is > 6, the new list should have "Big" in it
if the number from the list is 6, the new list should have "Six" in it
if the number from the list is < 6, the list should say "Small"

list1 = [1,7,2,6,13]

output = bigSixSmall(list1)
print(output)  #-> ['Small', 'Big', 'Small', 'Six', 'Big' ] 
'''


# In[27]:


def bigSixSmall(list1):
    new_list = []
    for num in list1:
        if num > 6:
            new_list.append('Big')
        elif num == 6:
            new_list.append('Six')
        else:
            new_list.append('Small')
    return new_list
        


list1 = [1,7,2,6,13]
output = bigSixSmall(list1)
print(output) #-> ['Small', 'Big', 'Small', 'Six', 'Big' ]


# In[ ]:


''' #7
Write a function called 'select'.

Given list and a dictionary, "select" returns a new dictionary
whose keys are those in the given dictionary which are present 
in the given list.

Notes:
If keys are present in the given list, but are not in the given 
dictionary, it should ignore them.
It does not modify the passed in dictionary.
input_list = ['a', 'c', 'e']
input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

output = select(input_list, input_dict)
print(output) # --> {'a': 1, 'c': 3}

print(input_dict) # --> {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''


# In[29]:


def select(lst,dictionary):
    new_dict = {}
    for item in lst:
        if item in dictionary:
            new_dict[item] = dictionary[item]
    return new_dict
            

input_list = ['a', 'c', 'e']
input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

output = select(input_list, input_dict)
print(output) # --> {'a': 1, 'c': 3}


# In[31]:


''' #8
Write a function called 'to_dictionary' that takes in
a list of numbers as input
and returns a dictionary.

The keys should be each number from the input list,
and the values should be 
True if the number is even 
or False if the number is odd

output = to_dictionary([3,6,9,12,15])
print(output) #-->  {3:False, 6:True, 9:False, 12:True, 15:False}
'''


# In[32]:


def to_dictionary(lst):
    new_dict = {}
    for key in lst:
        if key % 2 == 0:
            new_dict[key] = True
        else:
            new_dict[key] = False
    return new_dict

output = to_dictionary([3,6,9,12,15])
print(output) #-->  {3:False, 6:True, 9:False, 12:True, 15:False}

