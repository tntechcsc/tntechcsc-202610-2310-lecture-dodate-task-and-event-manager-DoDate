# TODO: import the task, category, and event classes

'''
The Planner class is the central coordinating component of the system. It owns and manages 
all categories, tasks, and events. Most application behavior ultimately routes through this class.
'''

# TODO: create a Planner class
class Planner:
    # TODO: write a constructor with the attributes name, categories, tasks, and events.
    #       Each of these attributes will be passed in as arguments. They should be set
    #       to each of the attributes accordingly.
    #       If categories, tasks, or events were passed as Nonetypes, set them equal to 
    #       an empty list.

    # TODO: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    # TODO: write a method called to_dict. This methods should turn a Planner object into a dictionary.
    #       It should return a dictionary where each attribute and its value is a key value pair. The key 
    #       should have the exact same name as the attribute. Categories, tasks, and events are stored
    #       as lists; each item in those lists will need to be converted to a dictionary as well. Using
    #       the to_dict method from each of those classes create lists of category, task, and event dictionaries
    #       to use for the corresponding values in the dictionary.

    # TODO: write a static method called from_dict. This method should take in a dictionary object as an 
    #       argument. It will then create a Planner object using the key value pairs. The keys will 
    #       correspond directly with the names of the Planner attributes. 
    #       For each of the attributes in a Planner, pull the data from the planner dictionary. You will
    #       need to convert each of the categories, events, and tasks to objects as well by calling the 
    #       from_dict method of each class. Those lists of objects should be used sent as the arguments
    #       for the Planner object--not the dictionaries from the raw data.
    
    # TODO: write a method called create_task that is passed each of the attributes for a Task object
    #       EXCEPT for the steps. It should use the data received as arguments to create a task object
    #       sending an empty list for the steps. Once the object has been created, append it to the 
    #       Planner's list of tasks.

    # TODO: write a method called set_task_status that is passed the index of a task. Get the task from
    #       the Planner's list of tasks according to its index and find its current status. According to
    #       the list below, set the status to the correct new value.
    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''

    # TODO: write a method called set_task_todays_focus which is passed the index of a task. Get that task 
    #       from the Planner's list of tasks according to its index. Call the set_todays_focus method from 
    #       the Task class on that object. 
