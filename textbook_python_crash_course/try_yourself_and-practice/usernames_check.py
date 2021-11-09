current_users = ['tansey', 'haslam', 'Dow', 'hamiltom', 'taYlor', 'brown']
current_users_lower = [current_user.lower() for current_user in current_users]
new_users = ['taylor', 'dow', 'mackey', 'kashani', 'darvel']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Please a new username.")

    else:
        print("This username is avaiabel.")
