#from django.db import models

# Create your models here.

class Serie():

    def __init__(self):
        self.episodes = []

    def add_ep(self, iframe):
        self.episodes.append(iframe)

    def get_ep(self, ep):
        return (self.episodes[ep])

    def get_li(self):
        return (self.episodes)

pascal = Serie()
pascal.add_ep('ep1')
pascal.add_ep('ep2')
pascal.add_ep('ep3')
pascal.add_ep('ep4')