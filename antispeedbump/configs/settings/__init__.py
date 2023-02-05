get = {
  "accept": "*/*",
  "accept-language": "en-US,en;q=0.9",
  "sec-ch-prefers-color-scheme": "dark",
  "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"macOS\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "viewport-width": "905",
  "x-asbd-id": "198387",
  "x-csrftoken": "LwTuL9KezONhvsYkcL9tfBjxHcyREUky",
  "x-ig-app-id": "936619743392459",
  "x-ig-www-claim": "hmac.AR2Eeqxxor3oCtcOHw-GgdN7pOQ-CWWplPB6LyBmU-xOowtJ",
  "x-requested-with": "XMLHttpRequest",
  "cookie": "mid=Y5ZI2QAEAAH4SC_6fRNydmN_pF1l; ig_nrcb=1; ig_did=7C4B0CE8-6630-416C-892E-5C1760B0B32D; datr=2EiWY2REn8xtJBQOwMOZT2pD; csrftoken=LwTuL9KezONhvsYkcL9tfBjxHcyREUky; ds_user_id=57603119263; dpr=1; sessionid=57603119263%3AcqzfKSpyK99PC1%3A10%3AAYcj_ruRQHJCBZhCX7c16gDcw-OzKjQ6PIqw_vkfvw; rur=\"NAO\\05457603119263\\0541706213987:01f78a6e5b52104000268aeaa64dcabc2b596eb3a89a8b3bf67bf480c8d30b078b48bc49\"",
  "Referrer-Policy": "strict-origin-when-cross-origin"
}

post = {
  "authority": "www.instagram.com",
  "x-ig-www-claim": "hmac.AR2-43UfYbG2ZZLxh-BQ8N0rqGa-hESkcmxat2RqMAXejXE3",
  "x-instagram-ajax": "adb961e446b7-hot",
  "content-type": "application/x-www-form-urlencoded",
  "accept": "*/*",
  "x-requested-with": "XMLHttpRequest",
  "x-ig-app-id": "1217981644879628",
  "origin": "https://www.instagram.com",
  "sec-fetch-site": "same-origin",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "accept-language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7"
}

story = {
  "accept": "*/*",
  "accept-language": "en-US,en;q=0.9",
  "content-type": "application/x-www-form-urlencoded",
  "sec-ch-prefers-color-scheme": "dark",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "x-asbd-id": "198387",
  "x-csrftoken": "LwTuL9KezONhvsYkcL9tfBjxHcyREUky",
  "x-ig-app-id": "1217981644879628",
  "x-ig-www-claim": "hmac.AR33ezMVQ-1_Z8FtSq556EcKHzDQWBIlAsJZ-F1PkXRZI_5t",
  "x-instagram-ajax": "1006908522",
  "x-requested-with": "XMLHttpRequest"
}

upload_id = {
  "content-type": "image / jpg",
  "content-length": "1",
  "Offset": "0",
  "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
  "x-entity-length": "1",
  "x-ig-app-id": "1217981644879628"
}

def setting(fn):
    getter = {
        'get': get,
    }

    return getter[fn]
