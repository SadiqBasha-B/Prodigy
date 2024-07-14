# Program Used To Check The Strength Of the Given Password And give The Feedback.
import Password_checker as pc
password = input("Enter your password: ")
result = pc.check_password_complexity(password)
print(result)