import requests
import json
import re
from datetime import datetime

USERNAME = "hamzawwui"

def analyze_post(caption, is_video=True):
    caption_lower = caption.lower()
    
    # 1. فحص قمع التحويل للأصل الرقمي (Lead Magnet Keywords)
    lead_keywords = ["دليل", "رابط", "خاص", "dm", "كومنت", "أرسل", "احصل", "free", "مجاني", "روتين", "daysline", "بايو", "bio"]
    has_funnel = any(k in caption_lower for k in lead_keywords)
    funnel_status = "نعم (تحويل للأصل الرقمي)" if has_funnel else "لا (بدون CTA)"
    
    # 2. ميزان 80/20
    if not is_video or len(caption) > 280:
        cat = "20% زاوية خاصة"
        post_type = "كاروسيل / منشور عميق"
    else:
        cat = "80% جذب سريع"
        post_type = "ريلز / فيديو سريع"
        
    # 3. معيار الجودة الاستراتيجي
    if has_funnel and cat == "80% جذب سريع":
        eval_score = "🌟 ممتاز: جذب سريع متصل بالقمع"
    elif has_funnel and cat == "20% زاوية خاصة":
        eval_score = "🌟 استثنائي: بناء هيبة وتحويل مباشر"
    elif not has_funnel and cat == "80% جذب سريع":
        eval_score = "⚠️ جذب عام بدون توجيه واضح للقمع"
    else:
        eval_score = "📌 محتوى بناء وعي ونواة فكرية"
        
    return post_type, cat, funnel_status, eval_score

def fetch_data():
    posts_list = []
    
    # مسار بديل موثوق لقراءة البروفايلات العامة بدون حظر السحابة
    url = f"https://imginn.com/{USERNAME}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"جاري جلب بيانات الحساب: {USERNAME}...")
    try:
        res = requests.get(url, headers=headers, timeout=20)
        print(f"حالة الاستجابة: {res.status_code}")
        
        if res.status_code == 200:
            # استخراج المنشورات والنصوص من عناصر الويب المفتوحة
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(res.text, "html.parser")
            items = soup.find_all("div", class_="item")
            
            for item in items[:12]: # سحب آخر 12 منشور
                desc_el = item.find("div", class_="desc")
                caption = desc_el.get_text(strip=True) if desc_el else ""
                
                # فحص هل البوست فيديو
                is_video = bool(item.find("i", class_="icon-video"))
                
                # استخراج التاريخ إن وجد
                time_el = item.find("span", class_="time")
                date_str = time_el.get_text(strip=True) if time_el else datetime.now().strftime("%Y-%m-%d")
                
                post_type, cat, funnel, score = analyze_post(caption, is_video)
                
                posts_list.append({
                    "التاريخ": date_str,
                    "نوع المحتوى": post_type,
                    "التصنيف": cat,
                    "النص": caption[:60] + "..." if len(caption) > 60 else (caption or "منشور بدون كابشن"),
                    "تحويل للأصل": funnel,
                    "التقييم النوعي": score,
                    "تفاعل (إعجاب/تعليق)": "📊 منشور مسجل"
                })
    except Exception as e:
        print(f"حدث خطأ أثناء الجلب: {e}")
        
    return posts_list

if __name__ == "__main__":
    posts = fetch_data()
    print(f"عدد المنشورات المستخرجة: {len(posts)}")
    if posts:
        with open("posts.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        print("تم حفظ posts.json بنجاح!")
    else:
        print("لم يتم العثور على منشورات لتسجيلها.")
