import streamlit as st
import matplotlib.pyplot as plt


def man_survived(file):
    survived_passengers = {
        'class_1': {},
        'class_2': {},
        'class_3': {},
    }
    for line in file:
        data = line.split(',')
        if data[1] == 'Survived' or data[1] == '0':
            continue
        if data[5] == 'female':
            continue
        elif data[2] == '1':
            age = data[6]
            if age == '':
                age = '0'
            if age not in survived_passengers['class_1']:
                survived_passengers['class_1'][age] = 1
            else:
                survived_passengers['class_1'][age] += 1
        elif data[2] == '2':
            age = data[6]
            if age == '':
                age = '0'
            if age not in survived_passengers['class_2']:
                survived_passengers['class_2'][age] = 1
            else:
                survived_passengers['class_2'][age] += 1
        elif data[2] == '3':
            age = data[6]
            if age == '':
                age = '0'
            if age not in survived_passengers['class_3']:
                survived_passengers['class_3'][age] = 1
            else:
                survived_passengers['class_3'][age] += 1
    return survived_passengers


def select_ages(passengers, selected_ages):
    selected_passengers = {
        'class_1': 0,
        'class_2': 0,
        'class_3': 0,
    }
    for n_class in passengers:
        for age in passengers[n_class]:
            if selected_ages[0] <= float(age) <= selected_ages[1]:
                selected_passengers[n_class] += passengers[n_class][age]
    return [selected_passengers['class_1'], selected_passengers['class_2'], selected_passengers['class_3']]

def SE_lab9():
    st.image('photo1715528350.jpeg')
    st.header('Информация по пассажирам Титаника')
    st.write('Количество выживших мужчин по каждому классу обслуживания в заданном возростном диапазоне.')
    with open('data.csv') as file:
        mans_survived = man_survived(file)
    clas = ['Класс 1', 'Класс 2', 'Класс 3']
    selected = st.slider("Возраст пассажиров", 0, 100, (0, 100))
    passenger = select_ages(mans_survived, selected)
    fig = plt.figure(figsize=(10, 8))
    plt.bar(clas, passenger)
    for i in range(len(clas)):
        plt.text(i, passenger[i], passenger[i], ha='center')
    plt.xlabel('Класс обслуживания')
    plt.ylabel('Число выживших')
    plt.title('Диаграмма - количество выживших мужчин')
    st.pyplot(fig)

SE_lab9()
