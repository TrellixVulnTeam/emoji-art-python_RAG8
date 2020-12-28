#
# times = 1
#
# while times < 10:
#     print("😊" * times)
#     times += 1

###################################

# for num in range(1, 11):
#     print("😊" * num)


###################################
# Without string multiplication - ugly solution

for num in range(1, 11):
    count = 1
    smileys = ""

    while count < num:
        smileys += "😊"
        count += 1
    print(smileys)




