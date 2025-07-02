# Video_language_translator
---
## ✅ `README.md` কনটেন্ট:

# 🎥 Voice Translator from Any Video Link (Offline + No API)

এই প্রজেক্টটি এমন একটি সিস্টেম যেখানে যেকোনো ভিডিও লিংক দিয়ে আপনি সেই ভিডিওর কথাগুলো আপনার পছন্দের ভাষায় ট্রান্সলেট করতে পারবেন — শুধু সাবটাইটেল নয়, বরং পুরো অডিও আপনার ভাষায় শুনতে পারবেন। কোনো API দরকার হয় না। সম্পূর্ণ অফলাইন।





## 📦 প্রয়োজনীয় প্যাকেজ ও ইনস্টলেশন

প্রথমে নিচের কমান্ডটি দিয়ে সকল প্রয়োজনীয় প্যাকেজ ইনস্টল করুন:
---
```
pip install -r requirements.txt
````

📂 `requirements.txt` ফাইলের ভিতরে থাকা প্যাকেজগুলো:

* flask
* yt-dlp
* openai-whisper
* argos-translate
* ffmpeg-python

---

## ⚙️ অতিরিক্ত সফটওয়্যার যা লাগবে:

1. ✅ `ffmpeg`
   [ডাউনলোড লিংক](https://ffmpeg.org/download.html)
   অথবা Linux/Termux-এ:

   ```bash
   pkg install ffmpeg
   ```

2. ✅ `espeak-ng` (Text-to-speech)

   ```bash
   apt install espeak-ng
   ```

3. ✅ Argos Translate language packages:
   প্রথমবার রান করার সময় Argos নিজেই বাংলা/ইংরেজি/আরবি এর মতো ভাষার প্যাকেজ ইনস্টল করতে বলবে। আপনি চাইলে [এখান থেকে](https://www.argosopentech.com/argospm/index/) প্যাকেজ ডাউনলোড করে ইনস্টল করতে পারেন।

---

## 🚀 ব্যবহার বিধি:
1. GitHub clone করুন:
``` 
git clone https://github.com/RH0099/Video_language_translator.git
```
2. প্রজেক্ট ফোল্ডারে যান:

```bash
cd Video_language_translator
```

3. Flask অ্যাপ চালু করুন:

```bash
python main.py
```

4. আপনার ব্রাউজারে যান:

```
http://127.0.0.1:5000
```

5. সেখানে:

* 🎯 ভিডিও লিংক দিন (YouTube, etc.)
* 🌐 ভাষা নির্বাচন করুন (বাংলা, ইংরেজি, আরবি, হিন্দি)
* ▶️ “Start Translation” বাটনে ক্লিক করুন

6. সিস্টেম:

* ভিডিও নামাবে
* অডিও থেকে স্পিচ আলাদা করবে
* স্পিচ ট্রান্সলেট করবে
* নতুন ভয়েস বানাবে
* ভিডিওতে বসিয়ে আপনাকে ডাউনলোড লিংক দেবে

---

## 💡 সাপোর্টেড ভাষা

* বাংলা (bn)
* ইংরেজি (en)
* আরবি (ar)
* হিন্দি (hi)

**নতুন ভাষা যোগ করতে চান?**
→ Argos Translate থেকে নতুন ভাষা প্যাকেজ ইনস্টল করে `translator.py` তে কোড যুক্ত করুন।

---

## 📜 লাইসেন্স

এই প্রজেক্টটি সম্পূর্ণ ওপেন-সোর্স এবং API-ফ্রি। আপনি চাইলে এটি ব্যবহার, কাস্টমাইজ, বা রিডিস্ট্রিবিউট করতে পারেন।

---

## 🤝 ডেভেলপার

🧠 তৈরি করেছেন: # [RH](https://www.facebook.com/Rad.Hacker)

👥 টিম :📿☝️Muslim Army☝️📿

```
