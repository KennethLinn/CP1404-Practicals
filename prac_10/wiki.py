import wikipedia

title_input = input("Please enter a page title: ")
while title_input != "":
    title_input = wikipedia.page(title_input, auto_suggest=False)
    print("{}".format(title_input.title))
    print("{}".format(title_input.summary))
    print("{}".format(title_input.url))
    try:
        monty = wikipedia.summary("Monty")
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    title_input = input("Please enter a page title: ")