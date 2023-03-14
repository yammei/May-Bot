from dotenv import load_dotenv
from RequestGPT import *
import subprocess
import re

RGPT = RequestGPT()

class Read():

    def read_msgs(client):

        @client.event
        async def on_ready():
            print(f'{client.user.name} has connected to Discord!')


        @client.event
        async def on_message(message):

            # Prevent self-recursion
            if message.author == client.user:
                return
            
            # Help Command
            if message.content.startswith('.help'):
                if message.content[1:5] == 'help':
                    expression = message.content[6:]
                    msg1 = "**Hello, I'm May Bot ! How may I help you? ✩‧₊˚** \n"
                    msg2 = "Commands: \n\n"
                    msg3 = "1. I can calculate any arithmetic expression ! \n"
                    msg4 =  "<Ex: .calc (2+2)**3/4> \n\n"
                    msg5 = "2. Save and view reminders with .me.new and .me.view like so: \n"
                    msg6 = "<Ex: .me.new Grocery List: Eggs, Milk, Spring Onions.> \n\n"
                    msg7 = "3. I can request OpenAI's ChatGPT to answer prompts for you. \n"
                    msg8 = "<Ex: .cgpt What is the definition of Concurrency?>"
                    await message.channel.send(msg1 + '```md\n' + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8 + '\n``` ')
                    return

            # Calculate Function
            if message.content.startswith('.calc'):
                expression = message.content[6:].replace("^","**")
                allowed = ['pow','max','min','int','sum','floor','ceil','sorted','reversed']
                pattern = re.compile('[a-zA-Z]')
                check = bool(pattern.search(expression))
                if check:
                    i = 0
                    for functions in allowed:
                        i += 1
                        if functions in expression:
                            await message.channel.send('The answer to ' + expression.replace("**","^") + ' is: ' + "**" + str(eval(expression)) + "**")
                            return
                        if i == len(allowed):
                            await message.channel.send('https://tenor.com/view/caught-in-4k-caught-in4k-chungus-gif-19840038')
                            return
                else:
                    await message.channel.send('The answer to ' + expression.replace("**","^") + ' is: ' + "**" + str(eval(expression)) + "**")
                        

            # Save Author Reminders
            if message.content.startswith('.me.new'):
                user_input = message.content[7:].replace("```","")
                file_name = str(message.author) + ".txt"

                with open("/Users/NAME/Projects/Personal/MayBot/User_Data/" + str(file_name), "w") as f:
                    f.write(user_input)
                    return 

            # View Author Reminders
            if message.content.startswith('.me.view'):
                file_name = str(message.author) + ".txt"

                with open("/Users/NAME/Projects/Personal/MayBot/User_Data/" + str(file_name), "r") as f:
                    await message.channel.send(f.read())
                    return 

            # Proud Mother
            if message.content == 'good girl':
                await message.channel.send('https://cdn.discordapp.com/attachments/1075159453315383427/1075196981829435402/happy.png')
                return

            # ChatGPT Function
            if message.content.startswith('.cgpt'):
                prompt = message.content[5:]
                # print(prompt)

                # Request ChatGPT API to answer the user's given prompt
                answer = RGPT.answer(prompt)

                # Post-processing 
                i = answer.find("\n")
                answer = answer[i:]

                await message.channel.send(answer)




            
                
