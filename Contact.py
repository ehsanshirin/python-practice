# تعریف دیکشنری با یک مقدار مشخص برای ذخیره اطلاعات مخاطب‌ها
phone_book = {
  "sara": "09011111111"
}

# منوی اصلی برنامه
menu_text = """
--- دفترچه تلفن ---
1- افزودن مخاطب
2- افزودن شماره به مخاطب
3- جستجوی شماره تلفن با اسم
4- حذف مخاطب
5- تعداد مخاطبین
6- خروج
"""

# حلقه بی‌نهایت برای اجرای برنامه
while True:
  
  # دریافت ورودی از کاربر
  user_choice = input(menu_text)


  # بررسی دستور خروج از برنامه
  if user_choice == "6" or user_choice == "":
    print("خداحافظ")
    break

  # پیاده‌ سازی گزینه افزودن مخاطب
  if user_choice == "1":
    name = input("اسم مخاطب رو وارد کن")
    if name in phone_book:
      result_message = "مخاطبی با این نام از قبل وجود داره"
    else:
      number = input("شماره تلفن رو وارد کن")
      phone_book[name] = [number]
      result_message = "مخاطب با موفقیت اضافه شد"
 
 # پیاده سازی گزینه افزودن شماره به مخاطب 
  elif user_choice == "2":
    name = input("اسم مخاطب رو وارد کن")
    if name not in phone_book:
      result_message = "مخاطبی با این نام پیدا نشد"
    else:
      number = input("شماره جدید رو وارد کن")
      phone_book[name].append(number)
      result_message = "شماره جدید اضافه شد"

  # پیاده سازی گزینه جستجوی شماره تلفن با اسم
  elif user_choice == "3":
    name = input("اسم مخاطب رو وارد کن")
    if name in phone_book:
      result_message = str(phone_book[name])
    else:
      result_message = "مخاطبی با این نام پیدا نشد"

  # پیاده سازی گزینه حذف مخاطب
  elif user_choice == "4":
    name = input("اسم مخاطب رو وارد کن")
    if name in phone_book:
      del phone_book[name]
      result_message = "مخاطب حذف شد"
    else:
      result_message = "مخاطبی با این نام پیدا نشد"

  # پیاده سازی گزینه نمایش تعداد مخاطب‌ها
  elif user_choice == "5":
     result_message = "تعداد مخاطب‌ها: " + str(len(phone_book))

  # مدیریت کردن ورودی نا معتبر
  else:
    result_message = "ورودی باید مقداری بین 1 تا 6 باشه"

  # اضافه کردن پرسش به رشته نتیجه و جداسازی دو پیام با علامت خط تیره
  result_message += " - آیا می‌خوای ادامه بدی؟ (بله/خیر)"
  
  # نمایش نتیجه و پرسش برای تمایل به ادامه دادن
  cont = input(result_message)
  if cont == "خیر" or cont == "":
    print("خداحافظ")
    break  
