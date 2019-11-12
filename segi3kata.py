def segitigaKata (letters):
    a = letters.replace(" ","")
    l = list (a)
    if len(l) == 10:
        n = 4
        def maju(n):   
            num = 0
            for i in range(0, n): 
                for j in range(0, i+1): 
                    print(l[num], end=" ")  
                    num = num + 1
                print("\r") 
        maju(n)
        def mundur(n):   
                num = 0
                for i in range(n, 0, -1): 
                    for j in range(1, i+1): 
                        print(l[num], end=" ")  
                        num = num + 1
                    print("\r") 
        mundur(n)
    elif len (l) == 36:
        n = 8
        def maju(n):   
            num = 0
            for i in range(0, n): 
                for j in range(0, i+1): 
                    print(l[num], end=" ")  
                    num = num + 1
                print("\r") 
        maju(n)
        def mundur(n):   
            num = 0
            for i in range(n, 0, -1): 
                for j in range(1, i+1): 
                    print(l[num], end=" ")  
                    num = num + 1
                print("\r") 
        mundur(n)
    else:
        print ("Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.")

# segitigaKata("purwadhika")
segitigaKata("Purwadhika Startup and Coding School @BSD")
# segitigaKata("kode python")
# segitigaKata("kode")
# segitigaKata("lintang")