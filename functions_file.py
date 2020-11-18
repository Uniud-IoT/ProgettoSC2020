import os
import json
import pprint

def serialize_json(folder, filename, data):
  if not os.path.exists(folder):
    os.makedirs(folder, exist_ok=True)
  with open(f"{folder}/{filename}", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
  print(f"Data serialized to path: {folder}/{filename}")

def read_json(path):
  if os.path.exists(path):
    with open(path, "r", encoding="utf8") as file:
      data = json.load(file)
    print(f"Data read fron path: {path}")
    return data
  else:
    print(f"No data found at path: {path}")
    return {}

def usersID (users):
    usersID = []
    for user in users:
        json_data = api.get_user(user)._json
        usersID.append(json_data["id"])
    return usersID

def download_followers(idUser, quantity):
  followers_of_user = []
  for follower in tweepy.Cursor(
        api.followers,
        id = user,
        skip_status=True,
        include_user_entities = False
    ).items(quantity):
        #json_data = follower._json
        followers_of_user.append(follower._json["id"])
  return followers_of_user

def download_following(user, quantity):
  friends_of_user = []
  for friend in tweepy.Cursor(
        api.friends,
        id = user,
        skip_status=True,
        include_user_entities = False
    ).items(quantity):
        json_data = friend._json
        friends_of_user.append(friend._json["id"])
  return friends_of_user