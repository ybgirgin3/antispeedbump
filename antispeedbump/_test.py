# from utils import Process, FileProcess
# from pprint import pprint
# import os
# from utils import Post
# from utils import Process, csrf_token, requester
# from requests import Response
# import json
# import requests
# from bs4 import BeautifulSoup
# import json
# import re

from commons import SQL_ALCHEMY_ENGINES, _create_table
from commons.models.schemas import Sites

_create_table("Sites", SQL_ALCHEMY_ENGINES["sites"])

# from utils.post._story import Story
# #
# st = Story()
# ret = st.login()
# # st.extract(ret)
# print(ret)

# payload = {
#     "username": "SessionDeneme",
#     "password": "'G7&z-E/*Gx4k^"
# }

# url = "https://www.instagram.com/accounts/login/"
# url = "https://www.instagram.com/api/v1/media/configure/"

# with open("sess.html", "r") as f:
#     html = f.read()
#
#
# territories = json.loads(
#     re.search(r"var raw = (\{.*\})", html)
# )
# print(territories)

# html = '<input type="hidden" name="csrfToken" value="ajax:SOME_TOKEN"/>'
# soup = BeautifulSoup(html)
# #
# token = soup.find()
# #
# print(token)

# ret = requests.post(url, data=payload)
# print(ret.text)

# with open("sess.json", "w") as f:
#     json.dump(ret.json(), f, indent=4)

# print(ret.cookies._cookies)
# print(ret.csrftoken)

# SessionDeneme
# 'G7&z-E/*Gx4k^

# import json
# with open('sess.json') as f:
#     sess_dict = json.load(f)
# print(sess_dict.cookies)


# response: Response = Process(username=username).fetch()
# headers = {
#       "accept": "*/*",
#       "accept-language": "en-US,en;q=0.9",
#       "content-type": "application/x-www-form-urlencoded",
#       "sec-ch-prefers-color-scheme": "dark",
#       "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
#       "sec-ch-ua-mobile": "?0",
#       "sec-ch-ua-platform": "\"macOS\"",
#       "sec-fetch-dest": "empty",
#       "sec-fetch-mode": "cors",
#       "sec-fetch-site": "same-origin",
#       "viewport-width": "825",
#       "x-asbd-id": "198387",
#       "x-csrftoken": "5qF75sHk0uZsiMWPkkjPhQePzFULUWMU",
#       "x-ig-app-id": "936619743392459",
#       "x-ig-www-claim": "hmac.AR2Eeqxxor3oCtcOHw-GgdN7pOQ-CWWplPB6LyBmU-xOowtJ",
#       "x-instagram-ajax": "1006793331",
#       "x-requested-with": "XMLHttpRequest",
#       "cookie": "mid=Y5ZI2QAEAAH4SC_6fRNydmN_pF1l; ig_nrcb=1; ig_did=7C4B0CE8-6630-416C-892E-5C1760B0B32D; datr=2EiWY2REn8xtJBQOwMOZT2pD; csrftoken=5qF75sHk0uZsiMWPkkjPhQePzFULUWMU; ds_user_id=56834290108; shbid=\"11937\\05456834290108\\0541704324103:01f788bbc103982e07cead490ac910b9249c55060876125b1ee15ec8bd8e893b4b254cff\"; shbts=\"1672788103\\05456834290108\\0541704324103:01f7f1f4835e0e77f484566a0659bce807739ea95848e7dc4539e46bb1712e00244e8fe9\"; dpr=1; sessionid=56834290108%3AmsvmGSOIUgEg4A%3A9%3AAYc4Ndq3W9vrs9jfl72nKmOE1hXfpKuPRVbNzDehEho; rur=\"ASH\\05456834290108\\0541704555981:01f7f68f10914ecfe3dd97d7b9d84c64177a841f05cb2cba335eb268ce81acede79748b4\"",
#       "Referer": "https://www.instagram.com/",
#       "Referrer-Policy": "strict-origin-when-cross-origin"
#     },
# "source_type=library&caption=nice+car&upload_id=1673020000614&disable_comments=0&like_and_view_counts_disabled=0&igtv_share_preview_to_feed=1&is_unified_video=1&video_subtitles_enabled=0&disable_oa_reuse=false",
# body = {
#
# }
# response: Response = requester()

# print(response)

# token = csrf_token(response)
# print("token: ", token)


# p = Post()
# print("post: ", p)


# env = True if 'DEBUG' in os.environ else False
# print(env)


# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# print(ROOT_DIR)

# username = 'bellathorne'
# content = FileProcess(filename=username).read()
# ret = Process.Parse(content=content).find_val()
# pprint(ret)


# from bs4 import BeautifulSoup
#
# html = 'login.html'
# with open(html, "r") as html:
#
#     soup = BeautifulSoup(html, "html.parser")
#     scripts = soup.find_all("script")
#     print(scripts)

# from commons import session
# from commons.models.schemas import Sites
# from utils import is_site_still_valid
#
# with session() as sess:
#     is_site_still_valid(sess, Sites, 'asd')
