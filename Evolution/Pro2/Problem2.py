import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('GOOGLE_GEMINI_API_KEY')

genai.configure(api_key=api_key)

file_path = 'sentences.txt'
df = pd.read_csv(file_path, delimiter='\t') 

def categorize_sentence(sentence):
    prompt = f"Categorize the following sentence into one of these categories: Sports, Business/Finance, Science/Technology.\n\nSentence: \"{sentence}\"\nCategory:"
    
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    category = response.text.strip().split("\n")[0] 
    return category

df['Category'] = df['Sentence'].apply(categorize_sentence)

df = df.rename(columns={'Sentence': 'Sentences'})

print(df)

output_file_path = 'categorized_sentences.csv'
df.to_csv(output_file_path, index=False)

print(f"Categorized sentences saved to {output_file_path}")
