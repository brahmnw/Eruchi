import discord
from discord.ext import commands
import json
import os

class LinksFull(Exception):
    pass

class ProfileHandler:

    def __init__(self, user_id, discord_profile: discord.Member, directory=None):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(discord_profile)
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

        if discord_profile is not None:
            discord_avatar = str(discord_profile.avatar_url)

        else:
            discord_avatar = 'https://a.ppy.sh'
        
        self.user = str(user_id)
        self.default_data = {
            'profile': {
                'bio': 'No bio provided.',
                'avatar': discord_avatar,
                'links': []
            }
        }

        if directory is not None:
            self.directory = directory

        else:
            self.directory = f'data/user/{user_id}.json'
        
        if os.path.exists(self.directory):
            f = open(self.directory, mode='r')
            self.user_data = json.load(f)
            print('Path Exists')

        else:

            f = open(self.directory, mode='w')
            json.dump(self.default_data, f)
            f = open(self.directory, mode='r')
            self.user_data = json.load(f)
            print('Created path with new defaults')

    def apply(self):
        f = open(self.directory, mode='w')
        json.dump(self.user_data, f)

    def add_link(self, title, link):

        if len(self.user_data['profile']['links']) >= 4:
            raise LinksFull("There is a maximum of 4 links per profile!")

        else:
            link = (title, link)
            self.user_data['profile']['links'].append(link)

        self.apply()

    def edit(self, attribute, value):

        if value == 'reset':
            self.user_data['profile'][attribute]

        self.user_data['profile'][attribute] = value
        self.apply()

    def get(self):
        return self.user_data

