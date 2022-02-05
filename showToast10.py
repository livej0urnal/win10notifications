# pip install win10toast use
import win10toast

toast = win10toast.ToastNotifier()
toast.show_toast(title='Wake up,Neo....', msg='The Matrix has you...', duration=10)
