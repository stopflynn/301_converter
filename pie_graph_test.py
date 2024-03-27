import matplotlib.pyplot as plt

achieved_credits = merit_credits = excellence_credits = 5

# Display pie chart
labels = 'Achieved', 'Merit', 'Excellence'
sizes = [achieved_credits, merit_credits, excellence_credits]
explode = (0, 0, 0)  # explode 1st slice
plt.pie(sizes, explode=explode, labels=labels, autopct='5', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('NCEA Credits')
plt.show()