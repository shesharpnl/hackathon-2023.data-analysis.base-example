import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('assets/sourcestack-data-id_bcu86flyul.csv')

plt.figure(figsize=(15, 10))
ax = df['hours'].value_counts().plot(kind='bar')
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.margins(0.1)
plt.savefig('bar_plot.png')