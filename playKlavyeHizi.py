import play 
import random
from datetime import datetime

arkaplan=play.new_image(image="keyb1.png",size=20,transparency=25)
def diziGizle(dizi):
    for i in range(len(dizi)):
        dizi[i].hide()
def diziGoster(dizi):
    for i in range(len(dizi)):
        dizi[i].show()
def fizikacma(dizi):
    for i in range(len(dizi)):
        dizi[i].start_physics()
def birlestir(dizi):
    yazi=""
    for i in range(len(dizi)):
        if i==0 or i==1:
            continue
        else:
            yazi+=dizi[i].words
    return yazi
z=0
yazi1=play.new_text(words="(: Hosgeldiniz :)",color="red",font_size=100)
yazi2=play.new_text(words="Bu uygulamada klavye hızınızı ölçeceksiniz!")
yazi3=play.new_text(words="BAŞARILAR!",font_size=70)
buton1=[play.new_box(color="grey",border_color="yellow",border_width=5,width=500,height=60,),play.new_text(words="HAZIR OLDUĞUNUZDA TIKLAYINIZ...",font_size=30,)]
hazirlik=play.new_text(words="Basliyor...",font_size=100,y=200)
yer2=-30
"""yazilan=play.new_text(words="",font_size=28,y=yer2)
baslangici=play.new_text(words="GİRİNİZ --> ",font_size=30,x=-300)
cerceve=play.new_box(color="white",border_color="black",y=-120,border_width=3,width=750,height=320,)
yazilanlar=[cerceve,baslangici,yazilan]"""

yazilanlar=[play.new_box(color="white",border_color="black",y=-120,border_width=3,width=750,height=320,),play.new_text(words="GİRİNİZ --> ",font_size=30,x=-300),play.new_text(words="",font_size=28,y=yer2)]

s1=play.new_text(words="",font_size=50,)
s2=play.new_text(words="",font_size=50,y=-50)
s3=play.new_text(words="",font_size=50,y=-100)
s4=play.new_text(words="",font_size=50,y=-150)
s5=play.new_text(words="",font_size=100,color="red",x=150,y=-200)
s1.hide()
s2.hide()
s3.hide()
s4.hide()
s5.hide()
sureTut=0
            

sayac=0

metin1="cetvel yapma düzeni şaryonun hareketini ve istenilen yerde durmasını sağlar. bu düzeni kullanmak bize zaman kazandırır bir çizelgedeki sütunların arasındaki boşluk. için her satırda sekiz on kez aralık çubuğuna vurmak her paragraf başında yedi kez aralık. başlıklar kağıda ya da yazıya ortalanıp yazılır kağıdın yatay orta noktasını buluruz şaryoyu. buraya getiririz her iki vuruşluk yer için bir kez geri tuşuna basarız harfleri ve boşlukları. içimizden söylerken geri tuşuna da basarız sonda tek harf kalıyorsa bu silgi kağıda yalnız. bir yönde temas ettirilmelidir geriye silgiyi hafifçe kaldırmak kağıda değdirmemek gerekir. saçımızı tararken tarağı nasıl tek yönlü kullanıyorsak silgi de aynı şekilde tek yönlü"
metin2="okumaya veya basılmaya hazır bir yazının daktilo ile yazılmış son şekline. manüskri denir manüskri için son müsvedde de denilebilir rapor makale ders notu nutuk. ile tez ve manüskri şeklinde yazılır manüskriler iki ara ile yazılır paragraflar arasında. kelime içinde bir iki harf atlanmış olabilir bütün yazıyı yeniden yazmamak için eksik harflerin. araya sıkıştırılması mümkündür gereği kadar harf silinir başparmakla uygun şekilde geri tuşuna. basılır parmak geri tuşunda tutulur sıkıştırılacak ilk harfe vurulur daktilo silgileri sert. kurşun kalem silgileri de yumuşak silgilerdir üstteki kağıt için sert silgi yani daktilo silgisi. alt kopyalar yani karbonlu kopyalar için yumuşak silgi kullanmak da mümkündür şerit"
metin3="parçaları kullanırken bakma öğrenci kolu attıktan sonra elini yerleştirmek. için tuşlara bakabilir bu durum da kötü bir alışkanlık olarak yerleşmeden önlenmelidir. serbest tuşunu iyi kullanılmasını öğrenmemiş olan öğrenci satır sonlarında makineye bakar. düz bir yazıyı daktilo ile yazdıktan sonra makineden çıkarmadan önce baştan sona kadar yeniden. ve dikkatlice okumak gerekir yazıyı kağıt makinedeyken okumayıp da makineden çıkardıktan sonra. okur isek bulunacak yanlışı düzeltmek zor olur çünkü bir cetveli yatay olarak ortalamak için. cetvelin kaç vuruşluk yer kapladığını buluruz bunu kağıdın aldığı vuruş sayısından çıkarırız. bulduğumuz sayıyı marjlar için ikile paylaştırırız marjları düzenleriz bundan sonra tabülatör"
metin4="yazı içinde geçen tek sütunlu kısımlar olabilir bunların kağıda ve veya yazıya. ortalanması uygun görünüm verebilir bazen de tek sütunluk bir çizelge yazılabilir. bu tür tek sütunlu yazılar blok halinde ortalanır buna blok ortalama denilir bunu yapmak bir. çizelgeyi dikey olarak ortalamak için bu çizelgenin kaç satırlık yer kaplayacağı bulunur. bu da satır sayısına boşlukların satır sayısı eklenerek bulunur bulunan sayı kağıdın aldığı satır. sayısından çıkartılır kalan üst ve alt marjlara paylaştırılır mumlu kağıtlar çoğaltma teksir. yapmak için yazıya başlarken şerit düzeni beyaz da yani mumlu kağıt yazım düzeninde olmalıdır. harf çekirdeklerinin temiz olması mum ve mürekkep artıklarından temizlenmesi gerekir"
metinler=[metin1,metin2,metin3,metin4]
metin=random.choice(metinler)
önceki_karakterler =      ["ş","ç","ö","ğ","ü",]
sonraki_karakterler =   ["s", "c", "o", "g","u",]
for i in range(5):
    metin=metin.replace(önceki_karakterler[i],sonraki_karakterler[i])
