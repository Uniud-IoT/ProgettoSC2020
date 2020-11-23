import os
import json
import tweepy
import random
import numpy as np


class Functions:

    def usersID(users, api):
        usersID = []
        for user in users:
            json_data = api.get_user(user)._json
            usersID.append(json_data["id"])
        return usersID

    def userID(user, api):
        json_data = api.get_user(user)._json
        return json_data["id"]

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

    def download_followers(idUser, quantity, api):
        followers_of_user = []
        for follower in tweepy.Cursor(
                api.followers,
                id=idUser,
                skip_status=True,
                include_user_entities=False
        ).items(quantity):
            followers_of_user.append(follower._json["id"])
        return followers_of_user

    def download_following(idUser, quantity, api):
        friends_of_user = []
        for friend in tweepy.Cursor(
                api.friends,
                id=idUser,
                skip_status=True,
                include_user_entities=False
        ).items(quantity):
            friends_of_user.append(friend._json["id"])
        return friends_of_user

    def random_json_with_control(json_array, quantity, all):
        a = quantity
        array = []
        while (a != 0):
            item = random.choice(json_array)
            if item not in array and item not in all:
                array.append(item)
                a = a - 1
        return array

    def downlodUserDetails(userId, api):
        json_data = api.get_user(userId)._json
        foundInfo = {
            'id': json_data['id'],
            'name': json_data['name'],
            'screen_name': json_data['screen_name'],
            'location': json_data['location'],
            'followers_count': json_data['followers_count'],
            'friends_count': json_data['friends_count']
        }
        return foundInfo

    def friendship(sourceid, targetid, api):
        friendship = api.show_friendship(source_id=sourceid, target_id=targetid)
        if friendship[0].following & friendship[0].followed_by:
            return "both"
        else:
            if friendship[0].following:
                return "sourceToTarget"
            if friendship[0].following:
                return "TargetToSource"
        return None

    def searchInDict(source, target, dictionary):
        for (k, v) in dictionary.items():
            if (source == v['target'] and target == v['source']):
                return True
        return False

    def is_following(sourceid, targetid, api):
        friendship = api.show_friendship(source_screen_name=sourceid, target_screen_name=targetid)
        if friendship[0].following:
            return True
        return False

    def converterNumber(allCent, n_nodes):
        allCent1 = np.empty((0, n_nodes), int)  #
        res = []  # TROVARE FUNZIONA PER CAPIRE IL NUMERO DI NODI E INSERIRE AL POSTO DI 6
        for cent in allCent:
            res.clear()
            for (k, v) in cent.items():
                res.append(v)
            allCent1 = np.append(allCent1, np.array([res]), axis=0)
        return allCent1

    def json_items_to_dict(file_names):
        allItems = {}
        for file in file_names:
            allItems.update(Functions.read_json(file))
        return allItems


    def deleteDuplicates(allItems):
        vector = []
        for (k, v) in allItems.items():
            for item in v:
                if item not in vector:
                    vector.append(item)
        return vector