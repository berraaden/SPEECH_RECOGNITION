import speech_recognition as sr #ses kütüp. dahil ettik

r = sr.Recognizer() #tanıma fonksiyonunu çağırdık

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) #ortamdaki seslerden temizle, ayarlama yap
    print("5 saniye boyunca konuşmaya devam edebilirsiniz:")
    kayit = r.record(source,duration=10) #5 saniye boyunca record etmesini sağladık
    print(":::::::SES KAYIT İŞLMELERİ YAPILIYOR:::::::")
    metin = r.recognize_google(kayit,language="tr")  #google a bağlan ve türkçe kaynak algıla
    print(metin)