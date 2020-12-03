from firebase import Firebase

firebase = Firebase()

# - データの格納 -
# 第一引数は辞書型のみ（str不可）
# key_value_data = {
#             'date_of_birth': 'June 23, 1984',
#             'full_name': 'Sazae Isono'
#         }
# firebase.push(key_value_data, "data/message/profile")

# - データのアップデート -
# 第一引数は辞書型のみ（str不可）
# updates = {"test": "this is test !"}
# firebase.update(updates, "data/message")

# - データの取得 -
# data = firebase.get("data/message")
# print(data)

# - データの削除 -
# firebase.delete("profile", "data/message")