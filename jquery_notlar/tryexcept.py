#try except else finally
# x = 5
# try:
#     print(x)
#     #çalıştırmayı ve hatalarını kontrol etmeyi deneyeceğim kod bloğu
# except NameError:
#     #nameError yani değişken tanımlanmadıysa gösterilecek hata için bu işlemler yapılacak.
#     print('x tanımlı değil')
# except: 
#     #geri kalan hatalar için oluşturuldu.
#     print('Başka bir hata oluştu.')
# else: 
#     # hiçbir hata çıkmadığı ve try içerisinde denenen kod çalıştığı durumda burası gösterilir.
#     print('x değişkeni ekrana yazdırıldı.')
# finally:
#     # kodlar çalışsa da çalışmasa da bu blok devreye girer.
#     print('Try bloğu tamamen denendi.')


# print('selam')


'''
NameError : Değişken oluşturulamama hatası.
ZeroDivisionError: 0 ile bölme işlemi denendiğinde gelir.
ValueError: Girilen değerin hatalı olması durumu
KeyboardInterrupt: Ctrl+c ile programı zorla durdurduğumuzda gelir.
TypeError: Uygun veri tipleri uygun işlemlerle kullanılmadığında gelir.
RunTimeError: Diğer kategorilere dahil olmayan özel hatalar için verilir.
SyntaxError: İstenilen syntax kurallarına uyulmazsa verilir.
MemoryError:  RAM içinde program çalışması için yeterli yer kalmazsa verilir.
KeyError: Var olmayan bir key çağırılmaya çalışılırsa verilir.
IndexError: Var olmayan index çağırılmaya çalışılırsa verilir.
ModuleNotFoundError: İmport edilmek istenen modül yoksa verilir.

'''

x = int(input('Lütfen bir sayı girin (pozitif): '))

if x < 0:
    raise ValueError('X değeri 0 dan küçük olamaz')
else:
    print('x değeri kaydedildi.')


print('asdasdasd')