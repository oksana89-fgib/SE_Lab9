import matplotlib.pyplot as plt
import streamlit as st

st.image('photo1715528350.jpeg')
st.header('Информация по пассажирам Титаника')
st.write('Количество выживших мужчин по каждому классу обслуживания в заданном возростном диапазоне.')
with open("data.csv") as file:
    Passenclass1 = {
        'selected': 0
    }
    Passenclass2 = {
        'selected': 0
    }
    Passenclass3 = {
        'selected': 0
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
                age = 0
            if not age in Passenclass1:
                Passenclass1[age] = 1
            else:
                Passenclass1[age] += 1
        elif data[2] == '2':
            age = data[6]
            if age == '':
                age = 0
            if not age in Passenclass2:
                Passenclass2[age] = 1
            else:
                Passenclass2[age] += 1
        elif data[2] == '3':
            age = data[6]
            if age == '':
                age = 0
            if not age in Passenclass3:
                Passenclass3[age] = 1
            else:
                Passenclass3[age] += 1
    selected = st.slider("Возраст пассажиров", 0, 100, (0, 100))
    for ages in Passenclass1:
        if ages == 'selected' or ages == '':
            continue
        if selected[0] <= float(ages) <= selected[1]:
            Passenclass1['selected'] += Passenclass1[ages]
    for ages in Passenclass2:
        if ages == 'selected' or ages == '':
            continue
        if selected[0] <= float(ages) <= selected[1]:
            Passenclass2['selected'] += Passenclass2[ages]
    for ages in Passenclass3:
        if ages == 'selected' or ages == '':
            continue
        if selected[0] <= float(ages) <= selected[1]:
            Passenclass3['selected'] += Passenclass3[ages]
clas = ['Класс 1', 'Класс 2', 'Класс 3']
Passenger = [Passenclass1['selected'], Passenclass2['selected'], Passenclass3['selected']]
fig = plt.figure(figsize=(10,8))
plt.bar(clas, Passenger)
for i in range(len(clas)):
    plt.text(i, Passenger[i], Passenger[i], ha='center')
plt.xlabel('Класс обслуживания')
plt.ylabel('Число выживших')
plt.title('Диаграмма - количество выживших мужчин')

st.pyplot(fig)