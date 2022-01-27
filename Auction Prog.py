print('''Art''')


bidders={}
bidding_finished = False

while not bidding_finished:
    name_bidder = input("Enter Your name: ")
    bidding_price = int(input("Enter Your price: $"))
    print("Thank you for bidding,", name_bidder, "You just bidded", bidding_price)
    bidders[name_bidder] = bidding_price
    ans = (input("Are there any other bidders? Enter Yes or No: ")).lower()
    if ans == "no":
        bidding_finished = True
    elif ans == "yes":
        clear()


# def bidding_details(name_bidder, bidding_price):
#     print("Thank you for bidding,", name_bidder, "You just bidded",bidding_price)
# bidding_details(name_bidder=input("Enter Your name: "),bidding_price=int(input("Enter Your price: $")))
#
# bidders=[]
#
# bidders.append(bidding_details({"name": name_bidder,"price": bidding_price}))
# # if name_bidder:
# #     ans = (input("Enter Yes or No: ")).lower()
# #     if ans == "yes":
# #         bidding_details.clear()
# #     elif ans == "no":
# #         for value in bidding_price:
# #             max_key = max(bidders, name =name_bidder.get)