# Questions from the Open Trivia Data Base API
# www.opentdb.com/api_config.php
# https://opentdb.com/api.php?amount=10&category=17&difficulty=easy&type=boolean

# NB: slight reformatting of JSON was required: Deleted outer {} and first key-value pair in JSON
# the result is a valid list of python dictionaries that can be assigned to quesion_data.
question_data = [{"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "Igneous rocks are formed by excessive heat and pressure.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "Salt is 100% composed of Sodium.", "correct_answer": "False",
                  "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "An atom contains a nucleus.", "correct_answer": "True",
                  "incorrect_answers": ["False"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "An exothermic reaction is a chemical reaction that releases energy by radiating "
                              "electricity.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "An Astronomical Unit is the distance between Earth and the Moon.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "An average human can go two weeks without water.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "Celiac Disease is a disease that effects the heart, causing those effected to be unable "
                              "to eat meat.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "Water always boils at 100&deg;C, 212&deg;F, 373.15K, no matter where you are.",
                  "correct_answer": "False", "incorrect_answers": ["True"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "Not including false teeth; A human has two sets of teeth in their lifetime.",
                  "correct_answer": "True", "incorrect_answers": ["False"]},
                 {"category": "Science & Nature", "type": "boolean", "difficulty": "easy",
                  "question": "A plant that has a life cycle for more than a year is known as an annual.",
                  "correct_answer": "False", "incorrect_answers": ["True"]}]
