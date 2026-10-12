def user_profile(first_name:str, last_name: str, role: str = "student", is_active: bool = True) ->dict:
    user_info = {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
    }
    return user_info
