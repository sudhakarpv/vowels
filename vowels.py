# vowels
def main():
    pass
    n=input().lower()
    temp=int(0)
    for i in n:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            temp+=1
    if(temp>1):
        print("yes")
    else:
        print("no")

if __name__ == '__main__':
    main()
