# -*- coding: utf-8 -*-
"""Movie_Review_Bot

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A9gOFRpPICwTkPneHg3acE-l8Zn7uqK7

##Package Installation

*   Sets the file encoding to UTF-8.
*   Metadata indicating automatic generation by Colab and original file location.
*   Installs necessary packages using pip.
*   Installs required libraries: openai, gradio, pandas, tensorflow, tensorflow_hub, numpy, requests, and beautifulsoup4.
"""

!pip install openai==0.28.1

!pip install gradio

!pip install pandas
!pip install tensorflow
!pip install tensorflow_hub
!pip install numpy

!pip install requests beautifulsoup4==4.12.2

"""##Library Imports

* Imports openai and getpass libraries for handling API interaction and secure input.
* Prompts the user to enter their OpenAI API key securely and sets the API key for use in the script.
"""

# Import required libraries
import openai
from getpass import getpass

# Prompt the user to enter the API key securely
api_key = getpass("Enter your OpenAI API key: ")

# Set the API key
openai.api_key = api_key

"""##File Handling

* Lists the contents of the /content directory to confirm the presence of the dataset.
* Imports pandas for data manipulation.
* Reads the Excel file containing movie ratings into a pandas DataFrame.
* Prints the column names and displays the first few rows of the DataFrame for inspection
Note: You need to upload the file <rating-short - Copy.xlsx> for the code to run
"""

# List the file in the content directory to make sure that you use the correct name of the file
!ls '/content/rating-short - Copy.xlsx'

# Import pandas library
import pandas as pd

# Define the file path for the dataset
file_path = '/content/rating-short - Copy.xlsx'

# Read the Excel file into a DataFrame
imdb_data = pd.read_excel(file_path)

# Print the actual column names in your DataFrame to make sure you use the correct name
print(imdb_data.columns)

"""##Data Preparation

* Extracts the 'tconst' and 'averageRating' columns into separate variables.
* Creates dictionaries mapping movie titles to their ratings and IMDb IDs.
"""

# Display the first few rows of the dataset to understand its structure
imdb_data.head()
# Define movies list of the column ' tconst', and ratings list of the column 'averageRating'
movies = imdb_data[' tconst']
ratings = imdb_data['averageRating']

# Display a few titles and ratings to verify
movies.head(), ratings.head()

# Create a dictionary mapping movie titles to ratings
title_to_rating = dict(zip(imdb_data['title'], imdb_data['averageRating']))
title_to_id = dict(zip(imdb_data['title'], imdb_data[' tconst']))

"""##Utility Functions

* Defines query_imdb() to retrieve the rating for a given movie title.
* Defines get_imdb_url() to construct the IMDb URL for a given movie title.
"""

# Import numpy library
import numpy as np

# Function to query IMDb for movie rating
def query_imdb(user_input):
    if user_input in title_to_rating:
        rating = title_to_rating[user_input]
        return f"The rating for {user_input} is {rating}"
    else:
        return f"{user_input} not found in the dataset."

# Function to get IMDb URL for a movie
def get_imdb_url(user_input):
  # Find the row corresponding to the movie name
  row = imdb_data.loc[imdb_data['title'] == user_input]

  if not row.empty:
    imdb_id = row[' tconst'].values[0]  # Extract the ' tconst' value
    url = f"https://www.imdb.com/title/{imdb_id}/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    return url, headers
  else:
    return None, None

"""##Chatbot Functionality

* Imports openai and gradio libraries again for completeness.
*Defines initial messages for the chatbot, setting the role and content for system messages.
*Implements CustomChatGPT() function to handle user input, query the IMDb dataset, generate a response using OpenAI's API, and integrate the IMDb response into the ChatGPT reply.
"""

# Import additional libraries
import openai
import gradio as gr

# Define initial messages for the chatbot
messages = [{"role": "system", "content": "You are a movie expert. When responding, always structure your answer into three distinct sections with headings: Summary, Analysis, and Famous Comments. Provide a concise response for each section."}]

# Custom ChatGPT function to handle user input
def CustomChatGPT(user_input):
    # Query IMDb dataset
    imdb_response = query_imdb(user_input)

    # Get IMDb URL
    imdb_url, _ = get_imdb_url(user_input)
    if imdb_url:
        imdb_response += f"\n\nIMDb URL: {imdb_url}"

    # Append user input to messages
    messages.append({"role": "user", "content": user_input})

    # Generate ChatGPT response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]

    # Integrate IMDb response into the ChatGPT reply
    chatgpt_reply_with_imdb = f"{imdb_response}\n\n{ChatGPT_reply}"

    # Append ChatGPT reply to messages
    messages.append({"role": "assistant", "content": chatgpt_reply_with_imdb})
    return chatgpt_reply_with_imdb

"""##Gradio Interface

* Creates a Gradio interface with the function CustomChatGPT, taking text input and providing text output.
* Launches the Gradio interface with sharing enabled for accessibility.
Note: The link expires in 72 hours so it's needed to relaunch the code for sharing purpose.
"""

# Create a Gradio interface.
demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Movie Review Pro")

# Launch the Gradio interface with sharing enabled
demo.launch(share=True)
