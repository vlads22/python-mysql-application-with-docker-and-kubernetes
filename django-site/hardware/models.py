import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# models file are essentially a history that Django can roll through to update your database schema to match your current models.
# each class is a table
# the name of the table will be <app name>_<class name>


class Type(models.Model):
    name = models.CharField(
        max_length=45, db_comment='Name of the hardware type, like laptop, monitor, etc.')
    month_available = models.CharField(max_length=45, blank=True, null=True,
                                       db_comment='The date at which the item in the name column will be available')

    class Meta:
        managed = False
        db_table = 'type'
        # ??

    def get_all_types_raw():
        query = "SELECT * from type"
        result_list = []
        result = Type.objects.raw(query)
        for object in result:
            result_list.append(object.name) # name being the column name defined above
        print(result_list)  
        return result_list

    # def get_all_types():
    #     result = Type.objects.all()
    #     for p in result:
    #         print(p)
    #     print("hello 2")
    #     return result


# calling the function here we get the result also when running python manage.py runserver, don't run this file directly
list = Type.get_all_types_raw()

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField("date published")
#     # for convenience when dealiing with django shell

#     def __str__(self):
#         return self.question_text

#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text
