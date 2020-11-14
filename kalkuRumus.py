#func untuk rumus keliling bangun ruang
def keliling_lingkaran():
    r = float(input("Masukkan jari - jari lingkaran = "))
    kl = 2 * 3.14 * r
    kl2 = 2 * 22/7 * r
    print ("Keliling lingkaran adalah = ",'2','*','3.14','*',r,'=',kl)
    print ("Keliling lingkaran adalah = ",'2','*','22/7','*',r,'=',kl2)
    

def keliling_persegi():
    s = float(input("Masukkan sisi persegi = "))
    kp = 4 * s
    print ("Keliling persegi adalah = ",'4','*',s,'=',kp)
    

def keliling_persegi_panjang():
    p = float(input("Masukkan panjangnya = "))
    l = float(input("Masukkan lebarnya = "))
    kpp = 2 * (p + l)
    print ("Keliling persegi panjang adalah = ",'2','*','(',p, '+' ,l,')','=',kpp)

    
def keliling_segitiga():
    a = float(input("Masukkan Panjang sisi segitiga a  = "))
    b = float(input("Masukkan Panjang sisi segitiga b  = "))
    c = float(input("Masukkan Panjang sisi segitiga c  = "))
    ks = a + b + c
    print("Keliling segitiga adalah =", a ,'+', b ,'+', c ,'= ',ks)
    

#func untuk rumus luas bangun ruang
def luas_lingkaran():
    r = float(input("Masukkan jari - jari lingkaran = "))
    hasil = 3.14 * (r ** 2)
    hasil2 = 22/7 * (r ** 2)
    print ("Luas lingkaran adalah = ",'3.14' , '*' , '(' , r , '*' ,  r , ')' , '= ' ,hasil)
    print ("Luas lingkaran adalah = ", '22/7' , '*' , '(' , r , '*' , r , ')' , '= ' ,hasil2)

def luas_persegi():
    s = float(input("Masukkan sisi persegi = "))
    hasil = s ** 2
    print ("Luas persegi adalah = ",s,'*',s,'= ', hasil)

def luas_persegi_panjang():
    p = float(input("Masukkan panjangnya = "))
    l = float(input("Masukkan lebarnya = "))
    hasil = p * l
    print ("Luas persegi panjang adalah = ",p,'*',l,'= ',hasil)

def luas_segitiga():
    a = float(input("Masukkan alas segitiga = "))
    t = float(input("Masukkan tinggi segitiga = "))
    hasil = 1/2 * (a * t)
    print ("Luas segitiga adalah = ", '1/2' ,'*','(',a,'*',t,')','= ',hasil)


# Kumpulan rumus luas
def rumus_luas():
    print ("\n===KALKULATOR RUMUS LUAS===")
    print ("\nMasukkan angka sesuai yang ingin dihitung")
    user2 = int(input ("1. Luas lingkaran\n2. Luas persegi\n3. Luas persegi panjang\n4. Luas segitiga\n= "))

    if user2 == 1:
        luas_lingkaran()

    elif user2 == 2:
        luas_persegi()

    elif user2 == 3:
        luas_persegi_panjang()

    elif user2 == 4:
        luas_segitiga()

    else:
        print("\nMaaf, pilihan yang anda masukkan tidak terdaftar")


# Kumpulan rumus keliling
def rumus_keliling():
    print ("\n===KALKULATOR RUMUS KELILING===")
    print ("\nMasukkan angka sesuai yang ingin dihitung")
    user1 = int(input ("1. keliling lingkaran\n2. keliling persegi\n3. keliling persegi panjang\n4. keliling segitiga\n= "))

    if user1 == 1:
        keliling_lingkaran()

    elif user1 == 2:
        keliling_persegi()

    elif user1 == 3:
        keliling_persegi_panjang()

    elif user1 == 4:
        keliling_segitiga()

    else:
        print("\nMaaf, pilihan yang anda masukkan tidak terdaftar")

print("\n==KALKULATOR APAKAH YANG INGIN ANDA AKSES?==\n " )
calcuChoice = int(input("1. Kalkulator rumus keliling bangun datar\n2. Kalkulator rumus luas bangun datar\n= "))

if calcuChoice == 1:
    rumus_keliling()

elif calcuChoice == 2:
    rumus_luas()

else:
    print("\nMaaf, pilihan yang anda masukkan tidak terdaftar")