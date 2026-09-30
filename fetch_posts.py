import requests
import json
import os
from datetime import datetime

USERNAME = "hamzawwui"

def analyze_post(caption, is_video=True):
    caption_lower = caption.lower()
    
    # 1. فحص قمع التحويل للأصل الرقمي (Lead Magnet Keywords)
    lead_keywords = ["دليل", "رابط", "خاص", "dm", "كومنت", "أرسل", "احصل", "free", "مجاني", "روتين", "daysline", "بايو", "bio"]
    has_funnel = any(k in caption_lower for k in lead_keywords)
    funnel_status = "نعم (تحويل للأصل الرقمي)" if has_funnel else "لا (بدون CTA)"
    
    # 2. ميزان 80/20 (الفيديوهات السريعة جذب 80%، الكاروسيل والنصوص الطويلة زاوية خاصة 20%)
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

def fetch_instagram_data():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0",
        "x-ig-app-id": "936619743392459",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.9,ar;q=0.8"
    }
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={USERNAME}"
    posts_list = []
    
    try:
        res = requests.get(url, headers=headers, timeout=15)
        if res.status_code == 200:
            data = res.json()
            user_data = data.get("data", {}).get("user", {})
            edges = user_data.get("edge_owner_to_timeline_media", {}).get("edges", [])
            for edge in edges:
                node = edge.get("node", {})
                caption_edges = node.get("edge_media_to_caption", {}).get("edges", [])
                caption = caption_edges[0].get("node", {}).get("text", "") if caption_edges else ""
                timestamp = node.get("taken_at_timestamp")
                date_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d") if timestamp else "غير محدد"
                is_video = node.get("is_video", False)
                likes = node.get("edge_liked_by", {}).get("count", 0)
                comments = node.get("edge_media_to_comment", {}).get("count", 0)
                
                post_type, cat, funnel, score = analyze_post(caption, is_video)
                
                posts_list.append({
                    "التاريخ": date_str,
                    "نوع المحتوى": post_type,
                    "التصنيف": cat,
                    "النص": caption[:60] + "..." if len(caption) > 60 else caption,
                    "تحويل للأصل": funnel,
                    "التقييم النوعي": score,
                    "تفاعل (إعجاب/تعليق)": f"❤️ {likes} | 💬 {comments}"
                })
    except Exception as e:
        print("Notice:", e)
        
    return posts_list

if __name__ == "__main__":
    posts = fetch_instagram_data()
    if posts:
        with open("posts.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False, indent=2)
        print(f"تم تحديث {len(posts)} منشور بنجاح.")
