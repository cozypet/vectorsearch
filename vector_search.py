import requests
import pymongo


def get_embedding(query):
    # Define the OpenAI API url and key.
    url = "https://api.openai.com/v1/embeddings"
    openai_key = "xxxxx"  # Replace with your OpenAI key.

    # Call OpenAI API to get the embeddings.
    response = requests.post(
        url,
        json={"input": query, "model": "text-embedding-ada-002"},
        headers={
            "Authorization": f"Bearer {openai_key}",
            "Content-Type": "application/json",
        },
    )

    if response.status_code == 200:
        return response.json()["data"][0]["embedding"]
    else:
        raise Exception(f"Failed to get embedding. Status code: {response.status_code}")


def find_similar_documents(embedding):
    url = "mongodb+srv://xxx:xxx@clusteropp.bofm7.mongodb.net/?retryWrites=true&w=majority"  # Replace with your MongoDB url.

    try:
        client = pymongo.MongoClient(url)
        print("Connected to MongoDB")
        db = client["sample_mflix"]
        collection = db["embedded_movies"]

        # Query for similar documents.
        documents = list(
            collection.aggregate(
                [
                    {
                        "$search": {
                            "index": "moviesPlotIndex",
                            "knnBeta": {
                                "vector": embedding,
                                "path": "plot_embedding",
                                "k": 5,
                            },
                        }
                    },
                    {"$project": {"_id": 0, "plot": 1, "title": 1}},
                ]
            )
        )
        return documents

    finally:
        client.close()


def main():
    query = "oiseaux bleu"  # Replace with your query. Tested words: oasis, money, oiseaux bleu, an explorer, archeologist adventure in india

    try:
        embedding = get_embedding(query)
        # print(embedding)
        documents = find_similar_documents(embedding)
        for document in documents:
            print(str(document) + "\n")
            print()
    except Exception as err:
        print(err)


main()
