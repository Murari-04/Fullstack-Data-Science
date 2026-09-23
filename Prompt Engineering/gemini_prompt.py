import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="Gemini RAG App",
    page_icon="🤖",
    layout="centered"
)

st.title("Prompt Engineering Using Gemini")

# Gemini API Key input
api_key = st.text_input(
    "Enter your Gemini API Key",
    type="password"
)

if api_key:

    # Create Gemini client
    client = genai.Client(api_key=api_key)

    # Dummy retriever for RAG demonstration
    def retriever_info(query):
        return "Explain about India's economy."

    # Main RAG function
    def rag_query(query):

        # Retrieve information
        retrieved_info = retriever_info(query)

        # Augment the user's query
        augmented_prompt = f"""
        User query: {query}

        Retrieved information:
        {retrieved_info}

        Please answer the user's query clearly and accurately.
        """

        # Generate response using the new Google GenAI SDK
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=augmented_prompt,
            config=types.GenerateContentConfig(
                temperature=1.0,
                max_output_tokens=1000,
                top_p=1.0,
                top_k=50,
                stop_sequences=["End"]
            )
        )

        return response.text.strip()

    # User query
    query = st.text_area(
        "💬 I am bot:",
        "How may I help you?"
    )

    # Generate button
    if st.button("🔍 Generate Response"):

        if not query.strip():
            st.warning("Please enter a query first.")

        else:
            with st.spinner("Generating response..."):

                try:
                    answer = rag_query(query)

                    st.success("✅ Response Generated!")

                    st.markdown(
                        f"**Answer:**\n\n{answer}"
                    )

                except Exception as e:
                    st.error(f"Error: {e}")

else:
    st.info("Please enter your Gemini API key to start.")

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit + Google Gemini API + Murari"
)