

fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]


def change_name(user_id: int, new_name: str):
    # return [(user['name'] = new_name if user['id'] == user_id else True) for user in fake_users2]
    # current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))
    current_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))[0]
    current_user["name"] = new_name
    
    for user in fake_users2:
        if user['id'] != user_id:
            continue

        user['name'] = new_name
        
change_name(2, 'aaa')
a = 0
