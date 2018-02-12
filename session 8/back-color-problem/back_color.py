from random import *
from inside import is_inside
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():

    text_list = [ 'blue', 'red','yellow','green']
    colour_list = ['#3F51B5', '#C62828', '#FFD600', '#4CAF50']
    k = randint(0,3)
    q = randint(0,3)
    text = text_list[k]
    colour = colour_list[q]
    types = 0
    return [text, colour, types]
#
# text = generate_quiz()[0]
# rect_list =
# for dictionary in shapes:
#     if dictionary['text'] == text:
#         rect_list.append(dictionary['rect'])
# print (rect_list)
def mouse_press(x, y, text, color, quiz_type):
    a = [x,y]
    rect_list_text = []
    rect_list_color = []
    print(x, y, text, color, quiz_type)
    for dictionary in shapes:
        if dictionary['text'] == text:
            rect_list_text.append(dictionary['rect'])     #get the cpordinates of rectangle with color same as of quiz shown
        if dictionary['color'] == color:
            rect_list_color.append(dictionary['rect'])
    check_result0 = is_inside(a, rect_list_text[0])
    check_result1 = is_inside(a, rect_list_color[0])
    if quiz_type ==0 and check_result0 == True:
        return True
    elif quiz_type ==1  and check_result1 == True:
        return True
    else:
        return False
