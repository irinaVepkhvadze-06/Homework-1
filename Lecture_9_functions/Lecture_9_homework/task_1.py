def create_user_profile(first_name, last_name, role = "student", is_active = True):
    return {
        "first_name": first_name,
        "last_name": last_name,
        "role": role,
        "is_active": is_active
}
print(create_user_profile("Irina", "Vepkhvadze"))

print(create_user_profile("Ana", "Smith"))



