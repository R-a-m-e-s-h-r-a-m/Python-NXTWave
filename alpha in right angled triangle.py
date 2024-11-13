n = int(input())
alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
for i in range(1,n+1):
    print("  "*(n-i) + alpha[:i*2])