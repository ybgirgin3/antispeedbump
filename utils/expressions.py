from .fp import FileProcess
#CONTENT_PATHS = FileProcess("content_paths", root="configs").read()

class Expressions:
    def __init__(self, data: dict):
        self.data = data

    def parse(self):
        self.data = self.data['data']['user']
        ret = dict()
        ret['id'] = self.data['id']
        ret['username'] = self.data['username']
        ret['total_follower_count'] = self.data['edge_followed_by']['count']
        ret['mutual_follower_count'] = self.data['edge_mutual_followed_by']['count']
        ret['profile_picture'] = self.data['profile_pic_url_hd']

        return ret

    def _test(self):
        return self.data


