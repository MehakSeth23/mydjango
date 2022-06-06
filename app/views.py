from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.utils.crypto import get_random_string
from datetime import datetime
from django.utils import timezone

def index(request):
    return HttpResponse('Welcome, glad you are here')

@csrf_exempt
def createUserProfile(request):
    if request.method == "POST":        
        try:
            userid = "seo_" + get_random_string(length=32)
            record = UserProfile()
            record.user_id = userid
            record.active = True
            record.uninstall = False
            record.save()
            return JsonResponse({'status':200,'message':"Record added.",'userid':userid})
        except:
            return JsonResponse({"status":500,"message":"Failure"})
    else:
        return JsonResponse({'status': 404,'message':"Not Found"})

@csrf_exempt
def updatedProfileLink(request):
    if request.method == "POST":       
        query = request.POST['userid']
        if query:
            record =  UserProfile.objects.get(userid__exact=query)
            print(record)
            record.active = False
            record.uninstall = True
            record.save()
            return JsonResponse({'status':200,'message':"Record updated."})
        else:
            return JsonResponse({"status":500,"message":"Failure"})
    else:
        return JsonResponse({'status': 404,'message':"Not Found"})

@csrf_exempt
def getKeywordList(request):
    if request.method == "GET":
       
        records = SearchURLKeyword.objects.filter(active=True)

        allUrls = []
        for items in records:
            data = {
                'keyword_id':items.id,
                'url':items.url,
                'keyword':items.keyword,
                'active':items.active
            }
            allUrls.append(data)
            
        return JsonResponse({'status':200,'message':"success",'data':allUrls})
    else:
        return JsonResponse({"status":500,"message":"Failure"})


@csrf_exempt
def SaveSearchKeywordLog(request):
    if request.method =="POST":
        userid = request.POST['user_id'].strip()
        keywordid = request.POST['keyword_id'].strip()
        search_date = request.POST["search_date"]
        try:
            userProfile =  UserProfile.objects.get(user_id= userid)
            searchURLKeyword = SearchURLKeyword.objects.get(pk = keywordid)            
            record = SearchKeywordLog()
            record.user_id = userProfile
            record.keyword_id = searchURLKeyword
            record.search_date = datetime.strptime(search_date, '%Y-%m-%d')
            record.save()
            return JsonResponse({'status':200,'message':"Successful"})
        except Exception as ex:          
            return JsonResponse({'status':500,'message':str(ex)})        
    else:
        return JsonResponse({'status': 404,'message':"Not Found"}) 

@csrf_exempt
def processKeywordbyDate(request):
    if request.method == "GET":
        user_id = request.GET['user_id']
        search_date = request.GET['search_date']
        try:
            search_date_value = datetime.strptime(search_date, '%Y-%m-%d')
            userProfile =  UserProfile.objects.get(user_id = user_id)
            # filter (fucn) which returns queryset array or list of queryset.
            searchedKeyword = SearchKeywordLog.objects.filter(user_id=userProfile.id,search_date__exact=search_date_value)
            usedKeywordList = []
            if len(searchedKeyword) > 0:
                for keyword in searchedKeyword:
                    usedKeywordList.append(keyword.keyword_id.id)
            print(usedKeywordList)
            allUrls = []
            records = SearchURLKeyword.objects.filter(active=True)
            for items in records:
                if items.id not in usedKeywordList:
                    data = {
                    'keyword_id':items.id,
                    'url':items.url,
                    'keyword':items.keyword,
                    'active':items.active
                    }
                    allUrls.append(data)

            return JsonResponse({'status':200,'message':"success",'data':allUrls})
        except Exception as ex:          
            return JsonResponse({'status':500,'message':str(ex)})        
    else:
        return JsonResponse({'status': 404,'message':"Not Found"}) 