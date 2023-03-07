# --- MANUAL TEMPLATE ---
# Import libraries
from docx import Document
from docx.shared import Inches
import openai
import credentials

#%%
# --- CHATGPT PROMPT  ---
header = input("What is the header of the document?")
prompt = input("What do you want to document?")

openai.api_key = credentials.OpenAI_Key
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message)
answer = completion.choices[0].message.content

#%%
# --- CREATE DOCUMENT ---
# Open template document `hello_world.docx`
document = Document('template.docx')

# Clear document
document._body.clear_content()

# Add title
document.add_heading(header, 1)

# Add paragraph
p = document.add_paragraph(answer)

# Save document
#document.save('doc2.docx')

# Save document on desktop with name of the first three word in the header
document.save('/Users/nilsjennissen/Desktop/' + header.split()[0] +' '+  header.split()[1] +' '+ header.split()[2] + '.docx')
