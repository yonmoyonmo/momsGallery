from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


def user_path(instance, filename):  # 파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)  # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1]  # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    # 예 : wayhome/abcdefgs.png
    return '%s/%s.%s' % (instance.author.username, pid, extension)


class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to=user_path, blank=True, null=True)  # 어디로 업로드 할지 지정
    # 로그인 한 사용자, many to one relation
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(timezone.now(), null=True)
    # 레코드 생성시 현재 시간으로 자동 생성

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        'gallery.Photo', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
