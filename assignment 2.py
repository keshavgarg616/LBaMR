import pandas as pd
# import matplotlib
# import matplotlib.pyplot as plt

df = pd.read_csv('e:/UMass/LBaMR/nppd/rating.csv')
new_df_for_average_ratings = df.groupby('movieId')['rating'].mean().reset_index()
new_df_for_average_ratings.columns = ['movieid', 'average_rating']
print(new_df_for_average_ratings)

highest_rating_movie = new_df_for_average_ratings.loc[new_df_for_average_ratings['average_rating'].idxmax()]
print("Movie with the highest average rating:", highest_rating_movie)

# df['timestamp'] = pd.to_datetime(df['timestamp'])
# df['Year'] = df['timestamp'].dt.year
# df['Month'] = df['timestamp'].dt.month
# df['Day'] = df['timestamp'].dt.day

# filtered_df = df[df['Year'] >= 2010]

# # Plot histogram
# filtered_df['rating'].plot(kind='hist', edgecolor='black', bins=10)

# # Add labels and title
# plt.xlabel('Ratings')
# plt.ylabel('Frequency')
# plt.title('Histogram of Ratings (2010 and Later)')

# # Show the plot
# plt.show()


