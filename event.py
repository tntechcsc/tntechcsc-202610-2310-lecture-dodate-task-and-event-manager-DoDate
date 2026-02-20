'''
The Event class represents a scheduled occurrence such as a meeting, appointment, 
or gathering. Unlike tasks, events are typically tied to a specific date or time 
and do not have progress states.
'''

# TODO: create an Event class
    # TODO: write a constructor with the attributes event_name, description, date, start_time, 
    #       end_time, and category_name. Each of these attributes  will be passed in as arguments. 
    #       They should be set to each of the attributes accordingly.

    # write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    # TODO: write a method called to_dict. This method should return an Event object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.

    # TODO: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to an Event attribute. Create and return an Event 
    #       object using the data extracted from the dictionary.