class Expressions:
    """
    edge_sidecar_to_children -> sliding images
    """

    def __init__(
        self,
        data: dict,
    ) -> None:
        self.data: dict = data["data"]["user"]
        self.medias: list = self.data["edge_owner_to_timeline_media"]["edges"]

    def parse(self) -> dict:
        ret = dict()

        # generic
        ret["id"] = self.data["id"]
        ret["username"] = self.data["username"]
        ret["profile_picture"] = self.data["profile_pic_url_hd"]
        ret["full_name"] = self.data["full_name"]
        ret["bio"] = self.data["biography"]
        ret["is_private"] = self.data["is_private"]

        if self.data["is_private"]:
            # if account is private return immediately
            print(
                "Account is private, Data will be limited... And no media will be included"
            )
            return ret

        _medias = []

        for media in self.medias:
            _ret = {}
            node = media["node"]
            is_video = node["is_video"]
            download_url = node["video_url"] if is_video else node["display_url"]
            #orginal_desc = node['edge_media_to_caption']['edges']['text']

            _ret["is_video"] = is_video
            _ret["download_url"] = download_url

            _medias.append(_ret)

        ret["medias"] = _medias
        return ret

    def _test(self):
        return self.data
