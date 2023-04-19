from utils.page_utils import PageUtils
from settings import *


class Trails(PageUtils):
    if platform == 'ios':
        search = ('id', 'IOS_Locator')
    else:
        search = ('id', 'Android_Locator')

    def search_for_trail(self, trial_name):
        self.send_keys(self.search, trial_name)
