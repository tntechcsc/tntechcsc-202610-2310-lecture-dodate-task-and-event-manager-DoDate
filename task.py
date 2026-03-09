# TODO: import the datetime library

'''
The Task class represents an actionable to-do item. Tasks have descriptive information 
and a status (incomplete, in progress, completed).
'''

# TODO: create a Task class
    # TODO: write a constructor with the attributes task_name, todays_focus, description, 
    #       due_date, status, weight, steps, and category_name. Each of these attributes 
    #       will be passed in as arguments. They should be set to each of the attributes accordingly.

    # TODO: Write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"

    # TODO: write a method called to_dict. This method should return a Task object that has been
    #       converted into a dictionary where each of the attribute names and its corresponding 
    #       value turned into a key-value pair. The dictionary keys should be the exact same as the
    #       attribute names.

    # TODO: write a static method called from_dict which accepts a dictionary object as an argument.
    #       Each entry in the dictionary corresponds to a Task attribute. Create and return a Task 
    #       object using the data extracted from the dictionary.

    # TODO: Write a methdo called update_task that accepts all attributes as arugments. It then sets
    #       each of the Task object's attributes to the given arguments. If any of the arugments was
    #       not given a value, the should be set to None as default. The attributes should only be 
    #       updated if a value was passed.

    # TODO: Write a method called is_overdue that accepts a date object as an argument representing 
    #       today's date. If the task was not given a due date or if the status is completed, return false. 
    #       Otherwise, format the due date with the following equation:
    #           due date = datetime.date.fromisoformat(Task object's due date)
    #       Use the datetime call exactly as it was given to you. After formatting, make sure the today 
    #       argument is populated. If the argument is Nonetype, set it equal to datetime.date.today()
    #       Finally, return true if the due date is less than today's date or false if not.

    ###################################
    #       Step Managment            #
    ###################################

    # TODO: Write a method called add_step that is passed a step title as an argument.
    #       It then creates a new step and adds it to the Task's list of steps.
    #       Steps are each a dictionary with the keys "step" and "status". The "step" key
    #       should have the value of the title sent as an argument. The "status" key should
    #       be set to "incomplete" when created.

    # TODO: Write a method called toggle_step that accepts a step index as an argument.
    #       The specified step's status should be set according to the following key.
    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''


    # TODO: Write a method called edit_step that accepts a step index and a new title as arugments.
    #       The specified step should be updated.


    # TODO: Write a method called remove_step that accepts a step index as an argument.
    #       The specified step should be removed from the Task's list of steps.

