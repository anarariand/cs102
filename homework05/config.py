domain = "https://api.vk.com/method"
access_token = '03c23b79310827a8024dd3ba4f0f8b78a9eda2118c9e8376df339b19e64438008ece7a34e7d3c2db8d653'
user_id = 367760592
fields = 'sex'
v = '5.103'

query = f"{domain}/friends.get?access_token={access_token}&user_id={user_id}&fields={fields}&v={v}"
response = requests.get(query)
