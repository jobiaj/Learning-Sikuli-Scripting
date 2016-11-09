modes = ("Add", "Sub", "Mul", "Div")
option = select("which operation you like to do????", options=modes)
click("1478601478992.png")
wait("1478601550253.png")
type("calc"+ Key.ENTER)
wait("1478602292947.png")
click(Pattern("1478602292947.png").targetOffset(-33,-17))
if option == modes[0]:
    click(Pattern("1478602292947.png").targetOffset(42,51))
elif option == modes[1]:
    click(Pattern("1478602292947.png").targetOffset(43,12))
elif option == modes[2]:
     click(Pattern("1478602292947.png").targetOffset(37,-21))
else:
     click(Pattern("1478602292947.png").targetOffset(34,-54))
click(Pattern("1478602292947.png").targetOffset(-43,16))
click(Pattern("1478602292947.png").targetOffset(80,27))

    

    