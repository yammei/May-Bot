from dotenv import *
import openai
import os

class RequestGPT:

    def answer(self, prompt):

        # Retrieve OpenAI Token from .env file
        load_dotenv()
        TOKEN = os.getenv('OPENAI_TOKEN')
        openai.api_key = str(TOKEN)

        '''
        prompt = "whats the definition of cereal"
        '''

        # Response request and settings
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # ChatGPT response information
        say = response.choices[0].text
        print(str(response) + "\n" + str(response.choices) + "\n" + say)
        return say

    '''
    answer("")
    '''