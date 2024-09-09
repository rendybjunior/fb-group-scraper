"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
import pandas as pd
# from google.colab import userdata

genai.configure(api_key="x")

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


history=[
]


# Define your method 'my_method'
def classify_post(post_text):
  """
  Processes the 'post_text' and returns a classification result.

  Args:
    post_text: The text content of a post.

  Returns:
    The classification result for the post.
  """
  chat_session = model.start_chat(history=history)
  response = chat_session.send_message(post_text)
  result = ""
  try:
    result = response.candidates[0].content.parts[0].text.strip()
  except Exception:
    print(response)

  return result


# # Replace 'your_file_path' with the actual path to your CSV file in Google Drive
file_path = '~/Downloads/2024-09-08 5_14pm - Sheet1 (1).csv'

# # Read the CSV file into a Pandas DataFrame
df = pd.read_csv(file_path)

# Create an empty list to store the classification results
post_classes = []

# Iterate through each row of the DataFrame
import time
start_time = time.time()
i = 0
for index, row in df.iterrows():
  # Get the 'POST_TEXT' from the current row
  post_text = row['POST_TEXT']

  # Call 'my_method' and append the result to the list
  classification_result = classify_post(post_text)
  post_classes.append(classification_result)
  i += 1
end_time = time.time()
duration = end_time - start_time
print(f"Gemini execution time: {duration:.6f} seconds for {i} rows")

# Add the classification results as a new column to the DataFrame
df['POST_CLASS'] = post_classes


# # Print the DataFrame with the new 'POST_CLASS' column
print(df.head())

output_file_path = 'output_file.csv'

# Write the DataFrame back to a CSV file in Google Drive
df.to_csv(output_file_path, index=False)