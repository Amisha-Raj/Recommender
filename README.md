# Movie Recommender

## **Overview**

This is a Movie Recommender System built using BERT (Bidirectional Encoder Representations from Transformers) and cosine similarity. The system analyzes movie descriptions and recommends similar movies based on textual content.

## **Features**

Utilizes BERT embeddings to generate meaningful representations of movie descriptions.

Computes cosine similarity to find and recommend similar movies.

Efficient and scalable approach for content-based recommendations.

## **Tech Stack**
Python

Transformers (Hugging Face BERT)

Scikit-learn (for cosine similarity computation)

Pandas & NumPy (for data handling)

# How It Works

Preprocessing: Movie descriptions are tokenized and converted into embeddings using a pre-trained BERT model.

Embedding Calculation: Each movie’s description is converted into a numerical representation.

Similarity Computation: Cosine similarity is used to measure how close two movies are in the embedding space.

Recommendation: The system suggests movies with the highest similarity scores.

