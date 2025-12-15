from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv


load_dotenv()

openai_client = OpenAI()

# Vector Embedding
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

# Vector Db Set up

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning_rag",
    embedding= embedding_model
)

def process_query(query: str):
    print("Searching Chunks : ", query)
    search_result = vector_db.similarity_search(query=query)
    context = "\n\n\n".join([ f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_result ])

    SYSTEM_PROMPT = f"""
    You are a helful AI Assistant who answers user query based on available context retrived from a PDF file alog with page_contents and page_number


    You should only ans the user based on the following context and navigate the user to open the right number to know more

    Context : 
    {context}
    """ 
    response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        { "role" : "system", "content" : SYSTEM_PROMPT},
        { "role" : "user", "content" : query}

    ]
    )
    print(f"🤖: {response.choices[0].message.content}")
    return response.choices[0].message.content

