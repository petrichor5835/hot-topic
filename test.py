import requests

cookies = {
    'buvid3': '063F266D-E0D0-B7E2-0E02-B6D8A7E0F73314159infoc',
    'b_nut': '1730872714',
    '_uuid': '73A81BE2-A7210-A44E-ECD9-101033B5F510410A13571infoc',
    'buvid4': '2A94E12A-9CE0-F0D0-C5BE-04A04894869A14613-024110605-5zc1zmqTP0qomH%2FPI6A%2BMQ%3D%3D',
    'enable_web_push': 'DISABLE',
    'DedeUserID': '400724706',
    'DedeUserID__ckMd5': 'c18d7943068bd647',
    'header_theme_version': 'CLOSE',
    'rpdid': "|(m~YkJu|mR0J'u~J|)~JRuJ",
    'LIVE_BUVID': 'AUTO9017308905425221',
    'CURRENT_QUALITY': '80',
    'hit-dyn-v2': '1',
    'fingerprint': '68060d0e0d6dd2e2d82d8da47b1db457',
    'buvid_fp_plain': 'undefined',
    'home_feed_column': '5',
    'buvid_fp': '68060d0e0d6dd2e2d82d8da47b1db457',
    'bili_ticket': 'eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzYxNjA2MTMsImlhdCI6MTczNTkwMTM1MywicGx0IjotMX0.dmdAj9JmHKaPJ3AGquK99p9CWPNQSYXxGKF5-5YoSvY',
    'bili_ticket_expires': '1736160553',
    'browser_resolution': '1897-879',
    'SESSDATA': '2c0576ea%2C1751627000%2C0074f%2A11CjAlDL_OXWMezWAxZmvqFpcLC1KN9C8yHq9Sbeh4LMx7oVWjUgIGUXOItwSE13mRc1sSVkpWR0FrZVJPUTJrM0lJeTZoWjhwUjAxR2g0TnhfQ0MxTGNJekVEX0QwZks3YUxCbk5KOGZscC1FN0l6Mkp4SlZDcDZyQXkyZW1nTk5BSW9zTFFTSkZBIIEC',
    'bili_jct': 'a6e2eeb01c9c7b14d0e0bb6f42f88bee',
    'PVID': '2',
    'b_lsid': 'CC310E4F8_19439B22CBF',
    'sid': '4l5gjn5c',
    'CURRENT_FNVAL': '4048',
    'bp_t_offset_400724706': '1019202800267034624',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.bilibili.com/v/popular/rank/all/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    'rid': '0',
    'type': 'all',
    'web_location': '333.934',
    'w_rid': '3711c872d6b9f8d6b66d739acbf3e723',
    'wts': '1736140051',
}

response = requests.get('https://api.bilibili.com/x/web-interface/ranking/v2', params=params, headers=headers)
print(response.json())
