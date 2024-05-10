with open("data.csv") as file:
    class1 = 0
    class2 = 0
    class3 = 0
    for line in file:
        data = line.split(',')
        if data[1] == 'Survived' or data[1] == '0':
            continue
        if data[5] == 'female':
            continue
        if data[2] == '1': class1 += 1
        if data[2] == '2': class2 += 1
        if data[2] == '3': class3 += 1
print(f"Kоличество выживших мужчин по первому классу обслуживания - {class1} чеолвек")
print(f"Kоличество выживших мужчин по втоому классу обслуживания - {class2} челове")
print(f"Kоличество выживших мужчин по тветьму классу обслуживания - {class3} чкловек")