# can you make it so the join depends on if the position is > 2 then the sepeartor is , but if position is -1 of len(items) its " and "
def oxford_comma(items):
    if len(items) <= 0:
        print(items)
        return ""
    
    if len(items) == 1:
        print(items[0])
        return items[0]
    
    if len(items) == 2:
        print(" and ".join(items))
        return " and ".join(items)  

    last_item = items[-1]
    # print(last_item)
    newString = ", ".join(items[:-1]) + f", and {last_item}"
    
    print(newString)
    return newString















    newItems = list
    # itterat thru to append new list with item += , || and || , and
    for item in items:
        # if items len(items) == 1 append newItems
        if len(items) == 1:
            newItems.append(items[0])
            # if items len(items) == 2 item += " and " && append newItems
        if len(items) == 2:
            newItems.append( " and ".join(items))
            # if items len(items) > 2 item += ", "
        if len(items) > 2:
            newItems.append(", and ".join(items))



    #.join them together
    newString = "".join(newItems)
    print(newString)
    return newString

oxford_comma(["fiddleheads"]) 
oxford_comma(["fiddleheads", "okra"]) 

oxford_comma(["fiddleheads", "okra", "kohlrabi"])   
# => "fiddleheads, okra, and kohlrabi"
oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"])   
# => "fiddleheads, okra, and kohlrabi"