# ==========================================
# Security Log Analyzer
# مشروع تحليل السجلات الأمنية
# ==========================================

import re

# ------------------------------------------
# قراءة ملف السجلات
# ------------------------------------------

with open("log.txt", "r") as file:
    logs = file.readlines()

# ------------------------------------------
# متغيرات التخزين
# ------------------------------------------

failed_attempts = 0
ip_addresses = []
usernames = []
sql_attacks = 0

# ------------------------------------------
# تحليل السجلات
# ------------------------------------------

for line in logs:

    # ------------------------------------------
    # استخراج البيانات من السجلات
    # ------------------------------------------

    # استخراج عناوين IP باستخدام findall
    # تم استخدام تعبير منتظم قوي للتحقق من صحة الـ IP
    ips = re.findall(r"\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\b", line) # تم استخدام تعبير قوي 

    if ips:
        ip_addresses.extend(ips)

    # التحقق أن السجل يبدأ بتاريخ صحيح باستخدام match
    if re.match(r"\d{4}-\d{2}-\d{2}", line):

        print("سجل صالح:", line.strip())

    # استخراج أسماء المستخدمين باستخدام search
    user = re.search(r"user:(\w+)", line)

    if user:
        usernames.append(user.group(1))

    # التحقق من محاولات الدخول الفاشلة باستخدام match
    if re.search(r"FAILED LOGIN", line):
        failed_attempts += 1

    # كشف هجمات SQL Injection
    if re.search(r"SQL Injection", line):
        sql_attacks += 1

# ------------------------------------------
# إخفاء جزء من الـ IP باستخدام sub
# ------------------------------------------

hidden_ips = []

for ip in ip_addresses:
    hidden_ip = re.sub(r"\.\d+$", ".XXX", ip)
    hidden_ips.append(hidden_ip)

# ------------------------------------------
# طباعة النتائج
# ------------------------------------------

print("=" * 40)
print("Security Log Analysis Results")
print("=" * 40)

print("Number of failed login attempts:", failed_attempts)

print("\nDetected IP addresses:")
for ip in hidden_ips:
    print(ip)

print("\nuser names:")
for user in usernames:
    print(user)

print("\n Number of attacks SQL Injection:", sql_attacks)

print("=" * 40)