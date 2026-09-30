import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import os
from datetime import datetime

# إعداد الصفحة وهوية البراند (أسود وأصفر)
st.set_page_config(
    page_title="Hamzawwui OS | مركز قيادة صناعة المحتوى",
    layout="wide",
    page_icon="⚡"
)

# تخصيص التصميم بالكامل
st.markdown("""
<style>
    .stApp {
        background-color: #0c0d0e;
        color: #F5F5F5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .metric-box {
        background-color: #16181a;
        border: 1px solid #FFD700;
        border-radius: 10px;
        padding: 16px;
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-num {
        font-size: 1.8rem;
        font-weight: 800;
        color: #FFD700;
        margin: 5px 0;
    }
    .metric-sub {
        font-size: 0.85rem;
        color: #A0A0A0;
    }
    .phase-card {
        background-color: #16181a;
        border-radius: 10px;
        padding: 18px;
        margin-bottom: 15px;
        border: 1px solid #282a2d;
    }
    .phase-card.active {
        border: 1.5px solid #FFD700;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.15);
    }
    .badge {
        display: inline-block;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: bold;
    }
    .badge-gold { background: rgba(255, 215, 0, 0.15); color: #FFD700; }
    .badge-gray { background: rgba(255, 255, 255, 0.08); color: #B0B0B0; }
</style>
""", unsafe_allow_html=True)

# رأس الصفحة والرسالة التموضع
st.markdown("<h1 style='text-align: right; color: white;'>⚡ مركز قيادة المحتوى والبيزنس المستقل</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: right; color: #888;'>hamzawwui | نظام التقييم النوعي والتشغيلي المباشر لصانع المحتوى</p>", unsafe_allow_html=True)

# المقاييس العلوية الثلاثة
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-sub">الهدف الجماهيري النهائي</div>
        <div class="metric-num">1,000,000</div>
        <div class="metric-sub">متابع نوعي حقيقي</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-sub">الدخل الصافي المستهدف</div>
        <div class="metric-num">10,025 $ / شهر</div>
        <div class="metric-sub">رعايات + 5,025$ منتج رقمي 5,000$</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-sub">الهدف الواقعي والتشغيلي</div>
        <div class="metric-num">استقلال تام</div>
        <div class="metric-sub">الاستقالة وإدارة البيزنس كشركة خاصة</div>
    </div>
    """, unsafe_allow_html=True)

# أجنحة المنظومة
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 هرم المراحل الاستراتيجية",
    "📊 تقييم المحتوى وقمع التحويل (80/20)",
    "🤝 محرك الرعايات والتعاقدات (Retainers)",
    "⚙️ دورة التشغيل الأسبوعية (Batching)"
])

# ================================
# الجناح 1: هرم المراحل
# ================================
with tab1:
    st.subheader("🪜 هرم الأهداف المرحلية والقرارات التشغيلية")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="phase-card active">
            <h4 style="color: #FFD700; margin-top:0;">المرحلة 1: تثبيت الأساس وكسر حاجز 50k (الحالية)</h4>
            <p><b>الجمهور:</b> الوصول من 36k إلى 50,000 متابع نوعي.</p>
            <p><b>المنتج المجاني (Lead Magnet):</b> إطلاق دليل الروتين الصباحي.</p>
            <p><b>قاعدة البيانات:</b> جمع أول 1,000 - 2,000 مهتم في القائمة.</p>
            <p><b>الدخل المستهدف:</b> 0$ (التركيز على بناء الثقة العميقة).</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="phase-card">
            <h4 style="color: #FFF; margin-top:0;">المرحلة 2: محرك الدخل الأول (50k ➔ 150k)</h4>
            <p><b>المنتج:</b> إطلاق أول أصل رقمي مدفوع منخفض التكلفة (30$ - 50$).</p>
            <p><b>التدفق المالي:</b> تحقيق 1,500$ إلى 3,000$ شهرياً.</p>
            <p><b>القرار التشغيلي:</b> التخلي عن إحدى الوظيفتين وتقليص ساعات العمل الخارجي.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="phase-card">
            <h4 style="color: #FFF; margin-top:0;">المرحلة 3: الرعايات الكبرى والاستقلال (150k ➔ 500k)</h4>
            <p><b>التعاقدات:</b> توقيع أول عقود رعاية طويلة المدى (Sponsorship Retainers).</p>
            <p><b>التدفق المالي:</b> كسر حاجز 10,000$ شهرياً صافية ومستدامة.</p>
            <p><b>القرار التشغيلي:</b> الاستقالة الكاملة والتفرغ التام لإدارة المحتوى كشركة.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="phase-card">
            <h4 style="color: #FFF; margin-top:0;">المرحلة 4: نادي المليون والريادة (500k ➔ 1,000,000)</h4>
            <p><b>التموضع:</b> المرجع الأول في الانضباط وتطوير الأداء عربياً.</p>
            <p><b>التوسع:</b> تنويع المنتجات وبناء فريق عمل مساعد (مونتاج، إدارة).</p>
        </div>
        """, unsafe_allow_html=True)

