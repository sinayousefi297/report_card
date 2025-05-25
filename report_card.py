import tkinter as tk
from tkinter import messagebox

class ReportCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("کارنامه دانشجویی ساده")

        self.student_info = {}
        self.courses = []

        # مشخصات دانشجو
        tk.Label(root, text="نام و نام خانوادگی:").grid(row=0, column=0, sticky='e')
        tk.Label(root, text="کد دانشجویی:").grid(row=1, column=0, sticky='e')
        tk.Label(root, text="رشته:").grid(row=2, column=0, sticky='e')
        tk.Label(root, text="دانشگاه:").grid(row=3, column=0, sticky='e')

        self.name_entry = tk.Entry(root)
        self.code_entry = tk.Entry(root)
        self.major_entry = tk.Entry(root)
        self.university_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1)
        self.code_entry.grid(row=1, column=1)
        self.major_entry.grid(row=2, column=1)
        self.university_entry.grid(row=3, column=1)

        # اطلاعات درس
        tk.Label(root, text="نام درس:").grid(row=5, column=0, sticky='e')
        tk.Label(root, text="تعداد واحد:").grid(row=6, column=0, sticky='e')
        tk.Label(root, text="نمره:").grid(row=7, column=0, sticky='e')

        self.lesson_entry = tk.Entry(root)
        self.unit_entry = tk.Entry(root)
        self.grade_entry = tk.Entry(root)

        self.lesson_entry.grid(row=5, column=1)
        self.unit_entry.grid(row=6, column=1)
        self.grade_entry.grid(row=7, column=1)

        tk.Button(root, text="➕ افزودن درس", command=self.add_course).grid(row=8, column=1, sticky='we')
        tk.Button(root, text="📊 نمایش کارنامه", command=self.show_report).grid(row=9, column=1, sticky='we')
        tk.Button(root, text="🖨️ چاپ کارنامه", command=self.print_report).grid(row=10, column=1, sticky='we')

    def add_course(self):
        try:
            name = self.lesson_entry.get()
            unit = float(self.unit_entry.get())
            grade = float(self.grade_entry.get())
            self.courses.append((name, unit, grade))
            messagebox.showinfo("موفقیت", f"درس '{name}' اضافه شد.")
            self.lesson_entry.delete(0, tk.END)
            self.unit_entry.delete(0, tk.END)
            self.grade_entry.delete(0, tk.END)
        except:
            messagebox.showerror("خطا", "اطلاعات درس معتبر نیست.")

    def get_report_text(self):
        self.student_info["name"] = self.name_entry.get()
        self.student_info["code"] = self.code_entry.get()
        self.student_info["major"] = self.major_entry.get()
        self.student_info["university"] = self.university_entry.get()

        total_units = sum(course[1] for course in self.courses)
        weighted_sum = sum(course[1] * course[2] for course in self.courses)
        average = weighted_sum / total_units if total_units > 0 else 0

        report = f"""\
📄 کارنامه دانشجویی

👤 نام: {self.student_info['name']}
🎓 کد دانشجویی: {self.student_info['code']}
📘 رشته: {self.student_info['major']}
🏛️ دانشگاه: {self.student_info['university']}

📚 دروس:
"""
        for course in self.courses:
            report += f"  - {course[0]} | واحد: {course[1]} | نمره: {course[2]}\n"

        report += f"\n📈 معدل کل: {average:.2f}"
        return report

    def show_report(self):
        try:
            report = self.get_report_text()
            messagebox.showinfo("کارنامه", report)
        except Exception as e:
            messagebox.showerror("خطا", f"اشکال در نمایش کارنامه: {e}")

    def print_report(self):
        try:
            report = self.get_report_text()
            with open("report_card.txt", "w", encoding="utf-8") as f:
                f.write(report)
            messagebox.showinfo("چاپ شد", "کارنامه در فایل 'report_card.txt' ذخیره شد.\nبرای چاپ آن را باز کنید.")
        except Exception as e:
            messagebox.showerror("خطا", f"اشکال در چاپ: {e}")

# اجرای برنامه
if __name__ == "__main__":
    root = tk.Tk()
    app = ReportCardApp(root)
    root.mainloop()
