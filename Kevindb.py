#next gen Kevin

import discord
import asyncio
import logging
import requests
from bs4 import BeautifulSoup
import random
import kev_queue

logging.basicConfig(level=logging.INFO)

soup = []
linkorder = 0


#------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        
        channel = client.get_channel(239504532734869505)
        await channel.send('I\'m back <:FeelsGoodMan:239511865120522240>')

        global msgQ
        msgQ = kev_queue.FixedSizeQueue(3)
        
        
#------------------------------------------------------------------------------------        
    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        
        msgQ.push(message.content)
        if msgQ.queue[2] == msgQ.queue[1] and msgQ.queue[2] == msgQ.queue[0]:
            await message.channel.send(message.content)

        message.content = message.content.lower()
        
        global soup
        global linkorder
 
# ------------------------------------------------------------------------------------          
        if 'kev' in message.content and '?' in message.content:
            if ' or ' in message.content:
                kev_ind = message.content.find('kev')
                string = str(message.content)
                string = string[kev_ind:]
                words = string.split(' ')
                words = words[1:]

                option = ''
                answers = []

                for word in words:
                    if word == 'or':
                        answers.append(option)
                        option = ''
                    elif '?' in word:
                        option = option + word[0 : len(word) - 1]
                        answers.append(option)
                        break
                    else:
                        option = option + word + ' '

                if len(answers) < 2 or '' in answers:
                    await message.channel.send('Either give me more choices or learn to type')
                    return
                j = random.randint(0, len(answers) - 1)
                await message.channel.send(answers[j])
                return
        
            if 'how' in message.content or 'chance' in message.content:
                j = random.randint(0, 100)
                string = 'About ' + str(j) + '%'
                await message.channel.send(string)
                return
            else:
                answers = ['yes', 'yeah', 'no', 'nah', 'nope', 'yup']
                j = random.randint(0, len(answers) - 1)
                await message.channel.send(answers[j])
                return
# ------------------------------------------------------------------------------------
    #set commands starting with '!'
        elif message.content.startswith('!'):
            if message.content.startswith('!roll'):
                rollan = random.randint(1, 100)
                if rollan < 31:
                    string = str(message.author.nick) + ' rolls: ' + str(rollan) + ' <:FeelsBadMan:239512099108159488>'
                elif rollan < 70:
                    string = str(message.author.nick) + ' rolls: ' + str(rollan) + ' <:pepeN:298529329938169856>'
                else:
                    string = str(message.author.nick) + ' rolls: ' + str(rollan) + ' <:FeelsGoodMan:239511865120522240>'

                await message.channel.send(string)
                
            if message.content.startswith('!yt'):
                linkorder = 0
                url = 'http://www.youtube.com/results?search_query=' + str(message.content)[4:] + '&gl=US'
                r = requests.get(url)
                data = r.text
                soup = BeautifulSoup(data, 'html.parser')
                for link in soup.find_all('a'):
                    link = link.get('href')
                    if str(link).startswith('/watch'):
                        strang = 'http://www.youtube.com' + str(link)
                        await message.channel.send(strang)
                        return

            if message.content.startswith('!nextlink'):
                linkorder = linkorder + 2
                if soup == []:
                    await message.channel.send('No previous searches')
                    return

                ordr = linkorder + 0
                counter = 11
                for link in soup.find_all('a'):
                    link = link.get('href')
                    if str(link).startswith('/watch'):
                        if ordr > 0:
                            ordr = ordr - 1
                            continue
                        strang = 'http://www.youtube.com' + str(link)
                        await message.channel.send(strang)
                        return

        
            if message.content.startswith('!py'):
                if message.content.split(' ')[0] == '!py':
                    strang = 'ans = ' + message.content[4:]
                elif len(message.content.split(' ')[0]) == 5:
                    strang = 'ans = ' + message.content[5:]

                    # if str(message.author) != 'llynx#4386':
                    # return
                try:
                    loc = locals()
                    exec (strang, globals(), loc)
                    if len(message.content.split(' ')[0]) == 5:
                        if message.content.split(' ')[0][3] == 'b':
                            await message.channel.send(str(bin(loc['ans'])))
                            return
                    await message.channel.send(str(loc['ans']))
                except BaseException as emsg:
                    await message.channel.send(str(emsg))
                    return
                    
                    
                    

client = MyClient()
client.run('') #token

