from random import *

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
    types = 1
    return [text, colour, types]
#
# text = generate_quiz()[0]
# rect_list =
# for dictionary in shapes:
#     if dictionary['text'] == text:
#         rect_list.append(dictionary['rect'])
# print (rect_list)
def mouse_press(x, y, text, color, quiz_type):
    rect_list = []
    text = generate_quiz()[0]
    color = generate_quiz()[1]
    quiz_type = generate_quiz()[2]
    for dictionary in shapes:
        if quiz_type == 0:
            if dictionary['text'] == text:
                rect_list.append(dictionary['rect'])
        else:
            if dictionary['color'] == color:
                rect_list.append(dictionary['rect'])
    if x > int(rect_list[0][0]) and y > int(rect_list[0][1]):
        return True
    else:
        return False
