while(True):
    quarterValue = int(input("Which quarter do you want to look at"))
    match quarterValue:
        case 1:
            print("X>0 and till infinity; Y> 0 and till infinity")
        case 2:
            print ("X<0 and till -infinity; Y>0 and till infinity")
        case 3:
            print ("X<0 and till -infinity; Y<0 and till -infinity")
        case 4:
            print("X>0 and till infinity;Y<0 and till -infinity")
    decision = input("Do you want to stop? Enter yes if you want to break a loop").lower()
    if (decision == "yes"):
        break


