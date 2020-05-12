def profile(name, age, bloodgroup="O+"):
    print('Name=', name)
    print('Age=', age)
    print('Blood Group=', bloodgroup)


# Positional Argument
profile("John", 31, "B+")
profile("Karen", 25)

# Keyword Argument
profile(age=43, bloodgroup="A+", name="Russ")
