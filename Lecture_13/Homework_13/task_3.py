def greeter_bot():
    name = yield "Enter your name"
    while True:
        name = yield f"Hello {name}!"

my_bot = greeter_bot()
print(next(my_bot))
print(my_bot.send("Irina"))
print(my_bot.send("Giorgi"))
        