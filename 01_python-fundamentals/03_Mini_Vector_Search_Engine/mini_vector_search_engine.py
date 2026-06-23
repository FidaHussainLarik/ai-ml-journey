# helper function for printing borders
import time 
def print_border(symbol):
    print(60 * symbol)

def search_engine(query):
    print(60 * '-')
    print("Evaluating Documents....")
    print(60 * '-')
        
    if len(documents) == 0:
        return 'No documents exist'
    
    for doc in documents:
        score = 0
        splitted_doc = doc.split()

        for query_word in query:
            if query_word in splitted_doc:
                score += 1
                
        print(score)
        break

    return doc
        
    

        
    



<<<<<<< HEAD

print_border('=')
=======
print_border()
>>>>>>> e1078212c9e7ede667eb0a775d9799e4df9cc57f
print('     MINI VECTOR SEARCH ENGINE       ')
print_border('=')

documents = [
    "Python is a high-level programming language commonly used in data science and artificial intelligence.",

    "Machine learning is a subset of artificial intelligence where computers learn patterns from data.",

    "Deep learning uses neural networks with multiple layers to learn complex patterns.",

    "A neural network consists of interconnected nodes called neurons that process information.",

    "Large Language Models are AI systems trained on massive amounts of text data.",

    "Tokens are small pieces of text that language models process instead of entire sentences.",

    "Embeddings convert text into numerical vectors that capture semantic meaning.",

    "Vector databases store embeddings and enable similarity search across documents.",

    "RAG stands for Retrieval Augmented Generation and combines search with language models.",

    "Prompt engineering is the practice of designing effective inputs for language models.",

    "LangChain is a framework used to build applications powered by large language models.",

    "Fine-tuning adapts a pre-trained model to perform better on a specific task.",

    "Hallucination occurs when a language model generates incorrect or fabricated information.",

    "Cosine similarity is a mathematical technique used to measure similarity between vectors.",

    "Transformers are neural network architectures that power modern language models."
]
greeting_messages = ['Good morning!','Good afternoon', 'Good night'] # Will add the fn which greet users according to the time they are using this RAG.


print("\nUser Query ")
query = input('>')

query = query.split() # Converting string into a list of words for word by word comparision to documents



matched_doc = search_engine(query)

<<<<<<< HEAD

print_border('-')
print('TOP MATCH')
print_border('-')

print(matched_doc)


print_border('=')
=======
print_border('=')
>>>>>>> e1078212c9e7ede667eb0a775d9799e4df9cc57f
