import json

def get_lesson_reading(lesson):
    f = open('data.json')
    data = json.load(f)
    
    # Iterating through the json list
    for lesson_dict in data['lessons']:
        if lesson == lesson_dict:
            retval = data['lessons'][lesson]['read']
            break
                
    # Closing file
    f.close()
    return retval

def get_lesson_quiz(lesson):
    f = open('data.json')
    data = json.load(f)
    
    # Iterating through the json list
    for lesson_dict in data['lessons']:
        if lesson == lesson_dict:
            retval = data['lessons'][lesson]['quiz']
            break
                
    # Closing file
    f.close()
    return retval