from setuptools import setup, find_packages

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='Akhila',
    author_email='akhilapemmaraju9@gmail.com',
    install_requires=['numpy', 'pandas', 'matplotlib', 'seaborn','notebook','pyYAML','path','tqdm','types-PyYAML','openai','langchain','streamlit','python-dotenv','PyPDF2'],
     packages=find_packages()
)

            







