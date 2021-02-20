# Song Popularity Analysis and Prediction
Group E
Members – Claire Nguyen, Gordon Chong Ren Ong, Nikheil Malakar, Tracey Truong

## Summary
At the end of each year, Spotify compiles a playlist of the 100 most streamed songs over the course of the year. In this project, we will analyse the audio attributes of 247,000 songs from Spotify to retrieve any interesting observations, compare that with the Top Spotify Tracks of 2018, and use those findings to predict the popularity of other songs.
## Description
We will conduct a low-level audio analysis for all the songs in the dataset below. There are 131,000 songs for the year 2019 and 116,000 songs for 2018. Each song has metadata that describes the song’s structure and musical content such as acousticness, danceability, duration, energy, instrumentals, key, liveness, loudness, etc. We will extract the “popularity” score of each song and use that in our analysis to determine if there is any correlation between a song’s audio attributes and its associated popularity.

Data set: https://developer.spotify.com/documentation/web-api/

## Goals
The goal of this project is to:
1.	Analyse the relationship between the popularity of the song and other factors
2.	Building clean data
3.	Training multiple models
4.	Reach high accuracy with both training and validation data
## Dataset Summary
The data set was obtained from https://developer.spotify.com/documentation/web-api/. There are 247,000 songs contained in a CSV file with each song having audio attributes that will be translated as integers, floating point values and strings in Python. We will create a SongID for each song and read the CSV data directly into a dictionary in Python with key = SongID and value = values of the 15 audio attributes.
* Artist Name	      The person/s singing the song.
* Track ID	        Unique ID that is used to track the song for Spotify
* Track Name	      Name of Song
* Acousticness	    How prominent acoustic sounds (values between 0 to 1)
* DanceAbility	    How much can you dance with the song (values between 0 to 1)
* Duration_ms	      Duration of song in milli seconds
* Energy	          Energy of the song (values between 0 to 1)
* Instrumentalness	How much instruments are used (values between 0 to 1)
* Key	              The key of the song (values between 0 to 11)
* Liveness	        How live the song is (values between 0 to 1)
* Loudness	        Loudness of the song (values between 0 to 1)
* Mode	            Mode of the song (0 or 1)
* Speechiness	      How likely the song is an audio is speech
* Tempo	            Tempo of the song (values between 0 and 250)
* Time Signature	  How many beats are contained in each measure (values between 0 and 5)
* Valence	          The musical positiveness (values between 0 and 1)
* Popularity	      Popularity of the song (0 to 100)

## Project Plan
Techniques
*	Data Visualisation using Matplotlib, Seaborn and Pandas Visualisation
*	Regression training
*	RFE Analysis
*	K-means
*	K nearest neighbour
## Milestones
* Establish GitHub: Establish the project which includes version control(GitHub) and project management a
* Data Handling: Clean data to suit our research needs removing all unessential data.
* Data Modelling: We need to sort 200k rows and ID the names of the songs.
* Overfitting: Memorizing training data and not being functional to unseen data.
* Regression: analyse data collected and see if there is a linear relationship between song duration and popularity loudness and tempo. compare all the different variables and see which has pair has the best R2 value.
* Need K mean and k nearest neighbour

