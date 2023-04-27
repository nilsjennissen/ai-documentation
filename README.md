# AI Documentation Generator


Automate your documentation process with AutoDoc, a smart and sophisticated tool that leverages the power of OpenAI API to auto-generate Word and README documentations.

## 🧭 Project Overview

AutoDoc saves you time and effort by automatically generating well-structured and coherent documentation for your software projects. With an easy-to-use interface and advanced natural language processing techniques, AutoDoc ensures that your documentation is informative, accurate, and engaging.

**⏱ Estimated time needed:** 3h

## 🚧 Prerequisites

Before diving into AutoDoc, make sure you have the following prerequisites:

1. Python 3.7 or higher
2. OpenAI API key
3. A stable internet connection

## 🎛 Project Setup

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourname/autodoc.git
   ```
2. Install all dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
4. Run one of the applications:
   ```
   python ai_readmy.py 
   python chatgpt.py
   ```

## 📦 Project Structure

The project is organized as follows:

- `main.py`: The main entry point of the application
- `requirements.txt`: Lists all the Python dependencies needed for the project
- `autodoc/`: The core package containing the following modules:
   - `api.py`: The OpenAI API wrapper class
   - `generator.py`: The documentation generator class
   - `utils.py`: Helper functions and utilities
- `assets/`: Contains images and other supporting files for the project
- `examples/`: Contains sample input files for testing and demonstration purposes
- `output/`: The directory where generated documentations will be saved

## 🗄️ Data

AutoDoc uses a combination of OpenAI API and predefined templates to auto-generate documentation. The input data consists of:

1. **Source code files:** AutoDoc reads your source code files (e.g., `.java`, `.py`, `.js`) to extract relevant information, such as methods, classes, and comments.
2. **Configuration files:** You can provide AutoDoc with specific configuration files (e.g., `.json`, `.toml`) that define your project's structure, dependencies, and other relevant information.

For example, consider this Python script as an input:

```python
# my_script.py

def add(a, b):
    """
    Add two numbers together and return the result.
    """
    return a + b
```

After processing the source code, AutoDoc generates a corresponding documentation using the OpenAI API to provide contextual descriptions and explanations.

## 📚 References

AutoDoc is built using the following resources:

1. OpenAI API: [Official Documentation](https://beta.openai.com/docs/)
2. Python: [Official Website](https://www.python.org/)
3. GitHub: [Git Introduction](https://guides.github.com/activities/hello-world/)

## 🏆 Conclusion

AutoDoc is an invaluable tool for developers who want to streamline their documentation process. With minimal setup and an easy-to-use interface, you can generate professional and high-quality documentations to keep your projects well-documented and up-to-date.

Join the AutoDoc community and see how it transforms your software development workflow.

## 🤝 Contributions

Feel free to contribute to the project by creating pull requests, reporting bugs, or suggesting new features. Your feedback and contributions will help make AutoDoc even better!