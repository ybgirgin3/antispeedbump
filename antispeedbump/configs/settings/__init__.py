get = {
  "accept": "*/*",
  "accept-language": "en-US,en;q=0.9",
  "sec-ch-prefers-color-scheme": "dark",
  "sec-ch-ua": "\"Google Chrome\";v=\"111\", \"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"111\"",
  "sec-ch-ua-mobile": "?0",
  "sec-ch-ua-platform": "\"macOS\"",
  "sec-fetch-dest": "empty",
  "sec-fetch-mode": "cors",
  "sec-fetch-site": "same-origin",
  "viewport-width": "862",
  "x-asbd-id": "198387",
  "x-csrftoken": "W61Oof2Zad8a9FoiP0AQAafe9eU3N21x",
  "x-ig-app-id": "936619743392459",
  "x-ig-www-claim": "hmac.AR2zUYz0rYW6os9Rtzk01H_vJ3RvvmQLCySJx558ZLe5aKtV",
  "x-requested-with": "XMLHttpRequest",
  "cookie": "mid=Y5ZI2QAEAAH4SC_6fRNydmN_pF1l; ig_nrcb=1; ig_did=7C4B0CE8-6630-416C-892E-5C1760B0B32D; datr=2EiWY2REn8xtJBQOwMOZT2pD; csrftoken=W61Oof2Zad8a9FoiP0AQAafe9eU3N21x; ds_user_id=57057025143; dpr=2; shbid=\"12821\\05457057025143\\0541710711862:01f7584bb8eea7ac36741cb398959bce85e0653541376a4d1e15723dba06c8bf709cdb7b\"; shbts=\"1679175862\\05457057025143\\0541710711862:01f7322307687b619af788a04b40a5eb846b4088625512b3f35da7d9bc0fd807879d87cd\"; sessionid=57057025143%3AOx2wph8dKrAXT3%3A20%3AAYed_FlMPG9deV-udi0Fqz2E2XMUHxkTXNJQUbnMNg; rur=\"ASH\\05457057025143\\0541710712167:01f7c230950d4d40a3dccdf8c9bdd1625451a56725a1272114b05e98bd2a61d55374764b\"",
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
  "x-ig-app-id": "1217981644879628"}


def setting(fn):
  getter = {
    'get': get,
  }

  return getter[fn]
