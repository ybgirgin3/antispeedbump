class Expressions:
    def __init__(self, data: dict):
        self.data = data

    def parse(self):
        self.data = self.data['data']['user']
        ret = dict()

        # generic
        ret['id'] = self.data['id']
        ret['username'] = self.data['username']
        ret['full_name'] = self.data['full_name']
        ret["bio"] = self.data['biography']
        ret["is_private"] = self.data['is_private']
        ret['total_follower_count'] = self.data['edge_followed_by']['count']
        ret['mutual_follower_count'] = self.data['edge_mutual_followed_by']['count']
        ret['profile_picture'] = self.data['profile_pic_url_hd']
        #ret["post_count"] = self.data['edge_owner_to_timeline_media']

        return ret

    def _test(self):
        return self.data
