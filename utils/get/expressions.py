from typing import Optional
import random


class Expressions:
    """
    edge_sidecar_to_children -> sliding images
    """

    def __init__(self,
                 data: dict,
                 post_index: Optional[int] = None,
                 shortcode: Optional[str] = ""
                 ) -> None:
        self.data = data['data']['user']
        self.shortcode = shortcode
        self.medias = self.data['edge_owner_to_timeline_media']['edges']
        print("len of media: ", len(self.medias))
        if not post_index:
            print("!! if item couldn't be found random item will fetched")
            self.post_index = random.randint(0, len(self.medias))
        else:
            self.post_index = post_index

    def parse(self) -> dict:
        ret = dict()

        # generic
        ret['id'] = self.data['id']
        ret['username'] = self.data['username']
        ret['profile_picture'] = self.data['profile_pic_url_hd']
        # ret['full_name'] = self.data['full_name']
        # ret["bio"] = self.data['biography']
        # ret['total_follower_count'] = self.data['edge_followed_by']['count']
        # ret['mutual_follower_count'] = self.data['edge_mutual_followed_by']['count']

        ret["is_private"] = self.data['is_private']
        if self.data['is_private']:
            print("account is private, Data will be limited...")
            return ret

        if self.shortcode != "":
            for media in self.medias:
                if media['node']['shortcode'] == self.shortcode:
                    print("shortcode bulundu")
                    self.post_index = self.medias.index(media)
                    print("medias.index(media)", self.post_index)
        else:
            print("no shortcode defined")

        print("current post index: ", self.post_index)
        info = self.medias[self.post_index]['node']
        code = f"{info['id']}_{info['shortcode']}"
        is_video = info['is_video']

        dimensions = [
            info['dimensions']['height'],
            info['dimensions']['width']
        ]

        ret["media"] = {
            "code": code,
            "is_video": is_video,
            "suffix": "mp4" if is_video else "jpeg",
            "dimensions": dimensions,
            "download_url": info['video_url'] if is_video else info["display_url"]
        }

        return ret

    def _test(self):
        return self.data
