#!/usr/bin/python3
""" extract infor about the telgram group """

import json

filename = "chat.json"
keys = []

with open(filename, mode='r', encoding='utf-8') as f:
    data = json.load(f)

if isinstance(data, dict):
    for key in data:
        print(key)
print("len of data is {}".format(len(data)))
print(type(data["messages"]))

messages = data["messages"]

print(len(messages))
print(messages[1]['text_entities'])
