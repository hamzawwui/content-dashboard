import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
        color: #9E9E9E;
    }
    .highlight-card {
        background: linear-gradient(135deg, #1f1f1a 0%, #16181a 100%);
        border-left: 4px solid #FFD700;
        padding: 15px;
        border-radius: 6px;
        margin-bottom: 12px;
    }
    div[data-testid="stMetricValue"] {
        color: #FFD700 !important;
    }
</style>
""", unsafe_allow_html=True)

# الرأس العام للمنصة
st.title("⚡ مركز قيادة المحتوى والبيزنس المستقل")
st.caption("نظام التقييم النوعي والتشغيلي المباشر لصانع المحتوى | hamzawwui")

# ================================
# الشريط العلوي: الهدف النهائي (The Ultimate North Star)
# ================================
top_c1, top_c2, top_c3 = st.columns(3)

with top_c1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-sub">الهدف الجماهيري النهائي</div>
        <div class="metric-num">1,000,000</div>
        <div class="metric-sub">متابع نوعي حقيقي</div>
    </div>
    """, unsafe_allow_html=True)

with top_c2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-sub">الدخل الصافي المستهدف</div>
        <div class="metric-num">10,025 $ / شهر</div>
        <div class="metric-sub">5,000$ رعايات + 5,025$ منتج رقمي</div>
    </div>
    """, unsafe_allow_html=True)

with top_c3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-sub">الهدف الواقعي والتشغيلي</div>
        <div class="metric-num">استقلال تام</div>
        <div class="metric-sub">الاستقالة وإدارة البيزنس كشركة خاصة</div>
    </div>
    """, unsafe_allow_html=True)

# أجنحة المنصة
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 هرم المراحل الاستراتيجية",
    "📊 تقييم المحتوى وقمع التحويل (80/20)",
    "🤝 محرك الرعايات والتعاقدات (Retainers)",
    "⚙️ دورة التشغيل الأسبوعية (Batching)"
])

