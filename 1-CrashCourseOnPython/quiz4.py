def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            groups = []
            if (user in user_groups):
                groups = user_groups.get(user)
            groups.append(group)
            user_groups[user] = groups
    return (user_groups)

print( groups_per_user({"local": ["admin", "userA"],"public": ["admin", "userB"],"administrator": ["admin"]}) )
