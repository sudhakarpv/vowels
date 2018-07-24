# vowels
def main():
    pass
    n=input().lower()
    l=list(n)
    temp=int(0)
    for i in l:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            temp+=1
    if(temp>0):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()
