

###########
# Part 02 #
###########
'''
Given a list of tuples of (name, score)
return a list of tuples (name, placement)
in descending order. The higher the score, the better.
'''

input_scores_02 = [
    ('Mason', 85),
    ('Henry', 92),
    ('Jaime', 86),
    ('Evan', 89),
    ('Noelle', 81),
]

expected_output_02 = [
    ('Henry', 1),
    ('Evan', 2),
    ('Jaime', 3),
    ('Mason', 4),
    ('Noelle', 5),
]


def place_02(scores):
    scores = []
    return scores

print place_02(input_scores_02)
print place_02(input_scores_02) == expected_output_02