# ================================
# الجناح 2: تقييم المحتوى ومعادلة 80/20
# ================================
with tab2:
    st.subheader("⚖️ ميزان المحتوى: استراتيجية 80 / 20")
    
    # تحميل أو تهيئة البيانات
    DATA_FILE = "posts.json"
    if "posts_data" not in st.session_state:
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    st.session_state.posts_data = json.load(f)
            except Exception:
                st.session_state.posts_data = []
        else:
            st.session_state.posts_data = [
                {"التاريخ": "2026-09-28", "نوع المحتوى": "ريلز / فيديو سريع", "التصنيف": "80% جذب سريع", "النص": "3 عادات صباحية تصنع فارقاً حقيقياً في تركيزك وطاقتك اليومية...", "تحويل للأصل": "نعم (تحويل للأصل الرقمي)", "التقييم النوعي": "🌟 ممتاز: جذب سريع متصل بالقمع", "تفاعل": "عالي"},
                {"التاريخ": "2026-09-25", "نوع المحتوى": "كاروسيل / منشور عميق", "التصنيف": "20% زاوية خاصة", "النص": "لماذا يفشل أغلب الناس في الالتزام؟ تفكيك مفهوم الحافز مقابل الانضباط...", "تحويل للأصل": "نعم (تحويل للأصل الرقمي)", "التقييم النوعي": "🌟 استثنائي: بناء هيبة وتحويل مباشر", "تفاعل": "حفظ ومشاركات"}
            ]

    # أداة تحليل وإضافة منشور فوري
    with st.expander("⚡ تحليل وإدراج منشور جديد في المنظومة", expanded=False):
        with st.form("add_post_form", clear_on_submit=True):
            f_col1, f_col2 = st.columns([1, 1])
            with f_col1:
                post_date = st.date_input("تاريخ المنشور", datetime.now())
                media_type = st.selectbox("شكل المحتوى", ["ريلز / فيديو سريع", "كاروسيل / منشور عميق"])
            with f_col2:
                engagement_level = st.selectbox("المؤشر التفاعلي الأبرز", ["حفظ عالي (Saves)", "مشاركات واسعة (Shares)", "تعليقات ونقاش (Comments)", "مشاهدات جذب عام"])
            
            caption_input = st.text_area("نص الكابشن أو فكرة المنشور:", placeholder="الصق هنا الكابشن الذي نشرته أو تخطط لنشره...")
            submitted = st.form_submit_button("تحليل المحتوى وإضافته للداشبورد")
            
            if submitted and caption_input:
                caption_lower = caption_input.lower()
                lead_keywords = ["دليل", "رابط", "خاص", "dm", "كومنت", "أرسل", "احصل", "free", "مجاني", "روتين", "daysline", "بايو", "bio"]
                has_funnel = any(k in caption_lower for k in lead_keywords)
                funnel_status = "نعم (تحويل للأصل الرقمي)" if has_funnel else "لا (بدون CTA)"
                
                if "فيديو" in media_type and len(caption_input) <= 280:
                    cat = "80% جذب سريع"
                else:
                    cat = "20% زاوية خاصة"
                    
                if has_funnel and cat == "80% جذب سريع":
                    score = "🌟 ممتاز: جذب سريع متصل بالقمع"
                elif has_funnel and cat == "20% زاوية خاصة":
                    score = "🌟 استثنائي: بناء هيبة وتحويل مباشر"
                elif not has_funnel and cat == "80% جذب سريع":
                    score = "⚠️ جذب عام بدون توجيه واضح للقمع"
                else:
                    score = "📌 محتوى بناء وعي ونواة فكرية"
                    
                new_entry = {
                    "التاريخ": str(post_date),
                    "نوع المحتوى": media_type,
                    "التصنيف": cat,
                    "النص": caption_input[:60] + "..." if len(caption_input) > 60 else caption_input,
                    "تحويل للأصل": funnel_status,
                    "التقييم النوعي": score,
                    "تفاعل": engagement_level
                }
                st.session_state.posts_data.insert(0, new_entry)
                try:
                    with open(DATA_FILE, "w", encoding="utf-8") as f:
                        json.dump(st.session_state.posts_data, f, ensure_ascii=False, indent=2)
                except Exception:
                    pass
                st.success("تم تحليل المنشور بنجاح وإدراجه ضمن ميزان المحتوى!")

    df_posts = pd.DataFrame(st.session_state.posts_data)

    col_chart, col_funnel = st.columns([1, 2])
    with col_chart:
        fig = px.pie(
            df_posts, names="التصنيف", title="التوازن الحالي للمنشورات",
            hole=0.6,
            color="التصنيف",
            color_discrete_map={"80% جذب سريع": "#FFD700", "20% زاوية خاصة": "#2B2B2B"}
        )
        fig.update_layout(paper_bgcolor="#0c0d0e", font_color="#FFF", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        st.caption("الهدف: 4 بوستات جذب سريع مقابل بوست واحد فكرة عميقة وزاوية خاصة.")

    with col_funnel:
        st.write("### سجل منشورات الحساب والتقييم النوعي")
        st.dataframe(df_posts, use_container_width=True, hide_index=True)
        st.info("💡 **مؤشر القيمة الحقيقي:** ارتفاع نسبة الحفظ (Saves) والمشاركات (Shares) مقارنة باللايكات يعني أن المحتوى تحول لمرجع يُعتمد عليه وجاهز للشراكات.")

# ================================
# الجناح 3: محرك الرعايات
# ================================
with tab3:
    st.subheader("💼 هيكل الرعايات الاحترافي (Retainer Model)")
    r1, r2 = st.columns([1, 1])
    with r1:
        st.markdown("""
        <div class="phase-card">
            <h4 style="color: #FFD700; margin-top:0;">شروط قبول الرعاية (Brand Safety)</h4>
            <ul>
                <li>توافق قيمي 100% مع أسلوب حياة الانضباط والأداء العالي.</li>
                <li>تجربة المنتج/الخدمة شخصياً والتأكد من جودتها قبل توقيع العقد.</li>
                <li>الحفاظ على حرية صياغة السكربت بالأسلوب الصادق والمقنع للجمهور.</li>
                <li>رفض إعلانات المنصات المشبوهة أو وعود الثراء السريع قطعياً.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with r2:
        st.markdown("""
        <div class="phase-card">
            <h4 style="color: #FFD700; margin-top:0;">حاسبة عروض الرعاية طويلة المدى</h4>
            <p><b>نموذج الشراكة ربع السنوية (3 أشهر):</b></p>
            <ul>
                <li>2 فيديو ريلز نوعي مدمج شهرياً.</li>
                <li>4 ستوريات موجهة بروابط تتبع شهرية.</li>
                <li><b>القيمة المقترحة:</b> 2,500$ - 3,500$ شهرياً لكل علامة تجارية.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ================================
# الجناح 4: دورة التشغيل الأسبوعية
# ================================
with tab4:
    st.subheader("⚙️ نظام الإنتاج الدفعي الأسبوعي (Batching)")
    st.markdown("""
    <div class="phase-card">
        <h4 style="color: #FFD700; margin-top:0;">جدول الإنتاج لحماية الوقت والطاقة</h4>
        <p><b>يوم الأحد:</b> تفريغ الأفكار وكتابة 4 إلى 5 سكربتات متكاملة (جلسة تركيز 3 ساعات).</p>
        <p><b>يوم الاثنين:</b> جلسة تصوير مجمعة لكافة الفيديوهات بكامل الإضاءة والمعدات دفعة واحدة.</p>
        <p><b>يوم الثلاثاء والأربعاء:</b> مونتاج وتجهيز الكاروسيل والأصول البصرية.</p>
        <p><b>نهاية الأسبوع:</b> جلسة التقييم الأسبوعي (30 دقيقة): مراجعة تفاعل DMs، وتدفق المهتمين للروتين المجاني.</p>
    </div>
    """, unsafe_allow_html=True)
