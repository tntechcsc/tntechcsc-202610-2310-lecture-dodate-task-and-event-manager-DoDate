# TODO: import the task, category, and event classes
# TODO: import the datetime library

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
    
    #########################################
    #            Task Methods               #
    #########################################

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


    # TODO: Write a method called delete_task that will take an index as an argument. It will then delete
    #       the task at that index for the Planner object


    # TODO: Write a method called add_task_step that will take in a task index and a step title as arguments.
    #       It will then call the add_step method on the Task object at the specified index in the Planner's 
    #       task list.

    # TODO: Write a method called toggle_task_step that takes in a task index and a step index as arguments.
    #       It will then call the toggle_step method on the Task object at the specified index in the Planner's
    #       task list.

    # TODO: Write a method called edit_task_step that takes a task index, a step index, and a new step title 
    #       as arguments. It will then call the edit_step method on the specified Task object.

    # TODO: Write a method called remove_task_step that will take a task index and a step index as arguments.
    #       It will then call the remove_step on the specified Task object.

    # TODO: Write a method called edit_task that will take a task index, task name, focus bool, description, 
    #       due date, status, and weight as arguments. Call the update_task method on the specified Task.

    # TODO: Write a method called get_task_by_index that accepts a task index as an arugment.
    #       It should return the specified task from the Planner's task list.

    # TODO: Write a method called get_overdue tasks that accepts a date object as the argument representing today.
    #       You will need a list to store the overdue tasks. For each task in the Planner's task list, determine if 
    #       the task is overdue using the is_overdue method. If it is, add it to the list of overdue tasks and return 
    #       the list when done.
    
    # TODO: Write a method called get_due_soon that accepts a date object as the argument representing today. This method
    #       will search for any tasks due within a week. To do so, find the date 7 days from now with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the tasks in the
    #       Planner.  If the task's due date is greater than or equal to today's and less than or equal to the end of the week,
    #       add it to the list of tasks due soon and return when done. Tasks that were not given a due date or are already
    #       completed should not be added to the list.

    # TODO: Write a method called get_tasks_in_todays_focus. For each task in the Planner's task list, add it to a list
    #       collecting tasks where the todays_focus is set to True. Return the list of tasks in today's focus.

    # TODO: write a method called get_task_status_counts. It should create a dictionary with each status as a key. The
    #       count for each status should start at a 0. For each task in the Planner, increment the count for the correct
    #       status in the dictionary. Return the dictionary when done.

    # TODO: Write a method called get_incomplete_by_category. It should create a dictionary with each category as a key.
    #       There should also be a variable to count the number of not complete tasks. The count for each category should 
    #       start at 0. For each task in the Planner, increment the count for the category that task is in only if the status
    #       is not "completed". Return a dictionary that has 2 key-value pairs: one pair has the key "total" with the value 
    #       of the number of tasks that are not complete and another pair with the key "byCategory" that has the value of the
    #       dictionary.
    
    #########################################
    #          Category Methods             #
    #########################################

    # TODO: Write a method called get_category_by_index that is passed a category index as an argument. Return
    #       the requested Category object from the Planner's list of categories

    # TODO: Write a method called add_category that accepts a name and description as arugments.
    #       Create a new Category object and add it to the Planner's list of categories.

    # TODO: Write a method called edit_category that accepts a category index, name and description
    #       as arguments. It will then call the setters for the specified Category object.

    # TODO: Write a method called remove_category_by_index that accepts a category index as an argument.
    #       It then remvoes the specified Category object from the Planner's list of categories.


    #########################################
    #            Event Methods              #
    #########################################

    # TODO: Write a method called get_event_by_index that accepts an index as an argument. It then
    #       returns the specified Event object from the Planner's list of events.

    # TODO: Write a method called add_event that accepts an event name, description, date, start time,
    #       end time, and category name as arguments. It then creates a new Event object and adds it 
    #       to the Planner's list of events.

    # TODO: Write a method called remove_event_by_index that accepts an index as an argument. It then
    #       removes the specified index from the Planner's list of events.

    # TODO: Write a method called set_event_category that accepts an event index and a category name. 
    #       Set the corresponding Event object's category to the specified category name.

    # TODO: Write a method called get_upcoming_events that accepts a date object as the arument representing
    #       today's date. It should calculate the date exactly 7 days from today with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the
    #       Planner's list of events. Collect all events in a list where there is a date and the date is greater
    #       than or equal to today and less than or equal to 7 days from now. Return the list of events happening
    #       within the next week.

    # TODO: write a method called get_todays_events that accepts a date object as an argument representing
    #       today's date. Iterate throught the Planner's list of events to find event's who's date matches
    #       today's date. Collect those events in a list and return them.
