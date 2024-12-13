import math

# Koordinat sayılarını int türünde kullanıcıdan almak için önce değişken oluşturuyorum.
x1 =int(input("x1 koordinatını giriniz: "))
x2 =int(input("x2 koordinatını giriniz: "))
y1 =int(input("y1 koordinatını giriniz: "))
y2 =int(input("y2 koordinatını giriniz: "))

"""SORU-1
‘points’ adında bir liste oluşturun. Bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir. 
Örneğin, ‘(x, y)’ noktası bir demet ‘(x, y)’ olarak temsil edilecektir."""


# Listenin adını oluşturdum. Üçgenin 3 noktasını tupple olarak bu listeye yazdım.
points = [(x1, y1), (x2, y1), (x2, y2)]  



"""SORU-2
euclideanDistance’ adında bir fonksiyon tanımlayın. 
Bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı ve bu iki nokta arasındaki Öklid mesafesini döndürmelidir."""


# Önce bir fonksiyon tanımlıyorum.
def euclideanDistance(point1, point2):
    # Bu parametlere değerlerini yazıyorum.
  
    
    # Resimdeki formülü math metoduyla oluşturuyorum.
    return  math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    
    





"""SORU-3
Bir döngü kullanarak, ‘points’ listesindeki her nokta çifti arasındaki Öklid mesafesini hesaplayın. 
Bu mesafeleri ‘distances’ adında başka bir listede saklayın."""

#Önce boş bir liste oluşturdum.
distance=[]

for i in range(len(points)):
    for k in range(i + 1, len(points)):  # yukarıda döngüye girmiş elemanı ikinci sefer sokmamak için bir döngü daha oluşturdum.
        point1 =points[i]
        point2 =points[k]
        
        
        # Öklid mesafesini hesaplıyoruz.
        dis = euclideanDistance(point1, point2)
        
        # Mesafeyi 'distances' listesine ekliyorum.
        distance.append(dis)
        print(distance)

"""SORU-4
‘distances’ listesinden minimum mesafeyi bulun ve yazdırın."""

# min distance diye bir değişken oluşturdum. Math metodundaki min ile distances listesini parametre olarak girdim.
min_distance = min(distance)
print("Minimum Mesafe:", min_distance)
