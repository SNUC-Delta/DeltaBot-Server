import os
import openai
openai.organization = "org-ASQj9plDYyS0mGN6zKuhAs3e"
openai.api_key = "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"

def solve(question):
    solutions = []
    for i in question:
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "I will provide questions. You have to respond with the solutions to each question such that, there is an algorithm block - where you have to give the algorithm for the program, with each algorithm starting with Step 1:, Step 2:, Step 3:, and so on. After that you have to provide the program solution. After that you have to provide the Output (whatever you predict the output to be of the program).  Do not have ANY other text other than that. "},
            {"role": "user", "content": i}
        ]
        )
        solutions.append(completion.choices[0].message["content"])

    return solutions
