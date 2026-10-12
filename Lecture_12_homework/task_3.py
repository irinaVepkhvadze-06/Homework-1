def require_role(allowed_role = "admin"):
    def decorator(func):
        def wrapper(user_role):
            if user_role == allowed_role:
                return func (user_role)
            else:
                print("Permission Denied: User is not an admin.")

        return wrapper
    return decorator

@require_role(allowed_role = "admin")
def delete_data(user_role = "admin"):
    print("Everything is fine")

delete_data("admin")
delete_data("guest")


