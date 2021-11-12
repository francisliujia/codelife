from admin import Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("adding privileges")
eric_privileges = [
    'can add post',
    'can delete post',
    'can ban users',
]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()