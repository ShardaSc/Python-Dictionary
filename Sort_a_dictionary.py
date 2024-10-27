my_dict = {"apple": 10, "banana": 5, "cherry": 20, "date": 15}

#Sort in ascending order
sorted_dict_asc = dict(sorted(my_dict.items(),key=lambda item:item[1]))

#Sort in descending order
sorted_dict_des = dict(sorted(my_dict.items(),key=lambda item:item[1],reverse=True))

#Print both the dictionaries
print (sorted_dict_asc)
print (sorted_dict_des)



#Output

{'banana': 5, 'apple': 10, 'date': 15, 'cherry': 20}
{'cherry': 20, 'date': 15, 'apple': 10, 'banana': 5}