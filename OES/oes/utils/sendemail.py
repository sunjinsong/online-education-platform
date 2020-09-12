from django.conf import settings
from django.core.mail import send_mail
from random import randrange
def SendRegisterInfo(user):
    subject = '在线教育注册激活按钮'
    message = "请点击下面的连接来激活你的账户，<a href='"+settings.EMAIL_URL+'active_acount/'+str(user.id)+"'>%s</a>"%(settings.EMAIL_URL+'active_acount/'+str(user.id))
    send_mail(
        subject,
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        html_message=message,
    )


def SendResetPwdInfo(user):

    subject = '在线教育密码修改'
    message = "，<a href='" + settings.EMAIL_URL + str(user.id) + "'>%s</a>" % (
                settings.EMAIL_URL + str(user.id))
    print(subject, message, settings.EMAIL_HOST_USER, user.email)
    send_mail(
        subject,
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        html_message=message,
    )