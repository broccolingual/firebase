from firebase import Firebase

firebase = Firebase()

# データの格納(ID自動生成)
key_value_data = {
            'date_of_birth': 'June 23, 1984',
            'full_name': 'Sazae Isono'
        }
firebase.push(key_value_data, "data/test")

# データの格納(非推奨/updateで代替してください)
data = {
        'user001': {
            'date_of_birth': 'June 23, 1984',
            'full_name': 'Sazae Isono'
            },
        'user002': {
            'date_of_birth': 'December 9, 1995',
            'full_name': 'Tama Isono'
            }
        }

firebase.set(data, "data/test")

# データのアップデート
updates = {'/user001/full_name': 'Sazae Fuguta'}
firebase.update(updates, "data/test")

# データの取得
data = firebase.get("data/test/user003")
print(data)

# # データの削除
# firebase.delete()