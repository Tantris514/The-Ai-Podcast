import openai
import pyttsx3
import os
import subprocess

# Set your OpenAI API key
openai.api_key = "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"
MALE_VOICE_TOKEN = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
FEMALE_VOICE_TOKEN = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine = pyttsx3.init()
conversation = []

# initialise the file
with open("discussion.txt", 'w') as f:
    pass


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
    user_input = "HI! welcome to the AI podcast, we are both AI and we will discuss subjects. What do you want to talk about?"
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
            print(response)
            f.writelines(response)
        nbDeReponse +=1




clear_directory(".\discussion")
run_chatbot()
