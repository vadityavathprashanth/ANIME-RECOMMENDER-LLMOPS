from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt


# Animerecommender class that uses a retriever and a language model to provide anime recommendations.
class AnimeRecommender:
    def __init__(self, retriever, api_key:str, model_name:str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()

        # Initialize the RetrievalQA chain with the retriever and the language model
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type= "stuff",
            retriever= retriever,
            return_source_documents= True,
            chain_type_kwargs= {"prompt":self.prompt}
        )

    # Method to get anime recommendations based on a query
    def get_recommendations(self, query:str):
        result = self.qa_chain.invoke({"query": query})
        return result['result'] 
    