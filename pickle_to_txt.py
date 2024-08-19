import pickle
import markdown
from bs4 import BeautifulSoup

# Step 1: Load the pickle file
print("Step 1: Loading pickle file...")
with open(r'D:\vertexai\microsoft_hackthon\parsed_data.pkl', 'rb') as file:
    markdown_content = pickle.load(file)

# Step 2: Process the content
print("\nStep 2: Processing content...")
processed_content = []
for i, doc in enumerate(markdown_content):
    if hasattr(doc, 'get_text'):
        content = doc.get_text()  # Use the get_text method if available
    elif hasattr(doc, 'text'):
        content = doc.text  # Fallback to the text attribute if get_text is not available
    else:
        content = str(doc)  # Fallback to string conversion
    processed_content.append(content)
    print(f"Processed document {i+1}/{len(markdown_content)}, content length: {len(content)}")

final_content = '\n'.join(processed_content)
print(f"Final combined content length: {len(final_content)}")

# Step 3: Convert Markdown to HTML
print("\nStep 3: Converting to HTML...")
html_content = markdown.markdown(final_content)
print(f"HTML content length: {len(html_content)}")

# Step 4: Parse HTML to plain text
print("\nStep 4: Parsing HTML to plain text...")
soup = BeautifulSoup(html_content, 'html.parser')
plain_text = soup.get_text()

# Debugging: Check the plain text length and sample
print(f"Final plain text length before writing: {len(plain_text)}")

# Step 5: Write the plain text to multiple text files to avoid truncation
chunk_size = 100000  # Adjust the chunk size as needed
for i in range(0, len(plain_text), chunk_size):
    with open(rf'D:\vertexai\microsoft_hackthon\output_part_{i//chunk_size + 1}.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(plain_text[i:i + chunk_size])

# Optional: Write the HTML content directly to a file for inspection
# with open(r'D:\vertexai\microsoft_hackthon\output_html.html', 'w', encoding='utf-8') as html_file:
#     html_file.write(html_content)

with open(r'D:\vertexai\microsoft_hackthon\final.txt', 'w', encoding='utf-8') as text_file:
    text_file.write(final_content)

print("Conversion completed. Please check the output files.")
