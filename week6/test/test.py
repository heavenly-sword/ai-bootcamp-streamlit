import os
import sys

# Tell Python to include the parent folder (week6) in its path checks
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now your import will work perfectly!
from logics import customer_query_handler as cqh

# user_query = "I'm interested in learning about artificial intelligence."
# result = cqh.identify_category_and_courses(user_query)
# print(result)

sample_input = [{'category': 'Programming and Development','course_name': 'Web Development Bootcamp'},
                {'category': 'Data Science & AI', 'course_name': 'Data Science with Python'},
                {'category': 'Data Science & AI', 'course_name': 'AI and Machine Learning for Beginners'}]


product_details = cqh.get_course_details(sample_input)
# print(product_details)

# Testing the function to make sure it works
# This part should not be included as part of the Python script.

user_query = f"""Do you have any coding or data related courses that are under $1000 """

response = cqh.generate_response_based_on_course_details(user_query, product_details)
print(response)