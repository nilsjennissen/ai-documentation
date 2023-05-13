# --- MANUAL TEMPLATE ---
# Import libraries
import openai
import credentials
from pathlib import Path

#%%
# --- DIRECTORY TREE  ---

class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root

        # Specify criteria to exclude directories/files
        children = sorted(list(path
                               for path in root.glob('*')  # for path in root.iterdir() <- all files
                               if not path.name.startswith('.') and criteria(path)),  # if criteria(path)),
                          key=lambda s: str(s).lower())
        count = 1
        for path in children:
            is_last = count == len(children)
            if path.is_dir():
                yield from cls.make_tree(path,
                                         parent=displayable_root,
                                         is_last=is_last,
                                         criteria=criteria)
            else:
                yield cls(path, displayable_root, is_last)
            count += 1

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def displayname(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    def displayable(self):
        if self.parent is None:
            return self.displayname

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.displayname)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))


# Call the function with the path to the directory you want to print and
def tree_with_exception(path, criteria=None):
    if criteria is None:
        criteria = lambda path: not (path.name.startswith('.') or path.name == '__pycache__' or path.name == 'venv')
    paths = DisplayablePath.make_tree(Path.home() / path, criteria=criteria)
    for path in paths:
        # Save the output to a text string with linebreaks to use later
        tree = '\n'.join([path.displayable() for path in paths])
    return tree

path = input("\nWhere are the documents? PycharmProjects/simulations: ")

structure = tree_with_exception(path)

# --- CHATGPT PROMPT  ---

openai.api_key = credentials.OpenAI_Key

description = input("\nWrite a little about the project: ")

prompt = f'''Write an interesting README.md with the structure: \n
# 🧭 Project Overview 
## ⏱ Estimated time needed: 3h
## 🚧 Prerequisites
## 🎛 Project Setup
## 📦 Project Structure
## 🗄️ Data
## 📚 References
## 🏆 Conclusion
## 🤝 Contributions

The project is about: 
{description}

In the project structure, use the predefined dir_tree: 
{structure}
'''

def gpt_docu(prompt):
    try:
      print(f"Prompt: {prompt}")
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