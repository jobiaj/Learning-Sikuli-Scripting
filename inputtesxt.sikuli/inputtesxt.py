name = input("Enter your name?")
popup("hello"+name, "Hello!")
someText = inputText("Enter some text!")
popError("ah..!!"+someText)
myOptions = ('1','2','3','4','5')
result = select("Pick a number..!", options= myOptions)
choice = popAsk("Did you select "+ result+"..?")
