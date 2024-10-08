import pdfplumber
import google.generativeai as genai

# Step 1: Extract text from the PDF
def extract_pdf_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

# Step 2: Load the PDF and extract the text
pdf_path = "Data Mining.pdf"
document_content = extract_pdf_text(pdf_path)

# Step 3: Configure the Generative AI model
genai.configure(api_key="AIzaSyDWv2VB6Bnn0a8lWunuVl_S5HZmcWysIQs")

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# Step 4: Start a chat session with the PDF content as context
chat_session = model.start_chat(
    history=[
    ]
)
chat_session.send_message("This chat is based on the following PDF document:")
chat_session.send_message(document_content)

# Step 5: Chat with the model
print("\n---------------------------\nWrite 'exit' to end session\n---------------------------\n\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Send user input to the model
    response = chat_session.send_message(user_input)
    print(f"AI: {response.text}\n-----------------------------------------------------------------\n")
