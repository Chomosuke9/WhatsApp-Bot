import hashlib
import random

daftar_khodam = ("Sucipto Tomat", "Kucing Mewing", "Perkedel Sayap", "Icikiwir", "Sempak Firaun",
                 "Ratu Iblis", "Bang Jago", "Kuda Cebol", "Sendal Jepit", "Balmond",
                 "Gajah Berbulu Domba", "Singa Tertawa", "Mi Goreng", "Slamet Kopling", "Ular Karet",
                 "Buaya Panci", "Elang Ubur-ubur", "Raja Iblis", "Kijang Diso", "Kucing Garong",
                 "Burung Halu", "Tupai Loncat", "Kura-Kura Ninja", "Macan Pink", "Burung Gelanggang",
                 "Kerbau Polkadot", "Ikan Selam", "Lumba-lumba Cepirit", "Ayam Kriuk", "Burung Cempreng",
                 "Anjing Kribo", "Bebek Jambul", "Domba Kocak", "Jerapah Woles", "Ikan Terbang",
                 "Burung Gigi", "Kuda Kocak", "Katak Goyang", "Burung Kipas", "Anjing Geboy",
                 "Burung Cengeng", "Ular Kadut", "Ikan Goreng", "Kuda Kipas", "Serigala Lucu",
                 "Burung Ketawa", "Kuda Kayu", "Burung Jempol", "Gajah Guling", "Ular Terbang")
arti_khodam = [
    "Kamu adalah petani tomat legendaris yang menguasai kebun-kebun sakti",
    "Kamu memiliki jiwa kucing yang selalu penasaran dan membawa keberuntungan",
    "Kamu adalah perkedel terbang yang memberikan rasa nyaman dan kebahagiaan",
    "Kamu adalah si pendek yang baik hati",
    "Kamu adalah penguasa dari zaman Mesir kuno yang terlahir kembali dengan keberanian yang tak tertandingi",
    "Kamu mendapat berkah berupa kecantikan yang luar biasa",
    "Kamu adalah pahlawan kampung yang selalu siap membela kebenaran",
    "Kamu adalah kuda kecil dengan kekuatan besar yang melampaui batas",
    "Kamu adalah simbol kenyamanan dan ketangguhan dalam kehidupan sehari-hari",
    "Kamu adalah pejuang tangguh dari dunia fantasi yang tidak kenal takut",
    "Kamu adalah kombinasi kekuatan dan kelembutan, membawa kedamaian di mana pun kamu berada",
    "Kamu memiliki kekuatan singa dengan jiwa humor yang menyenangkan",
    "Kamu membawa kehangatan dan kebahagiaan dalam setiap situasi",
    "Kamu adalah penguasa kendaraan dengan keahlian mengendalikan segala sesuatu",
    "Kamu adalah simbol fleksibilitas dan kemampuan beradaptasi dalam segala situasi",
    "Kamu memiliki daya tahan luar biasa, mampu bertahan dalam kondisi apapun",
    "Kamu adalah kombinasi kecepatan dan kelembutan yang memukau",
    "Kamu adalah reinkarnasi dari raja iblis dari dunia lain yang terlahir di dunia ini",
    "Kamu memiliki kecepatan dan ketangkasan yang tak tertandingi",
    "Kamu adalah penjaga malam yang selalu waspada dan melindungi sekitar",
    "Kamu adalah pembawa mimpi-mimpi indah dan inspirasi tak terbatas",
    "Kamu memiliki energi dan keceriaan yang menular ke orang lain",
    "Kamu adalah pejuang yang lambat tapi pasti dalam mencapai tujuan",
    "Kamu adalah macan dengan sentuhan lembut yang menawan",
    "Kamu adalah penerbang tinggi yang membawa kebebasan dan petualangan",
    "Kamu adalah simbol keunikan dan kekuatan yang berbeda",
    "Kamu adalah penjelajah laut yang penuh dengan misteri dan pengetahuan",
    "Kamu adalah makhluk laut yang ceria dan membawa keceriaan",
    "Kamu adalah simbol kebahagiaan dan kenikmatan dalam hidup",
    "Kamu adalah suara riang yang selalu membawa kebahagiaan",
    "Kamu adalah teman setia yang penuh dengan cinta dan perhatian",
    "Kamu adalah makhluk air yang unik dengan keindahan tersendiri",
    "Kamu adalah pembawa tawa dan keceriaan di segala situasi",
    "Kamu adalah simbol ketenangan dan kebijaksanaan yang tinggi",
    "Kamu adalah penjelajah yang tak kenal batas, selalu mencari hal baru",
    "Kamu memiliki kekuatan dan keunikan yang luar biasa",
    "Kamu adalah simbol kegembiraan dan energi yang tak terbatas",
    "Kamu adalah makhluk yang membawa ritme dan kegembiraan",
    "Kamu adalah simbol kesejukan dan ketenangan",
    "Kamu adalah teman setia yang penuh dengan semangat",
    "Kamu adalah suara lembut yang selalu menyentuh hati",
    "Kamu adalah makhluk yang fleksibel dan penuh dengan kejutan",
    "Kamu adalah simbol kelezatan dan kebahagiaan dalam hidup",
    "Kamu adalah makhluk yang membawa kesejukan dan kedamaian",
    "Kamu adalah pembawa keceriaan dan kebahagiaan di segala situasi",
    "Kamu adalah simbol tawa dan kebahagiaan yang menular",
    "Kamu adalah simbol ketangguhan dan keabadian",
    "Kamu adalah makhluk yang selalu memberi dukungan dan inspirasi",
    "Kamu adalah simbol kekuatan dan keanggunan yang bersatu",
    "Kamu adalah makhluk yang melampaui batas, membawa kejutan dan keajaiban"
]
khodam = ""
nama = ""


def cek_khodam(nama):
    while nama == "":
        break
    else:
        global angka_khodam
        space_remover = nama.replace(" ", "")
        lowercaser = space_remover.lower()
        hasil_hash = hashlib.md5(lowercaser.encode()).hexdigest()
        angka_hash = int(hasil_hash, 16)
        random.seed(angka_hash)
        angka_khodam = random.randint(0, 49)
        khodam = daftar_khodam[angka_khodam]
        return khodam
def arti():
    arti=arti_khodam[angka_khodam]
    return arti
