# UDE — Apple Silicon (arm64) Native

[Uyap Doküman Editörü](https://uyap.gov.tr)'nü (UDE) Apple Silicon (M1/M2/M3/M4)
Mac'lerde **Rosetta olmadan** native çalıştırır. Rosetta çeviri katmanı olmadığı için
**daha hızlı** açılır ve çalışır. Java gömülü gelir; ayrıca bir şey kurmaya gerek yoktur
ve `.udf` dosyalarına **çift tıklayarak** açabilirsiniz.

> 💻 **Intel Mac'iniz mi var?** Aşağıdaki tüm mimari-bağımsız iyileştirmeler (keskin metin,
> modern ikonlar, Mac kısayolları, native pencereler, e-imza, PDF Türkçe harf) Intel'de de
> geçerli. Kurulum komutu için bkz. **[Intel işlemcili Mac'ler için](#-intel-işlemcili-macler-için)**.

![UDE — modern Material ikonlar ve Retina'da keskin metin](assets/ekran-goruntusu.jpeg)

> Modern Material ikonlar + Java 11 HiDPI ile **Retina'da keskin** metin ve arayüz.

### Önce / Sonra

Aynı belge, aynı Retina ekranda. **Solda** resmî paket (Rosetta + Java 8: tüm pencere
bulanık); **sağda** bu derleme (native + Java 11: metin keskin, modern düz Word-2026
görünümü ve koyu mod).

| Öncesi — resmî paket (bulanık) | Sonrası — bu derleme (keskin, koyu) |
|:---:|:---:|
| ![Önce: bulanık, eski turkuaz görünüm](assets/before-blurry.png) | ![Sonra: keskin, koyu Word-2026 görünümü](assets/after-word2026.png) |

> Modern görünüm, sistem teması neyse onu takip eder — açık modda da aynı düz Word-2026 arayüzü:

![Açık modda Word-2026 görünümü](assets/after-word2026-light.png)

> ⚠️ **Bu depo UYAP Doküman Editörü'nün kaynak kodunu içermez.** Tamamen bağımsız,
> **gayriresmî** bir Mac **yamasıdır**: hiçbir kamu kurumu tarafından
> geliştirilmemiş/onaylanmamıştır. Burada bulunan yalnızca yama ve build betikleridir;
> resmî UDE paketi build sırasında uyap.gov.tr'den **siz** indirir ve yamayı uygulamanın
> üstüne **siz** çalıştırırsınız. "Olduğu gibi" sunulur.

> ✅ **E-imza çalışıyor:** Akıllı kart okuyucu algılaması (`5.4.17_4`+) çözüldü —
> gömülü Java artık PCSC üzerinden kartı görüyor ve imzalama akışı baştan sona
> çalışıyor. Belge açma/düzenleme de sorunsuz.

> 🗂️ **Native macOS dosya pencereleri:** Aç / Kaydet / Farklı Kaydet artık eski
> görünümlü Java penceresi yerine macOS'un **kendi** dosya penceresini kullanır —
> Finder kenar çubuğu, iCloud Drive, son kullanılanlar ve `.udf` filtresiyle.

![UDE — native macOS Aç/Kaydet penceresi](assets/native-dosya-penceresi.png)

> Aç/Kaydet pencereleri artık macOS'un native dosya seçicisi.

> 📦 **Hazır (paketlenmiş) uygulama dağıtılmaz.** İşgüzarlarla uğraşmak istemediğim
> için paketlenmiş hâlini dağıtmıyorum; uygulamayı **kendiniz derleyip paketlersiniz**.
> Bu sayfada bir "Releases" / hazır indirme bağlantısı **bulmazsınız**. Aşağıdaki adımlar
> derlemeyi olabildiğince kolaylaştırır — komutları kopyala-yapıştır ile çalıştırmanız yeterli.

---

# 👩‍⚖️ Kolay kurulum — tek satır

Programcı olmanıza gerek yok. **Terminal** uygulamasını açın (klavyede
`Command (⌘) + Boşluk`'a basıp açılan kutuya **Terminal** yazın ve **Enter**'a basın),
ardından aşağıdaki **tek satırı** kopyalayıp yapıştırın ve **Enter**'a basın:

```bash
arch -arm64 bash -c "$(curl -fsSL https://raw.githubusercontent.com/saidsurucu/ude-mac-arm64/main/kur.sh)"
```

Hepsi bu kadar. Manuel indirme, klasöre girme, Java kurma gibi adımlar **yok**. Bu komut
gerisini sizin için yapar:

- Gerekiyorsa **geliştirici araçlarını** (Xcode komut satırı araçları) kurar — bir pencere
  açılırsa yalnızca **"Yükle"**ye basıp bitmesini bekleyin, betik kendiliğinden devam eder.
- **Kaynak kodu** `~/ude-mac-arm64` klasörüne indirir (zaten varsa en güncel sürüme günceller).
- Gereken **Java** sürümlerini otomatik indirir.
- Uygulamayı modern ikonlarla **derler + imzalar** ve doğrudan **/Applications** klasörüne kurar.

İlk derleme internet hızınıza göre birkaç dakika sürebilir.

Bittiğinde uygulama **Launchpad** ve **Applications** klasöründe hazırdır; çift tıklayarak
ya da `.udf` dosyalarına çift tıklayarak açabilirsiniz. (Kendiniz derleyip imzaladığınız
için macOS "geliştirici doğrulanamadı" uyarısı **çıkmaz**; `xattr` ile uğraşmanıza gerek
yoktur.)

**Yeni Editör sürümü çıktığında yukarıdaki tek satırı yeniden çalıştırmanız yeterli. En
güncel sürüm otomatik inecek ve yamalanacak.**

## 💻 Intel işlemcili Mac'ler için

Mac'iniz Intel (x86_64) işlemcili ise — yani Apple Silicon (M1/M2/M3/M4) **değilse** —
aynı kurulumu şu **tek satırla** yapın (Apple Silicon'dakinin aksine `arch -arm64`
**yoktur**; Intel zaten yalnız x86_64'tür):

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/saidsurucu/ude-mac-arm64/main/kur.sh)"
```

> Mimarinizden emin değil misiniz? Sol üstteki **Apple () menüsü → Bu Mac Hakkında**'ya
> bakın: **"Apple M…"** yazıyorsa üstteki Apple Silicon komutunu, **"Intel"** yazıyorsa
> bu komutu kullanın. (Betik mimariyi kendisi de algılar; yanlış komutu çalıştırırsanız
> sizi uyarır.)

Intel'de resmî UDE paketi zaten x86_64 olduğu için burada kazanç "Rosetta'sız native hız"
**değildir**; kazanç şunlardır: **Java 11 ile Retina'da keskin metin**, **modern Material
ikonlar**, *