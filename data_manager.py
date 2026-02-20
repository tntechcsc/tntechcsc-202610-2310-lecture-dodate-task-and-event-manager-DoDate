
# TODO: import the json module and the Planner class

'''
The Data_Manager class handles persistence. It is responsible for loading planner 
data from storage and saving planner data back to storage.
'''

# TODO: create a Data_Manager class
    # TODO: write a constructor with the attribute file_path which is sent as an argument

    # TODO: write a method called open_planner. It will open the file specified in the file_path
    #       attribute and read the data from it. It will then use the json loads command to 
    #       convert the json object to a dictionary. The dictionary should then be used to create 
    #       a Planner object using the from_dict method and return the resulting object.
    
    # TODO: Write a method called save_planner that accepts a Planner object as an argument.
    #       It should then open the file from the file_path attribute in write mode. It will
    #       then convert the Planner to a dictionary and use the json dump command to write 
    #       the dictionary to the file.
