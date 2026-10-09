color=input("Enter the color you see : ")
match color :
    case "Green":
        print("Go")
    case "Red" :
        print("Stop")
    case _:
        print("Wrong Color")