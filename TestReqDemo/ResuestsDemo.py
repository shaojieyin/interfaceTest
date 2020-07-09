# -*- coding: UTF-8 -*-
import json

import requests

req = requests.get("https://api.xdclass.net/pub/api/v1/web/all_category").json()
print(json.dumps(req, ensure_ascii=False, indent=2)) # 排序并且缩进两个字符输出