class Data:
    """ This class represents all the data available in the current game which is equivalent to 
    the current state. 
    
    Member:
    circles -- A list of circle objects.
    deltaTime -- The time difference since the last step.
    time -- The accumulated time of all steps.
    """

    circles = []
    deltaTime = 0
    time = 0