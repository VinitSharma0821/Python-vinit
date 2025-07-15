[4:25 pm, 11/7/2025] Vinit_0821:     i+=1
[4:25 pm, 11/7/2025] Vinit_0821: # for i in range(1,5):
#     for j in range(10,16):
#         print("*", end=" ")
#     print("")

# for i in range(1, 5):
#     for j in range(10, 16):
#         print(j, end=" ")
#     print("")

n = int(input("Enter the number of rows you want: "))
                                                                     
for i in range(1,n+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print("") 