README

This repository contains code files for generating plot embeddings using OpenAI API, setting up an Atlas Search index, and querying the index using a Python script.

Files

atlas.js - JavaScript function that generates plot embeddings using OpenAI API and updates documents in a MongoDB collection with the embeddings.
atlas_search.json - JSON definition for setting up an Atlas Search index with the necessary configuration for the plot_embedding field.
query.py - Python script to run queries against the Atlas Search index.
Prerequisites
Before running the code in this repository, make sure you have the following prerequisites:

OpenAI API Key - Obtain your OpenAI API key from the OpenAI website. This key will be used to generate plot embeddings.
MongoDB Atlas Cluster - Set up a MongoDB Atlas cluster where the sample_mflix database and movies collection exist. Replace the placeholders in the code with your actual database and collection names.
Values in App Services - In your MongoDB Atlas project, set up a value named "openAI_value" and store your OpenAI API key as the value. This value will be used by the JavaScript function to authenticate with the OpenAI API.
Instructions
Follow these steps to set up and run the code:

Get OpenAI API Key:

Obtain your OpenAI API key from the OpenAI website.
Store your API key securely as it will be used to authenticate API requests.
Modify Trigger Function:

Open the atlas.js file and replace the placeholder with your OpenAI API key:
javascript
Copy code
const openai_key = context.values.get("openAI_value");
Replace the database and collection names in the following lines with your actual database and collection names:
javascript
Copy code
const db = mongodb.db('sample_mflix');
const collection = db.collection('movies');
Build Search Index:

Create a new Atlas Search index in your MongoDB Atlas cluster using the atlas_search.json file. This index will enable efficient searching based on plot embeddings. You can use the MongoDB Atlas UI or the command-line interface to create the index.
Run Python Query Script:

Ensure you have Python installed on your machine.
Open the query.py file and replace the placeholder with your actual Atlas Search index name:
python

index_name = "your_index_name"
Run the vector_search.py script using the command:
shell

python3 vector_search.py

Notes

Make sure to handle the OpenAI API key securely and avoid exposing it in public repositories or code.
The provided code assumes you have a working MongoDB Atlas cluster and the necessary permissions to perform the required operations.
For more detailed information and troubleshooting, refer to the official MongoDB and OpenAI API documentation.
