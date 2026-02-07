from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.imdb.com/chart/top/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
}

response = requests.get(url, headers=headers)

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.select("li.ipc-metadata-list-summary-item")

movie_data = []

for movie in movies:
    title = movie.select_one("h3.ipc-title__text")
    year = movie.select_one("span.cli-title-metadata-item")
    rating = movie.select_one("span.ipc-rating-star--rating")

    movie_data.append({
        "Title": title.text if title else "N/A",
        "Year": year.text if year else "N/A",
        "Rating": rating.text if rating else "N/A"
    })

df = pd.DataFrame(movie_data)
df.to_csv("imdb_top_250_movies.csv", index=False)

print("CSV file created successfully!")
