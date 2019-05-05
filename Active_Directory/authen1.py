from __future__ import unicode_literals, print_function

from getpass import getpass
from json import dumps

from easyad import EasyAD

# Workaround to make input() return a string in Python 2 like it does in Python 3
# It's 2016...you should really be using Python 3
try:
    input = input
except NameError:
        pass

# Set up configuration. You could also use a Flask app.config
config = dict(AD_SERVER="192.168.8.134",
              AD_DOMAIN="itsupport")

# Initialize all the things!
ad = EasyAD(config)

# Authenticate a user
username = input("Username: ")
password = getpass("Password: ")

local_admin_group_name = "itsupport.local/Network"

user = ad.authenticate_user(username, password, json_safe=True)

if user:
    # Successful login! Let's print your details as JSON
    print(dumps(user, sort_keys=True, indent=2, ensure_ascii=False))

    # Lets find out if you are a member of the "LocalAdministrators" group
    print(ad.user_is_member_of_group(user, local_admin_group_name))
else:
    print("Those credentials are invalid. Please try again.")
    exit(-1)

# You can also add service account credentials to the config to do lookups without
# passing in the credentials on every call
ad.config["AD_BIND_USERNAME"] = "Administrator"
ad.config["AD_BIND_PASSWORD"] = "P@ssw0rd"

user = ad.get_user("maurice.moss", json_safe=True)
print(dumps(user, sort_keys=True, indent=2, ensure_ascii=False))

group = ad.get_group("helpdesk", json_safe=True)
print(dumps(user, sort_keys=True, indent=2, ensure_ascii=False))

print("Is Jen a manager?")
print(ad.user_is_member_of_group("jen.barber", "Managers"))

# The calls below can be taxing on an AD server, especially when used frequently.
# If you just need to check if a user is a member of a group use
# EasyAD.user_is_member_of_group(). It is *much* faster.

# I wonder who all is in the "LocalAdministrators" group? Let's run a
# query that will search in nested groups.
print(dumps(ad.get_all_users_in_group(local_admin_group_name, json_safe=True)))

# Let's see all of the groups that Moss in in, including nested groups
print(dumps(ad.get_all_user_groups(user), indent=2, ensure_ascii=False))