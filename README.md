***Disclaimer***: This is only a prototype so there is a limit number of fims to search for. You can check which films are available to be searched in this [excel file](https://github.com/quynhanh010106/movie_review_bot/blob/main/rating-short%20-%20Copy.xlsx)

# Movie Review Chatbot

## Introduction:

The objective of this project was to develop a chatbot that can quickly and efficiently provide essential information about films. Leveraging the capabilities of the OpenAI API, the chatbot is designed to respond to user queries about movies with relevant and succinct details. This publication outlines the development process, the current limitations, and potential future improvements.

[Documentation](https://docs.google.com/document/d/1D4WnBWnADgN_aBQ1ziurc1AYA_gxQpQxybC_ayRNqS4/edit?usp=drive_link)

## Demo:

[![Watch the video](https://github.com/quynhanh010106/movie_review_bot/blob/main/moviereviewchatbot.png)](https://www.youtube.com/watch?v=NhGjFRmOusU)

## Installation:
To run the web application, you need to download the [code file](https://github.com/quynhanh010106/movie_review_bot/blob/main/movie_review_bot.py) and follow the instruction. This code will generate a link at the end to the web application using a Gradio interface.

I use Google Colab to make this, so you can try upload this file (and don't forget the [excel file](https://github.com/quynhanh010106/movie_review_bot/blob/main/rating-short%20-%20Copy.xlsx)) to google colab if it doesn't run in your IDE.

## Methodology:
- **Data Collection:** The dataset for this chatbot was sourced from IMDb, focusing on a selection of 100 films listed in the file "rating-short-copy". As IMDb provides free access to datasets through IDs, the initial dataset required manual pairing of film titles with their corresponding IDs.
- **Development Environment:** The project was developed on Google Colab, a cloud-based platform that facilitates Python programming and integration with various APIs. The OpenAI API was used to process user queries and generate responses.
- **AI Integration:** The chatbot’s development involved extensive use of AI tools. Gemini and ChatGPT were instrumental in debugging code and enhancing the chatbot's functionalities. These tools provided valuable support in overcoming technical challenges and improving the chatbot's performance.

## Features:
- **Quick Information Retrieval:** The chatbot delivers fast and concise information about films, including summaries, ratings, and other relevant details.
User-Friendly Interface: The chatbot interacts with users in a natural language format, making it easy to use for individuals seeking quick film information.

## Limitations:
- **Prototype Stage:** As a prototype, the chatbot is currently limited to providing information on only 100 films. The dataset includes a small, manually curated list of films, which constrains the chatbot’s utility.

## Future Improvements:
- **Automated Data Expansion:** Future development will focus on automating the data collection process to expand the dataset significantly. This involves creating a system to dynamically retrieve film IDs from IMDb based on user input and automatically updating the dataset.
- **Enhanced Functionality:** Plans to integrate images and other multimedia content into the chatbot’s responses will improve user engagement and the overall user experience.
- **Scalability:** Optimizing the chatbot to handle a larger dataset efficiently will be crucial for future scalability.

## Conclusion:
The Movie Review Chatbot represents a significant milestone in my journey of learning and applying Python and AI technologies. Despite its current limitations, the project demonstrates the potential of combining Python programming with powerful AI tools to create useful and interactive applications. Future improvements aim to enhance the chatbot’s functionality and expand its dataset, making it a more robust and versatile tool for film enthusiasts.

## Dataset Credit: 
The dataset used in this project is credited to IMDb’s free source.

## Acknowledgments:
I would like to extend my gratitude to the developers of Gemini and ChatGPT for their invaluable assistance throughout the development of this project. Their support was crucial in overcoming the challenges encountered during the development process.

## Contact Information:
For more information about this project, please contact: ngquynhanh.forwork@gmail.com or on LinkedIn as [Quỳnh Anh Nguyễn](https://www.linkedin.com/in/anh-nguyenquynh/)
