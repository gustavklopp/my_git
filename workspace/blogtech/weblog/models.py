from django.db import models

class Tags(models.Model):
    tagname = models.CharField(max_length=20)

    def __str__(self):
        return self.tagname

    class Meta:
        ordering = ('tagname',)


class Post(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=500)
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.title

    def get_tag_list(self):
        return re.split(",", self.tags)

    class Meta:
        ordering = ('-date_created',)