# ================================
# الجناح 1: هرم المراحل (Milestones)
# ================================
with tab1:
    st.subheader("🪜 هرم الأهداف المرحلية والقرارات التشغيلية")
    
    m_col1, m_col2 = st.columns([1, 1])
    
    with m_col1:
        st.markdown("""
        <div class="highlight-card" style="border-color: #FFD700;">
            <h4 style="color: #FFD700; margin: 0;">المرحلة 1: تثبيت الأساس وكسر حاجز 50k (الحالية)</h4>
            <p style="margin: 5px 0;"><b>الجمهور:</b> الوصول من 36k إلى 50,000 متابع.</p>
            <p style="margin: 5px 0;"><b>المنتج المجاني:</b> إطلاق دليل الروتين الصباحي (Lead Magnet).</p>
            <p style="margin: 5px 0;"><b>قاعدة البيانات:</b> جمع أول 1,000 - 2,000 مهتم في القائمة.</p>
            <p style="margin: 5px 0; color: #888;"><b>الدخل المستهدف:</b> 0$ (التركيز على بناء الثقة العميقة).</p>
        </div>
        
        <div class="highlight-card" style="border-color: #555;">
            <h4 style="color: #DDD; margin: 0;">المرحلة 2: محرك الدخل الأول (50k ➔ 150k)</h4>
            <p style="margin: 5px 0;"><b>المنتج:</b> إطلاق أول أصل رقمي مدفوع منخفض التكلفة (30$ - 50$).</p>
            <p style="margin: 5px 0;"><b>التدفق المالي:</b> تحقيق 1,500$ إلى 3,000$ شهرياً.</p>
            <p style="margin: 5px 0; color: #FFD700;"><b>القرار التشغيلي:</b> التخلي عن إحدى الوظيفتين وتقليص ساعات العمل الخارجي.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with m_col2:
        st.markdown("""
        <div class="highlight-card" style="border-color: #555;">
            <h4 style="color: #DDD; margin: 0;">المرحلة 3: الرعايات الكبرى والاستقلال (150k ➔ 500k)</h4>
            <p style="margin: 5px 0;"><b>التعاقدات:</b> توقيع أول عقود رعاية طويلة المدى (Sponsorship Retainers).</p>
            <p style="margin: 5px 0;"><b>التدفق المالي:</b> كسر حاجز 10,000$ شهرياً صافية ومستدامة.</p>
            <p style="margin: 5px 0; color: #FFD700;"><b>القرار التشغيلي:</b> الاستقالة الكاملة والتفرغ التام لإدارة المحتوى كشركة.</p>
        </div>
        
        <div class="highlight-card" style="border-color: #555;">
            <h4 style="color: #DDD; margin: 0;">المرحلة 4: نادي المليون والريادة (500k ➔ 1,000,000)</h4>
            <p style="margin: 5px 0;"><b>التموضع:</b> المرجع الأول في الانضباط وتطوير الأداء عربياً.</p>
            <p style="margin: 5px 0;"><b>التوسع:</b> تنويع المنتجات وبناء فريق عمل مساعد (مونتاج، إدارة).</p>
        </div>
        """, unsafe_allow_html=True)

# ================================
# الجناح 2: تقييم المحتوى ومعادلة 80/20
# ================================
with tab2:
    st.subheader("⚖️ ميزان المحتوى: استراتيجية 80 / 20")
    
    col_chart, col_funnel = st.columns([1, 2])
    
    # بيانات محاكاة المنشورات وقمع التحويل
    posts_data = [
        {"التاريخ": "2026-09-28", "نوع المحتوى": "ريلز سريع", "التصنيف": "80% جذب سريع", "الهدف": "عادات صباحية", "تحويل للأصل": "نعم (Daysline)", "حفظ/مشاركة": "مرتفع", "التقييم النوعي": "🌟 يخدم القمع والانتشار"},
        {"التاريخ": "2026-09-25", "نوع المحتوى": "كاروسيل عميق", "التصنيف": "20% زاوية خاصة", "الهدف": "تغيير مفهوم الانضباط", "تحويل للأصل": "نعم (دليل الروتين)", "حفظ/مشاركة": "مرتفع جداً", "التقييم النوعي": "🌟 بناء هيبة وتحويل"},
        {"التاريخ": "2026-09-22", "نوع المحتوى": "ريلز سريع", "التصنيف": "80% جذب سريع", "الهدف": "تنظيم بيئة العمل", "تحويل للأصل": "لا", "حفظ/مشاركة": "متوسط", "التقييم النوعي": "⚠️ جذب بدون Call to Action"},
        {"التاريخ": "2026-09-19", "نوع المحتوى": "ريلز سريع", "التصنيف": "80% جذب سريع", "الهدف": "قاعدة الـ 5 دقائق", "تحويل للأصل": "نعم (دليل الروتين)", "حفظ/مشاركة": "مرتفع", "التقييم النوعي": "🌟 يخدم القمع والانتشار"},
        {"التاريخ": "2026-09-15", "نوع المحتوى": "كاروسيل عميق", "التصنيف": "20% زاوية خاصة", "الهدف": "تحليل كتاب Made to Stick", "تحويل للأصل": "نعم (رابط الملف)", "حفظ/مشاركة": "مرتفع جداً", "التقييم النوعي": "🌟 مرجع للمهتمين والرعايات"}
    ]
    df_posts = pd.DataFrame(posts_data)
    
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
# الجناح 3: محرك الرعايات والتعاقدات (Retainers)
# ================================
with tab3:
    st.subheader("🤝 هندسة معادلة الرعايات والتعاقدات المستمرة (Retainers)")
    
    r_col1, r_col2 = st.columns(2)
    
    with r_col1:
        st.markdown("""
        <div class="highlight-card">
            <h4 style="color: #FFD700;">💼 ركيزة الرعايات الشهرية (5,000$ شهرياً)</h4>
            <p>• <b>النموذج:</b> عقدان شهريان مستمران (Retainers) مع تطبيقات ومنصات موثوقة.</p>
            <p>• <b>الحسبة:</b> 2 × 2,500$ = <b>5,000$ شهرياً</b> تدفق ثابت.</p>
            <p>• <b>القطاعات المستهدفة:</b> تطبيقات الإنتاجية، أدوات الذكاء الاصطناعي، أجهزة بيئة العمل، المكملات ومنصات الرياضة الموثوقة.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 📋 بنود حماية العقد الإلزامية:")
        st.checkbox("نطاق العمل المحدد (عدد الفيديوهات، الثواني، مواعيد التسليم)", value=True)
        st.checkbox("شرط التعديلات: تعديل إلى 2 بحد أقصى بالنص المتفق عليه مسبقاً", value=True)
        st.checkbox("حقوق الاستخدام: النشر بحسابي فقط (استخدامه كـ Dark Ad يضيف 30% إلى 50%)", value=True)
        st.checkbox("شروط الدفع: 50% مقدمة غير مستردة قبل التصوير، و 50% قبل النشر للعامة", value=True)
        
    with r_col2:
        st.markdown("""
        <div class="highlight-card">
            <h4 style="color: #FFD700;">📦 ركيزة الأصل الرقمي (5,025$ شهرياً)</h4>
            <p>• <b>المنتج:</b> أداة تطبيقية أو كورس تدريبي عملي بسعر <b>67$</b>.</p>
            <p>• <b>المعدل المطلوب:</b> بيع 75 نسخة شهرياً فقط (بمعدل 2.5 مبيعة يومياً من بين آلاف المشاهدين).</p>
            <p>• <b>الحسبة:</b> 75 × 67$ = <b>5,025$ شهرياً</b> صافية من الأصول الرقمية.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("### 🎯 حاسبة تسعير الريلز المنفرد:")
        reach_est = st.slider("متوسط مشاهدات الريلز في حسابك:", 10000, 150000, 45000, step=5000)
        suggested_rate = int((reach_est / 1000) * 10)
        suggested_rate = max(250, min(suggested_rate, 800))
        st.metric(label="السعر الاسترشادي المقترح للريلز الواحد:", value=f"{suggested_rate} $", help="قاعدة الحسابات النشطة (30k-50k) تتراوح بين 250$ إلى 600$+")

# ================================
# الجناح 4: دورة التشغيل الأسبوعية (Batching)
# ================================
with tab4:
    st.subheader("⚙️ نظام العمل الأسبوعي (Content Batching)")
    st.markdown("""
    > **معيار اليوم الناجح:** مقياس إنجازك لا يقاس بالمشاهدات؛ مقياسك الوحيد هو إنهاء مرحلة اليوم المحددة وإغلاق الملف فوراً دون تأنيب ضمير.
    """)
    
    b_col1, b_col2, b_col3, b_col4, b_col5 = st.columns(5)
    with b_col1:
        st.checkbox("📝 يوم الكتابة\n(3-5 سكريبتات دفعة واحدة)")
    with b_col2:
        st.checkbox("🎨 يوم التصميم\n(كاروسيل أسود وأصفر بالدرايف)")
    with b_col3:
        st.checkbox("🎥 يوم التصوير\n(تسجيل المقاطع بجلسة واحدة)")
    with b_col4:
        st.checkbox("✂️ يوم المونتاج\n(إخراج نهائي وجدولة)")
    with b_col5:
        st.checkbox("🚀 يوم النشر والردود\n(20 دقيقة تفاعل وتوجيه للدليل)")

    st.divider()
    st.subheader("🔍 دائرة التقييم الذكي (جلسة الـ 30 دقيقة الأسبوعية)")
    q1, q2 = st.columns(2)
    with q1:
        st.text_area("أفضل Hook وزاوية حققت تفاعلاً هذا الأسبوع لتكرارها:", placeholder="مثال: خطاف المقارنة الصادمة في بوست العادات الصباحية...")
        st.text_area("عمق رسائل الخاص (DM Depth): هل بدأت تأتي أسئلة لعملاء جاهزين؟", placeholder="مثال: استفسارات عن كيفية تطبيق الدليل وعن الأدوات المستخدمة...")
    with q2:
        st.text_area("مؤشر الجودة والانطباع التجاري: هل البروفايل يعكس شخصاً تبحث عنه البراندات؟", placeholder="تدقيق ألوان البوستات، نظافة النصوص، والوضوح...")
        st.button("💾 حفظ تقرير التقييم الأسبوعي", use_container_width=True)
