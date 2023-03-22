#Öğrenci kayıt sistemi yazıyoruz.

studentNameList=["Fatma Gökan", "Hatice Zeybek", "Büşra Anaçoğlu", "Merve Sena Kitiş"]
print(studentNameList)

print("----------")

#Listeye öğrenci ekliyoruz.
studentNameList.append("Şeyma Çakmak")
print(studentNameList)

print("----------")

#Listeden öğrenci çıkarıyoruz.
studentNameList.pop()
print(studentNameList)

print("...")

studentNameList.remove("Fatma Gökan")
print(studentNameList)

print("----------")

#Listeye birden fazla öğrenci ekliyoruz.
studentNameList.extend(["Fatma Gökan", "Şeyma Çakmak", "Bilge Çelen","Dorukhan Vatanlar"])
print(studentNameList)

print("----------")

#Listedeki tüm öğrencileri tek tek ekrana yazdırıyoruz.
for student in studentNameList:
    print(student)

print("----------")

#Listedeki öğrencilerin index numaralarını öğrenci numaraları olarak yazdırıyoruz.

for student in studentNameList:
    print(f"Öğrenci Numarası: {studentNameList.index(student)}, Öğrenci Adı-Soyadı:{student} ")

print("----------")

#Listeden birden fazla öğrenci siliyoruz.

def deleteStudents():
    number=int(input("Silmek istediğiniz öğrenci sayısını giriniz."))
    i=0
    while i<number:
        who=input("Silmek istediğiniz öğrencinin ad-soyad bilgisini giriniz.")
        studentNameList.remove(who)
        i+=1

deleteStudents()


print(studentNameList)