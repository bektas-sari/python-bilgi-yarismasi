# Python Flask Bilgi Yarışması Uygulaması

Bu proje, Flask kullanılarak geliştirilmiş basit bir bilgi yarışması web uygulamasıdır. Kullanıcılar, Python programlama dili hakkında 10 soruyu cevaplayarak bilgilerini test edebilirler.

## Özellikler

- 10 soruluk bir bilgi yarışması
- Her soru için 4 seçenek
- Anlık puan hesaplama
- Responsive tasarım

## Kurulum

1. Repoyu klonlayın:
   \`\`\`
   git clone https://github.com/bektas-sari/flask-quiz-app.git
   cd flask-quiz-app
   \`\`\`

2. Sanal ortam oluşturun ve aktifleştirin:
   \`\`\`
   python -m venv venv
   source venv/bin/activate  # Windows için: venv\Scripts\activate
   \`\`\`

3. Gerekli paketleri yükleyin:
   \`\`\`
   pip install -r requirements.txt
   \`\`\`

4. Uygulamayı çalıştırın:
   \`\`\`
   python app.py
   \`\`\`

5. Tarayıcınızda \`http://localhost:5000\` adresine gidin.

## Kullanım

- Ana sayfada "Başla" butonuna tıklayarak yarışmayı başlatın.
- Her soru için bir seçenek seçin ve "Sonraki Soru" butonuna tıklayın.
- Son sorudan sonra, toplam puanınızı göreceksiniz.
- "Tekrar Dene" butonuna tıklayarak yarışmayı yeniden başlatabilirsiniz.

## Katkıda Bulunma

1. Bu repoyu fork edin
2. Yeni bir özellik dalı oluşturun (\`git checkout -b yeni-ozellik\`)
3. Değişikliklerinizi commit edin (\`git commit -am 'Yeni özellik: Açıklama'\`)
4. Dalınıza push yapın (\`git push origin yeni-ozellik\`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için \`LICENSE\` dosyasına bakın.

