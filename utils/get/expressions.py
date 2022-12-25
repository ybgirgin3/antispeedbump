class Expressions:
    """
    edge_sidecar_to_children -> sliding images
    """

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

        media = self.data['edge_owner_to_timeline_media']['edges']
        info = media[0]['node']
        code = f"{info['id']}_{info['shortcode']}"
        is_video = info['is_video']

        dimensions = [
            info['dimensions']['height'],
            info['dimensions']['width']
        ]
        download_url = info['video_url']

        ret["media"] = {
            "code": code,
            "is_video": is_video,
            "dimensions": dimensions,
            "download_url": download_url
        }

        return ret

    def _test(self):
        return self.data
