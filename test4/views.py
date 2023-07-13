from django.shortcuts import render

# Create your views here.
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
