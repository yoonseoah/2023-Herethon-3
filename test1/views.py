from django.shortcuts import render, redirect, get_object_or_404
from .models import *
#*  urls.py에서 요청 ->? test1/ 주소로 요청 -> views.py 함수 호출  

#* create 부분 (기본)
# def create(request):
#     if request.method == "POST":        #* POST 요청 시 
#         index = Index()
#         index.title = request.POST.get("title")
#         index.content = request.POST.get("content")
#         index.save()                                    #* index 객체 저장 후 index url으로 돌아감 
#         return redirect("index")
#     return render(request, "create.html")               #* get 요청 시 

#* create 별점 5항목 + 평균 
def create(request):
    if request.method == "POST":
        review = Review()
        review.star_avg = request.POST.get("star_avg")          #* 별점 평균 
        review.star_danger = request.POST.get("star_danger")    #* 치안 별점
        review.star_price = request.POST.get("star_price")      #* 물가 별점 
        review.star_traffic = request.POST.get("star_traffic")  #* 교통 편의성 별점 
        review.star_leisure = request.POST.get("star_leisure")  #* 즐길 거리 별점
        review.star_food = request.POST.get("star_food")        #* 먹거리 별점
        index.save()                                    #* index 객체 저장 후 index url으로 돌아감 
        return redirect("index")
    return render(request, "create.html")               #* get 요청 시 


# #* 모아보기 화면 (기본 )
# def index(request):
#     todo = Index.objects.all()
#     return render(request, "index.html", {"todo":todo})

#* 다른 사용자의 평점 모아보기 화면
def index(request):
    avg = Review.objects.all()
    return render(request, "index.html", {"avg":avg})


#* read 부분 
def detail(request, id):
    todo = get_object_or_404(Index, pk=id)
    return render(request, "detail.html", {"todo":todo})


#* views 부분
def update(request, id):
    update_todo = get_object_or_404(Index, pk=id)
    if request.method == "POST":
        update_todo.title=request.POST.get("content")
        update_todo.content=request.POST.get("content")
        update_todo.date=request.POST.get("date")
        update_todo.save()
        return redirect("detail", update_todo.pk)
    return render(request, "update.html", {"update_todo": update_todo})

#* delete 삭제 부분 
def delete(request, id):
    delete_todo=get_object_or_404(Index, pk=id)
    delete_todo.delete()
    return redirect("index")


#* Review 모델에 대한 정보를 가져와 HTML 페이지에 전달
    #^ 지민 수정 ) -> 점수는 뜨는데 별모양으로 안 뜬다. 

def review_list(request):
    reviews = Review.objects.all()
    # return render(request, 'review_list.html', {'reviews': reviews})
    return render(request, 'mypage.html', {'reviews': reviews})





#* 방법 2 시도..
def main_view(request):
    obj = Review.objects.filter(score=0).order_by("?").first()
    context ={
        'object':obj
    }
    return render(request, 'create.html', context)


# 방법 2 python models (사례 따라하기)
def RateList(request):
    queryset = Rate.objects.filter(ratings__isnull=False).order_by('ratings__average').first()
    context= {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, 'example.html', context)