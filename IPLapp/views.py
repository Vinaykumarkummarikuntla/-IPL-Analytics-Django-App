"importing packages"
from IPLapp.models import Matches,Deliveries
from django.shortcuts import render
from django.db.models import Count,Sum

# Create your views here.

def Home(request):
    "creating a home function"
    return render(request,'home.html')



def PlayedPerYear(request):
    "creating a function for return the played per year matches"
    #result=Matches.objects.values('season').annotate(Count('season')).order_by('season')
    result=Matches.objects.values('team1').annotate(win=Count('id')).order_by('-win')
    return render(request,'playedperyear.html',{'result':result})

def WonPerYear(request):
    "creating a function for return the no matches won per year"
    result = list(Matches.objects.values('winner', 'season').annotate(Count('winner')).order_by('season'))
    #result=Matches.objects.values('season','winner').annotate(win=Count('winner')).order_by('season','-win')
    return render(request,'wonperyear.html',{'result':result})



def ExtraRunsin2016(request):
    "creating a function for return extra runs concedded for 2016"
    #result = Deliveries.objects.filter(match_id__season=2016).values('bowling_team').annotate(Sum('extra_runs')).order_by('extra_runs')

    result=Deliveries.objects.filter(match_id__season=2016).values('batting_team').annotate(extraruns=Sum('extra_runs')).order_by('extraruns')
    return render(request,'extrarunsin2016.html',{'result':result})



def EconomicBowler(request):
    "Creatig a function for top"
    result = list(Deliveries.objects.filter(match_id__season=2015).values
    ('bowler').annotate(eco=Sum('total_runs') / Count('over', distinct=True)).order_by('eco')[:10])
    #result = Deliveries.objects.filter(match_id__season=2015).values('bowler').annotate(economy=Sum('total_runs')*6/Count('total_runs')).order_by('economy')[:10]
    return render(request,'top10economybowlingin2015.html',{'result':result})
