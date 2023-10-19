import safi

while True:
    text = input("safi > ")
    result, error = safi.run("<stdin>", text)

    if error:
        print(error.as_string())
    else:
        print(result)
