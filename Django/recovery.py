from django.contrib.auth import get_user_model

# list(get_user_model().objects.filter(
#     is_superuser=True).values_list("username", flat=True))


def reset_password(u, password):
    try:
        user = get_user_model().objects.get(username=u)
    except:
        return "User could no be found"
    user.set_password(password)
    user.save()
    return "Password has been changed succesfully"


resp = reset_password("admin", "passw0rd")
print(resp)