metin2=metin.split(".")
buton2=[play.new_box(color="white",border_color="black",y=175,border_width=5,width=750,height=200,)]



yer=245
for i in range(len(metin2)):
    buton2.append(play.new_text(words=metin2[i],font_size=23,y=yer))
    yer-=20


yazi1.hide()
yazi2.hide()
yazi3.hide()
hazirlik.hide()
tikla=False
gorunmez=buton1[0]
diziGizle(yazilanlar)
diziGizle(buton2)

@play.when_program_starts
async def do():
    buton1[0].hide()
    buton1[1].hide()
    
    yazi1.show()
    await play.timer(3)
    yazi1.hide()
    yazi2.show()
    await play.timer(3)
    yazi2.hide()
    yazi3.show()
    await play.timer(3)
    yazi3.hide()
    buton1[0].show()
    buton1[1].show()
    global tikla
    while(not tikla):
        tikla=buton1[1].is_clicked
        buton1[0].angle,buton1[1].angle=10,10
        await play.timer(0.3)
        await play.animate()
        tikla=buton1[1].is_clicked
        buton1[0].angle,buton1[1].angle=-10,-10
        await play.timer(0.3)
        await play.animate()
        tikla=buton1[1].is_clicked
        buton1[0].angle,buton1[1].angle=0,0
        await play.animate()
        await play.timer(1)
        tikla=buton1[1].is_clicked
    
    
@gorunmez.when_clicked
async def baslatici():
    buton1[0].remove()
    buton1[1].remove()
    global tikla
    tikla=True
    hazirlik.show()
    await play.timer(1)
    hazirlik.words="3"
    await play.timer(1)
    hazirlik.words="2"
    await play.timer(1)
    hazirlik.words="1"
    await play.timer(1)
    hazirlik.hide()
    diziGoster(yazilanlar)
    diziGoster(buton2)





before=0
after=0
@play.when_any_key_pressed
async def yaz(key):
    #encoding:utf-8
    
    try:
        global sureTut
        global before
        global after
        if sureTut==0:
            before=datetime.now()
            sureTut+=1
        global sayac
        diziGoster(yazilanlar)
        deger=ord(key)
        if deger==13:
            diziGizle(yazilanlar)
            after=datetime.now()
            sure=(after-before).seconds
            alinan=birlestir(yazilanlar)
            dogru=0
            alinan=alinan.split(" ")
            global metin
            metinislem=metin.split(" ")
            
            for i in range(len(alinan)):
                if alinan[i]==metinislem[i]:
                    dogru+=1
                elif(len(alinan)>len(metinislem) and i>=len(metinislem)):
                    break
            puan=(100/len(metinislem))*dogru
            sonuc1=str(sure)+" saniyede "+str(len(alinan))+" kelime yazdiniz..."
            sonuc2="Dogru kelime sayiniz: "+str(dogru)
            sonuc3="saniyede kelime girisi: "+str(round(len(alinan)/sure,2))
            sonuc4="PUANINIZ: "
            sonuc5=str(round(puan,2))+"/100"
            
            s1.words=sonuc1
            s2.words=sonuc2
            s3.words=sonuc3
            s4.words=sonuc4
            s5.words=sonuc5
            s1.show()
            s2.show()
            s3.show()
            s4.show()
            s5.show()
            diziGizle(buton2)
            
            veda=play.new_text(words="İZTEDİĞİNİZ ZAMAN HIZINIZI TEST EDEBİLİRSİNİZ :)",color="red",y=150,font_size=40)
            veda.show
            await play.timer(5)
            s1.start_physics()
            s2.start_physics()
            s3.start_physics()
            s4.start_physics()
            s5.start_physics()
            veda.start_physics()
            await play.animate()
            await play.timer(3)
            global z
            z=1
            
                
            
                        
            

        if ord(key)==127 or ord(key)==8:
            yazilanlar[-1].words=yazilanlar[-1].words[0:-1]
        else:
            sayac+=1
            yazilanlar[-1].words+=key
            
        if sayac==70:
            sayac=0
            global yer2
            yer2-=20
            yazilanlar.append(play.new_text(words="",font_size=28,y=yer2))

    

    except:
        pass
@play.repeat_forever
async def repeat():
    global z
    if z==1:
        quit()
            



        
    
        


    
    

    


    



    










play.start_program()