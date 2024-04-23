import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import  SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Set up the language model
embedding_model = GoogleGenerativeAIEmbeddings(google_api_key="AIzaSyC2Bztff9XtDCDrCJfMJ8py9JaT8VkwSlY", 
                                               model="models/embedding-001")


db_connection = Chroma(persist_directory="./chroma_db_", embedding_function = embedding_model)
# Set up the output parser
output_parser = StrOutputParser()
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
retriever = db_connection.as_retriever(search_kwargs={"k": 5})
# Set up the chat template
chat_template = ChatPromptTemplate.from_messages([
   SystemMessage(content="You are a Helpful AI Bot. You take the context and question from the user. Your answer should be based on the specific context."),
   HumanMessagePromptTemplate.from_template("""Answer the question based on the given context.\nContext:\n{context}\nQuestion:\n{question}\nAnswer:""")
])

chat_model = ChatGoogleGenerativeAI(google_api_key="AIzaSyC2Bztff9XtDCDrCJfMJ8py9JaT8VkwSlY", 
                                   model="gemini-1.5-pro-latest")
# Set up the RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | chat_template
    | chat_model
    | output_parser
)

# Define Streamlit a
st.title("🤖RAG System")
st.subheader("AI for Contextual Q&A")
st.header("📖Context:  Leave No Context Behind")

    # Get user input
user_question = st.text_input("Ask a question:")
if st.button("🖊Get Answer"):
    if user_question:
        response = rag_chain.invoke(user_question)
        st.write("💬 Answer:")
        st.write(response)
    else:
        st.warning("⚠️ Please enter a question.")


