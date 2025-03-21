#1) List-ის შექმნა და ელემენტების გამოტანა
# შექმენით სია, რომელიც შეიცავს 5 რიცხვს. შემდეგ გამოიტანეთ პირველი, ბოლო და შუათანაში მყოფი ელემენტები.

n = [1, 2, 3, 4, 5]
   # 0, 1, 2, 3, 4

print(n[0], n[2], n[4])


# 2) List-ის შეცვლა
# შეასწორეთ შეცდომები რასაც ხედავთ არასწორს ჩაასწორედ აუციელბლად  num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12]

num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12]
     # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

num[1] = 2
num[6] = 7
num[9] = 10
print(num)


# 3) Index-ით წვდომა
# შექმენით სია, რომელშიც არის ცხოველები, შემდეგ გამოიტანეთ ცხოველის ინდექსი (მაგალითად, "dog").

animals = ["horse", "cat", "snake", "tiger", "dog", "owl"]
         #    0,      1,      2,       3,      4,     5

print(animals[4])


# 4)მიწარმოეთ რამდენიმე სიტყვა  HELLOWEN იდან 

#owl
#well
#one
#low

a = "helloween"
print(a[4] + a[5] + a[2])
print(a[5] + a[1] + a[2] + a[3])
print(a[4] + a[8] + a[1])
print(a[2] + a[4] + a[5])



#4) შეაერთე სიტყვა რომ გამოვიდეს GOA IS THE BEST ACADEMY

# ["GOA" , "MAGARIA", "NOVATORI","IS","THE", "VIRGIN", "CHAD" ,"BEST" ,"ACADEMY"

GOA = ["GOA" , "MAGARIA", "NOVATORI","IS","THE", "VIRGIN", "CHAD" ,"BEST" ,"ACADEMY"]

print(GOA[0], GOA[3], GOA[4], GOA[7], GOA[8])





