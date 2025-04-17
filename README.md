# Connected Component Labeling with Two-Pass Algorithm

Bu proje, herhangi bir harici kütüphane kullanılmadan, bağlı bileşen etiketleme (Connected Component Labeling, CCL) problemini çözmek için **Two-Pass** algoritmasının saf Python ile uygulanmasını içermektedir. Kodlar, algoritmanın mantığını öğretici ve modüler bir şekilde açıklamak amacıyla fonksiyonlar hâlinde yazılmıştır.

## 📌 Bağlı Bileşen Etiketleme Nedir?

Bağlı bileşen etiketleme (Connected Component Labeling, CCL), ikili (binary) görüntülerdeki birbirine bitişik (komşu) olan pikselleri tespit ederek bu kümeleri benzersiz etiketlerle ayıran temel bir görüntü işleme yöntemidir. Görüntüdeki nesneleri ve arka planı ayırmak, nesne sayımı yapmak ya da nesneler üzerinde ölçümler gerçekleştirmek gibi birçok temel analiz için ön koşul niteliğindedir.

Bir bağlı bileşen, belirli bir bağlantılılık (4'lü veya 8'li komşuluk) tanımına göre, aynı değere (genellikle "1") sahip ve birbirine bağlı olan piksellerin oluşturduğu bir kümedir.

## 🔍 Bağlı Bileşen Etiketlemede Kullanılan Yöntemler

Bağlı bileşen etiketleme için literatürde farklı algoritmalar geliştirilmiştir. En yaygın kullanılan yöntemler şunlardır:

- **One-Pass (Tek Geçişli) Yöntemler**  
  Genellikle union-find (birleştir-bul) veri yapısını paralel programlamayla birleştiren yöntemlerdir. GPU uygulamaları için uygundur ancak veri yapısı ve eşzamanlılık nedeniyle karmaşıktır.

- **Two-Pass (İki Geçişli) Algoritma**  
  Basitliği ve teorik açıklanabilirliği açısından sıklıkla tercih edilir. İlk geçişte etiket ataması yapılırken, ikinci geçişte bu etiketler sadeleştirilerek nihai hale getirilir.

- **Multi-Pass (Çok Geçişli) ve Rekürsif Yöntemler**  
  Bu tür algoritmalar genellikle tekrarlı olarak tüm görüntüde tarama yaparak değişiklik kalmayana kadar çalışırlar. Hesaplama maliyetleri yüksektir.

## 🧠 Two-Pass Algoritması Nasıl Çalışır?

Two-Pass algoritması, iki aşamalı bir işlemdir:

1. **İlk Geçiş (Labeling + Equivalence):**  
   Görüntü satır satır taranır. Her pikselin komşuları (genellikle üst ve sol komşular) kontrol edilerek:
   - Komşularda etiket yoksa, yeni bir etiket atanır.
   - Komşularda tek bir etiket varsa, bu etiket atanır.
   - Komşularda birden fazla etiket varsa, en küçük etiket atanır ve bu etiketlerin eşdeğer olduğu kaydedilir.

2. **İkinci Geçiş (Label Resolution):**  
   İlk geçişte oluşturulan etiket eşdeğerliliği (equivalence table) çözülerek, tüm geçici etiketler nihai etiketlerine dönüştürülür. Böylece her bağlı bileşen benzersiz ve tutarlı bir şekilde etiketlenmiş olur.

### ✅ Avantajları
- Uygulaması basit ve öğreticidir.
- Herhangi bir dış kütüphane veya karmaşık veri yapısı gerektirmez.
- Küçük ve orta ölçekli görüntülerde oldukça verimlidir.

### ❌ Dezavantajları
- Büyük görüntülerde bellek erişimi ve eşdeğerlik çözümlemesi nedeniyle yavaş çalışabilir.
- Paralel programlamaya uygun değildir.

## 📚 Two-Pass Algoritmasının Teorik Anlatımı

Two-Pass algoritması, temel olarak etiketleme ve etiket çözümleme olmak üzere iki aşamalı bir işlem dizisine dayanır. Bu süreçte kullanılan temel kavramlar:

- **4’lü / 8’li Komşuluk:**  
  Piksellerin birbirine bağlı sayılabilmesi için aralarındaki mekânsal ilişki. 4’lü komşulukta sadece yukarı, aşağı, sağ ve sol; 8’li komşulukta çaprazlar da dahil edilir.

- **Eşdeğerlik (Equivalence):**  
  İki veya daha fazla etiketin aynı bağlı bileşene ait olduğunun anlaşılmasıdır. Bu eşdeğerlikler, birleştir-bul (union-find) veri yapısı ile veya sade dizisel yapı ile tutulabilir.

- **Etiket Propagasyonu:**  
  Eşdeğer etiketlerin sadeleştirilerek en küçük temsilci etiket ile ifade edilmesidir.

Aşağıdaki matematiksel ifade, bir pikselin etiketlenme sürecini açıklar:

Verilen bir piksel \( p \), komşu pikselleri kümesi \( N(p) \) ile tanımlansın. Eğer \( \exists q \in N(p) \) ve \( I(q) = 1 \), o halde:

- Eğer \( \forall q \in N(p), L(q) = 0 \) ise: yeni etiket ata.
- Eğer \( \exists q \in N(p), L(q) > 0 \) ise: en küçük \( L(q) \)'yi ata.
- Eğer birden fazla \( L(q) > 0 \) ise: eşdeğerlikleri kaydet.

İkinci geçişte, her etiket için eşdeğerlik tablosundan nihai etikete dönüştürme işlemi gerçekleştirilir.

## 🔄 Two-Pass Algoritmasının Görsel Açıklaması

![Two-Pass Algoritması Görseli](https://www.aishack.in/static/images/connected-components/first-pass.png)

*Kaynak: [AI Shack](https://www.aishack.in/tutorials/labelling-connected-components-example/)*

Yukarıdaki görsel, Two-Pass algoritmasının ilk geçişinde etiketleme sürecini göstermektedir. Her piksel, komşularına göre etiketlenir ve eşdeğerlikler kaydedilir.

## 📎 Faydalı Kaynaklar

- [AI Shack: Connected Components Labeling](https://www.aishack.in/tutorials/labelling-connected-components-example/)
- [CodeProject: Connected Component Labeling](https://www.codeproject.com/Articles/336915/Connected-Component-Labeling-Algorithm)
- [HandWiki: Connected-component labeling](https://handwiki.org/wiki/Connected-component_labeling)

## 🛠️ Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına göz atınız.
