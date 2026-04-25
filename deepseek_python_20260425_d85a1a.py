"""
برنامج تقدير الطالب
يقوم بقراءة درجة الطالب ويعطيه التقدير المناسب (ضعيف، جيد، جيد جدًا، ممتاز)
يستمر البرنامج حتى يدخل المستخدم كلمة "خروج"
"""

def get_grade_estimation(score):
    """
    دالة لتحديد التقدير بناءً على الدرجة
    """
    if score < 50:
        return "ضعيف"
    elif score < 65:
        return "جيد"
    elif score < 80:
        return "جيد جدًا"
    else:
        return "ممتاز"

def main():
    print("=" * 40)
    print("برنامج تقدير الطالب")
    print("=" * 40)
    
    continue_loop = True
    
    while continue_loop:
        # طلب الإدخال من المستخدم
        user_input = input("\nأدخل درجة الطالب (0-100) أو اكتب 'خروج' لإنهاء البرنامج: ")
        
        # شرط الخروج
        if user_input.strip().lower() == "خروج":
            continue_loop = False
            print("تم إنهاء البرنامج. شكرًا لاستخدامك البرنامج.")
            continue
        
        # محاولة تحويل الإدخال إلى رقم
        try:
            degree = float(user_input)
        except ValueError:
            print("[خطأ] القيمة التي أدخلتها ليست رقمًا صالحًا ولا كلمة 'خروج'. يرجى إدخال رقم بين 0 و100.")
            continue
        
        # التحقق من صحة المدى
        if degree < 0 or degree > 100:
            print(f"[خطأ] الدرجة {degree} خارج النطاق المسموح (0-100). يرجى إدخال درجة صحيحة.")
            continue
        
        # حساب التقدير وعرضه
        estimation = get_grade_estimation(degree)
        print(f"تقدير الطالب: {estimation}")

if __name__ == "__main__":
    main()