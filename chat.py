"""
$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDWv2VB6Bnn0a8lWunuVl_S5HZmcWysIQs")

# Create the model
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
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

print ("\n---------------------------\nwrite \"exit\" to end session\n---------------------------\n\n ")
while True:
    user_input = input("You: ")
    if user_input.lower() in "exit":
        break

    response = chat_session.send_message(user_input)
    print(f"AI: {response.text}\n-----------------------------------------------------------------\n")