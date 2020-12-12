import matplotlib.pyplot as plt

hfont = { 'fontname' : 'Lato'}

#generate a pie chart with the Olympic data

values= [316, 203, 107]
labels= ["Gold", "Silver", "Bronze"]


plt.title("Medals obtained by Pol", pad=20, **hfont)

plt.pie(values, labels=labels, colors=colors)
# generate the chart
plt.show()