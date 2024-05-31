from main_lab9 import *


def test_man_ages_survived_in_classes():
    lines = [
        'PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked',
        '1,1,1,0,0,male,,0,0,0,71.2833,0,0',
        '2,1,1,0,0,female,2,0,0,0,83.1583,0,0',
        '3,0,2,0,0,male,74,0,0,0,53.1000,0,0',
        '4,1,2,0,0,female,11,0,0,0,40.0500,0,0',
        '5,1,3,0,0,male,41,0,0,0,7.9250,0,0',
        '6,1,3,0,0,female,24,0,0,0,9.5875,0,0',
        '7,1,2,0,0,male,41,0,0,0,53.1000,0,0',
        '8,1,1,0,0,male,47,0,0,0,40.0500,0,0',
        '9,1,3,0,0,male,41,0,0,0,7.9250,0,0',
        '10,1,3,0,0,female,0,0,0,0,9.5875,0,0'
    ]
    assert man_survived(lines) == {'class_1': {'0': 1,
                                               '47': 1},
                                   'class_2': {'41': 1},
                                   'class_3': {'41': 2}}


def test_man_survived_all_ages():
    mans_survived = {'class_1': {'28': 2,
                                 '0': 5,
                                 '23': 1,
                                 '45': 6,
                                 '40': 1,
                                 '38': 1,
                                 '37': 1,
                                 '0.92': 1, },
                     'class_2': {'0': 2,
                                 '34': 10,
                                 '0.83': 5,
                                 '1': 2,
                                 '0.67': 1},
                     'class_3': {'0': 9,
                                 '32': 5
                                 }
                     }
    ages = (0, 10)
    assert select_ages(mans_survived, ages) == [6, 10, 9]


def test_man_not_survived_ages():
    mans_survived = {'class_1': {},
                     'class_2': {},
                     'class_3': {}
                     }
    ages = (0, 100)
    assert select_ages(mans_survived, ages) == [0, 0, 0]
