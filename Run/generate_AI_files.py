import openai
import os
import sys


"""
This file generate awnser from the AI, it store them into the directory discussion
and increment the name of each file by 1
"""


# Set your OpenAI API key
openai.api_key = "" #Your Api key goes here.

conversation = []


def clear_directory(directory_path):
    # Iterate over all the files and subdirectories in the specified directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        # Check if the current item is a file
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)
        else:
            # If it's a subdirectory, remove it recursively
            clear_directory(file_path)
            os.rmdir(file_path)


def get_chatbot_response(user_input):
    role = "user"
    content = user_input

    # Create completion
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": role, "content": content}
        ]
    )

    # Return the response from the completion
    return completion.choices[0].message.content

def run_chatbot():

    if len(sys.argv) == 1:
        user_input = "HI! welcome to the AI podcast, we are both AI and we will discuss subjects. What do you want to talk about?"
    else:
        argument = str(sys.argv[1:])
        user_input = f"Hello! Welcome to my podcast, let's discuss about this subject: {argument}"

    response = get_chatbot_response(user_input)
    conversation.append(response)

    nbDeReponse = 0
    while True:

        #Stock la valeurs la reponse dans la conversation
        response = get_chatbot_response(conversation[-1])
        conversation.append(response)

        # check if file exists
        # then create a new file
        with open(f"discussion\\{nbDeReponse}.txt", 'w') as f:
            f.writelines(response)
        nbDeReponse +=1



clear_directory(".\discussion")
run_chatbot()
