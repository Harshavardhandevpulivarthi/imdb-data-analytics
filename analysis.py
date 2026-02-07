import pandas as pd

df = pd.read_csv("imdb_top_250_movies.csv")

print(df.head())

print("\nAverage IMDb Rating:", df['Rating'].mean())

print("\nTop 5 Highest Rated Movies:")
print(df.sort_values(by="Rating", ascending=False).head())
df['Decade'] = (df['Year'] // 10) * 10
print("\nMovies per Decade:")
print(df['Decade'].value_counts().sort_index())
print("\nAverage Rating per Decade:")
print(df.groupby('Decade')['Rating'].mean())
import matplotlib.pyplot as plt

df.groupby('Decade')['Rating'].mean().plot(kind='bar')
plt.title("Average IMDb Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Rating")
plt.show()
