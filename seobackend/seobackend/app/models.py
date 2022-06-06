
from django.db import models


class UserProfile(models.Model):
    user_id=models.CharField(max_length=200)
    active=models.BooleanField()
    uninstall=models.BooleanField()

    def __str__(self):
        return  self.user_id


class SearchURLKeyword(models.Model):
    url=models.CharField(max_length=200)
    keyword=models.CharField(max_length=200)
    active=models.BooleanField(max_length=200) 
    def __str__(self):
        return  self.url


class UserAssignKeyword(models.Model):
    uid=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    key=models.ForeignKey(SearchURLKeyword,on_delete=models.CASCADE)
    active=models.BooleanField()
    def __str__(self):
        return self.uid

class SearchKeywordLog(models.Model):
    user_id=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    keyword_id=models.ForeignKey(SearchURLKeyword,on_delete=models.CASCADE)
    search_date=models.DateTimeField()  
    def __str__(self):
        return self.user_id



















    


