import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel(r"C:/Users/geeta/Documents/data_movie.xlsx")
high_movie = df.loc[df['IMDb Rating'].idxmax()]
average = df['IMDb Rating'].mean()
movie_rating = df[df['IMDb Rating']>8]
top5 = df.sort_values(by = 'IMDb Rating',ascending = False).head(5)
print(top5)
print('Category',df.groupby('Category')['IMDb Rating'].mean())
print("Movie rating more than 8",movie_rating)
print("average of rating",average)
print('high_movie',high_movie)
plt.bar(top5['Name'],top5['IMDb Rating'])
plt.xlabel('Name')  
plt.ylabel('IMDb Rating')
plt.show()
