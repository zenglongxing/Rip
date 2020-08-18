from django.db import models


# Create your models here.

class Star(models.Model):
    id = models.CharField(max_length=60, verbose_name="id", primary_key=True)
    actor_name = models.CharField(max_length=100, verbose_name="女优名称")
    count = models.IntegerField(verbose_name="影片数")
    new_movie_name = models.CharField(verbose_name="最新影片名称", max_length=100)
    online_photo = models.CharField(verbose_name="头像图片地址", max_length=256)
    sort = models.IntegerField(verbose_name="排名")

    def __str__(self):
        return self.id,

    class Meta:
        verbose_name = '女优信息表'
        verbose_name_plural = '女优信息表'
        db_table = 'star'


class Movie(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=256, verbose_name="影片名称")
    describe = models.TextField(verbose_name="描述", null=True)
    director = models.CharField(max_length=100, null=True, verbose_name='导演')
    can_load = models.BooleanField(verbose_name="是否可下载")
    can_online = models.BooleanField(verbose_name="是否可以在线观看")
    czn = models.BooleanField()
    fan_num = models.CharField(max_length=50, verbose_name="番号")
    labels = models.CharField(max_length=256, verbose_name="标签")
    movie_type = models.IntegerField(verbose_name="电影类型")
    new_cloud_time = models.DateTimeField(verbose_name="新上线时间")
    photo = models.CharField(max_length=256, verbose_name="封面图片")
    push_time = models.DateTimeField(verbose_name="上传时间")
    score = models.FloatField(verbose_name="评分")
    img_count = models.IntegerField(verbose_name='图片数量', default=10)
    star = models.ManyToManyField(Star)

    class Meta:
        verbose_name = '影片信息表'
        verbose_name_plural = '影片信息表'
        db_table = 'movie'


class Photo(models.Model):
    id = models.CharField(max_length=50, primary_key=True, auto_created=True)
    video = models.ForeignKey(to=Movie, on_delete=models.CASCADE, verbose_name='电影', related_name='video')
    path = models.TextField(verbose_name='图片路径')

    class Meta:
        verbose_name = '电影图片'
        verbose_name_plural = '电影图片'
        db_table = 'photo'


class Source(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    content = models.TextField(verbose_name='资源内容', null=True)
    fan_num = models.CharField(max_length=50, verbose_name='番号', null=True)
    text = models.TextField(verbose_name='描述')
    local_path = models.CharField(verbose_name='图片路径', null=True, max_length=255)

    class Meta:
        verbose_name = '资源'
        verbose_name_plural = '资源'
        db_table = 'source'
