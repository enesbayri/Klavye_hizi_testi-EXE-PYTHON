from datetime import datetime
import random
import time



metin1="Cetvel yapma düzeni şaryonun hareketini ve istenilen yerde durmasını sağlar Bu düzeni kullanmak bize zaman kazandırır Bir çizelgedeki sütunların arasındaki boşluk için her satırda sekiz on kez aralık çubuğuna vurmak her paragraf başında yedi kez aralık Başlıklar kağıda ya da yazıya ortalanıp yazılır Kağıdın yatay orta noktasını buluruz şaryoyu buraya getiririz Her iki vuruşluk yer için bir kez geri tuşuna basarız Harfleri ve boşlukları içimizden söylerken geri tuşuna da basarız Sonda tek harf kalıyorsa bu Silgi kağıda yalnız bir yönde temas ettirilmelidir Geriye dönüşlerde silgiyi hafifçe kaldırmak kağıda değdirmemek gerekir Saçımızı tararken tarağı nasıl tek yönlü kullanıyorsak silgi de aynı şekilde tek yönlü kullanılmalıdır. Böyle yaparsak kağıt"
metin2="Okumaya veya basılmaya hazır bir yazının daktilo ile yazılmış son şekline manüskri denir Manüskri için son müsvedde de denilebilir Rapor makale ders notu nutuk ile tez ve manüskri şeklinde yazılır Manüskriler iki ara ile yazılır Paragraflar arasında Kelime içinde bir iki harf atlanmış olabilir Bütün yazıyı yeniden yazmamak için eksik harflerin araya sıkıştırılması mümkündür Gereği kadar harf silinir Başparmakla uygun şekilde geri tuşuna basılır Parmak geri tuşunda tutulur Sıkıştırılacak ilk harfe vurulur Daktilo silgileri sert kurşun kalem silgileri de yumuşak silgilerdir Üstteki kağıt için sert silgi yani daktilo silgisi kullanılır Alt kopyalar yani karbonlu kopyalar için yumuşak silgi kullanmak da mümkündür Şerit çok yeni ise üst sayfada bulunan yanlış da önce"
metin3="Parçaları kullanırken bakma Öğrenci kolu attıktan sonra elini yerleştirmek için tuşlara bakabilir Bu durum da kötü bir alışkanlık olarak yerleşmeden önlenmelidir Serbest tuşunu iyi kullanılmasını öğrenmemiş olan öğrenci satır sonlarında makineye bakar Düz Bir yazıyı daktilo ile yazdıktan sonra makineden çıkarmadan önce baştan sona kadar yeniden ve dikkatlice okumak gerekir Yazıyı kağıt makinedeyken okumayıp da makineden çıkardıktan sonra okur isek bulunacak yanlışı düzeltmek zor olur Çünkü Bir cetveli yatay olarak ortalamak için cetvelin kaç vuruşluk yer kapladığını buluruz Bunu kağıdın aldığı vuruş sayısından çıkarırız Bulduğumuz sayıyı marjlar için ikile paylaştırırız marjları düzenleriz Bundan sonra tabülatör durağı yapılacak sütun"
metin4="Yazı içinde geçen tek sütunlu kısımlar olabilir Bunların kağıda ve veya yazıya ortalanması uygun görünüm verebilir Bazen de tek sütunluk bir çizelge yazılabilir Bu tür tek sütunlu yazılar blok halinde ortalanır buna blok ortalama denilir Bunu yapmak Bir çizelgeyi dikey olarak ortalamak için bu çizelgenin kaç satırlık yer kaplayacağı bulunur Bu da satır sayısına boşlukların satır sayısı eklenerek bulunur Bulunan sayı kağıdın aldığı satır sayısından çıkartılır Kalan üst ve alt marjlara paylaştırılır Mumlu kağıtlar çoğaltma teksir yapmak için kullanılır Yazıya başlarken şerit düzeni beyaz da yani mumlu kağıt yazım düzeninde olmalıdır Harf çekirdeklerinin temiz olması mum ve mürekkep artıklarından temizlenmesi gerekir Bu temizlik yapılmaz ise"
metinler=[metin1,metin2,metin3,metin4]
metin=random.choice(metinler)
metinislem=metin.split(" ")

print("program basliyor bitirmek için ENTER'e basiniz")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
print("BASLA!")
print("\n"+metin+"\n")

before=datetime.now()
alinan=input("BURAYA GİRİNİZ: ")
after=datetime.now()
sure=(after-before).seconds

dogru=0
alinan=alinan.split(" ")


for i in range(len(alinan)):
    if alinan[i]==metinislem[i]:
        dogru+=1
    elif(len(alinan)>len(metinislem) and i>=len(metinislem)):
        break
puan=(100/len(metinislem))*dogru
print("{} saniyede {} kelime yazdiniz...".format(sure,len(alinan)))
print("Dogru kelime sayiniz: {}".format(dogru))
print("saniyede kelime girisi: {}".format(round(len(alinan)/sure,2)))
print("PUANINIZ: {}/100".format(round(puan,2)))

