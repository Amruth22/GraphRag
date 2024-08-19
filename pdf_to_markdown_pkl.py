import os
import nest_asyncio  # noqa: E402
nest_asyncio.apply()
from llama_parse import LlamaParse
import pickle

def load_or_parse_data():
    # Get Free Api in this link "https://cloud.llamaindex.ai/login"
    llamaparse_api_key=''
    # Initialize LlamaParse
    parser = LlamaParse(api_key=llamaparse_api_key, result_type="markdown")
    
    # Parse the data from the PDF
    llama_parse_documents = parser.load_data([r"D:\vertexai\microsoft_hackthon\250884_2_english_01042024.pdf"])
    
    # Save the parsed data
    with open(data_file, "wb") as f:
        pickle.dump(llama_parse_documents, f)
    
    return llama_parse_documents

# Example usage
# provide the path to save the pickle file
data_file = r"D:\vertexai\microsoft_hackthon\parsed_data.pkl"
parsed_data = load_or_parse_data()

# Now you can work with `parsed_data` which contains the plain markdown of the PDF
