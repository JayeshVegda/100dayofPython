dict_data = {
    "FirstName": "jay",
    "LastName": "vegda",
    "Phone": "9510233120"
}

dict_data.update({"FirstName": "Jayesh"}) 
dict_data.clear() # to clear dict
dict_data.pop("Phone") # to remove item
dict_data.popitem() # to Remove last item
del dict_data["FirstName"] # to delete item

print(dict_data)
