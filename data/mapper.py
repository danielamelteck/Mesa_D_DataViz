import matplotlib.pyplot as plt

hfont = { 'fontname' : 'Arial'}

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Poland', 'United Kingdom'
sizes = [74.28, 25.72]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
colors = ['orange', 'purple']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title("Poland VS. United Kingdom", pad=20, **hfont)

plt.show()