import datetime
from haystack import indexes
from .models import Course

class CourseIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    # 对那张表进行查询
    def get_model(self):  # 重载get_model方法，必须要有！
        # 返回这个model
        return Course

    # 针对哪些数据进行查询
    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        # return self.get_model().objects.filter(updated__lte=datetime.datetime.now())
        return self.get_model().objects.all()