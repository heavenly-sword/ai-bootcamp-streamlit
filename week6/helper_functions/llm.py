import os
from dotenv import load_dotenv
from google import genai
import tiktoken
import json

load_dotenv()

# Pass the API Key to the GenAI Client
client = genai.Client(api_key=os.environ.get("OPENAI_API_KEY"))

def get_embedding(input, model='gemini-embedding-2-preview'):
    response = client.embeddings.create(
        input=input,
        model=model
    )
    return [x.embedding for x in response.data]

# This is the "Updated" helper function for calling LLM
def get_completion(prompt, model="gemini-3.1-flash-lite", temperature=0, top_p=1.0, max_tokens=256, n=1, json_output=False):
    # if json_output == True:
    #   output_json_structure = {"type": "json_object"}
    # else:
    #   output_json_structure = None

    # messages = [{"role": "user", "content": prompt}]
    # response = client.chat.completions.create( #originally was openai.chat.completions
    #     model=model,
    #     messages=messages,
    #     temperature=temperature,
    #     top_p=top_p,
    #     max_tokens=max_tokens,
    #     n=1,
    #     response_format=output_json_structure,
    # )
    # return response.choices[0].message.content

    # Set up config options for Google GenAI
    config_args = {
        "temperature": temperature,
        "max_output_tokens": max_tokens,
    }
    
    # Handle JSON output formatting if requested
    if json_output:
        config_args["response_mime_type"] = "application/json"
        
    # Call the correct Google GenAI SDK method
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=config_args
    )
    
    return response.text

# This a "modified" helper function that we will discuss in this session
# Note that this function directly take in "messages" as the parameter.
# def get_completion_by_messages(messages, model="gemini-3.1-flash-lite", temperature=0, top_p=1.0, max_tokens=1024, n=1):
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=temperature,
#         top_p=top_p,
#         max_tokens=max_tokens,
#         n=1
#     )
#     return response.choices[0].message.content

def get_completion_by_messages(messages, model="gemini-3.1-flash-lite", temperature=0, top_p=1.0, max_tokens=1024, n=1):
# 1. Convert OpenAI message formats to Gemini 'contents' format
    # OpenAI uses "user"/"assistant". Gemini uses "user"/"model".
    gemini_contents = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        gemini_contents.append({
            "role": role,
            "parts": [{"text": msg["content"]}]
        })
    
    # 2. Build the configuration dictionary
    config_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_output_tokens": max_tokens,
    }
    
    # 3. Call the correct Google GenAI method
    response = client.models.generate_content(
        model=model,
        contents=gemini_contents,
        config=config_args
    )
    
    return response.text

# These functions are for calculating the tokens.
# ⚠️ These are simplified implementations that are good enough for a rough estimation.
def count_tokens(text):
    encoding = tiktoken.encoding_for_model('gemini-3.1-flash-lite')
    return len(encoding.encode(text))

def count_tokens_from_message(messages):
    encoding = tiktoken.encoding_for_model('gemini-3.1-flash-lite')
    value = ' '.join([x.get('content') for x in messages])
    return len(encoding.encode(value))

filepath = './data/courses-full.json'
# filepath = 'courses-full.json'

with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)

def get_course_details(list_of_category_n_course: list[dict]):
    course_names_list = []
    for x in list_of_category_n_course:
        course_names_list.append(x.get('course_name')) # x["course_name"]

    list_of_course_details = []
    for course_name in course_names_list:
        list_of_course_details.append(dict_of_courses.get(course_name))
    return list_of_course_details