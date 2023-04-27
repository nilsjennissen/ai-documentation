# --- MANUAL TEMPLATE ---
# Import libraries
from docx import Document
from docx.shared import Inches
import openai
import credentials
import os

#%%
# --- CHATGPT PROMPT  ---

openai.api_key = credentials.OpenAI_Key

prompt = input("What project do you want to document?")

preprompt = f'''Write an interesting README.md with the structure: \n
🧭 Project Overview 
⏱ Estimated time needed: 3h
🚧 Prerequisites
🎛 Project Setup
📦 Project Structure
🗄️ Data
📚 References
🏆 Conclusion
🤝 Contributions

The project is about: {prompt}
'''

def gpt_docu(prompt):
    try:
      print(f"----- {prompt} -----")
      completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
          {"role": "user", "content": prompt}
        ]
      )

      answer = completion.choices[0].message.content
      for i in range(2):
          try:
              if answer[0] == "\n":
                  answer = answer[1:]
          except:
              pass


      return answer
    except:
      print("Something went wrong. Please try again.")


answer = gpt_docu(prompt)
print(answer)