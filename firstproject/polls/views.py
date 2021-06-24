from __future__ import unicode_literals
from django.utils import timezone

import pprint

from django.shortcuts import render,get_object_or_404

import json
from django.core.serializers.json import DjangoJSONEncoder

from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Question,Choice,Tag

from django.shortcuts import render
from django.core import serializers


def index(request):
    ls_dict={}
    global ls
    ls=[]

    question= Question.objects.all()

    for x in range(len(question)):

        q=question[x]  #instance of question
        q_id = Question.objects.filter(question_text=q).values("id")
        print(q_id[0]['id'])
        cho_vot=(Choice.objects.filter(question=q).values("choice_text","votes"))
        cv_dict={}
        for c in cho_vot:           #concatenating choice and votes
            ch=c["choice_text"]
            vo=str(c["votes"])
            cv_dict[ch]=vo  #dictionary of choices and votes
        ls_tags=[]
        t=Tag.objects.filter(question=q).values("name")
        for l in t:
            ls_tags.append(l["name"])
           #list of tags
        ls_dict={"QID":q_id[0]['id'],"Question":q.question_text,"OptionVote":cv_dict,"Tags":ls_tags}
        ls.append(ls_dict)


    return HttpResponse(json.dumps(ls, indent=4), content_type="application/json")



def detail(request, question_id):
    global Question_id
    Question_id=question_id
    return render(request, 'polls/page2.html')


def poll_details(request):

    global ls
    ls= []
    try:
        questn = Question.objects.get(pk=Question_id)
        cho_vot = (Choice.objects.filter(question=questn).values("choice_text", "votes"))
        cv_dict = {}
        for c in cho_vot:  # concatenating choice and votes
            ch = c["choice_text"]
            vo = str(c["votes"])
            cv_dict[ch] = vo
        ls_tags = []
        t = Tag.objects.filter(question=questn).values("name")
        for l in t:
            ls_tags.append(l["name"])
        # dictionary of choices and votes

        # list of tags
        ls_dict = {"QID":Question_id, "Question": questn.question_text, "OptionVote": cv_dict,"Tags":ls_tags}
        ls.append(ls_dict)

    except Question.DoesNotExist:
        pass


    return HttpResponse(json.dumps(ls, indent=4), content_type="application/json")

def pollvotes(request):


    return HttpResponse(json.dumps(ls, indent=4), content_type="application/json")

@csrf_exempt
def update_votes(request):

    if request.method == 'PUT':
        print(request.body)
        choice = json.loads(request.body.decode('utf-8'))
        print(choice)
        if not choice:
            print('empty')
        else:
            question = get_object_or_404(Question, pk=Question_id)
            try:
                selected_choice = question.choice_set.get(choice_text=choice[0])
                selected_choice.votes += 1
                selected_choice.save()

            except Question.DoesNotExist:
                pass


    return HttpResponse(json.dumps(ls, indent=4), content_type="application/json")






def add(request):
    val1=int(request.POST["num1"])
    val2=int(request.POST["num2"])
    res=val1+val2
    return render(request,'result.html',{'result':res})



def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls / results.html', {'question': question})

def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))



@csrf_exempt
def createpost(request):
    if request.method == 'POST':
        print(request.body)
        data = json.loads(request.body.decode('utf-8'))

        q = Question(question_text=data["Question"], pub_date=timezone.now())
        q.save()
        for x,y in data["OptionVote"].items():
            q.choice_set.create(choice_text=x,votes=y)

        '''for x in range(len(data["Tags"])):
            q.tags.add(Tag.objects.get_or_create(name=data["Tags"][x]))

        #two scens :tag is present and tag not present
        #to add tags ,use add func parameter type
        # when the tag is present fetch the requird type and add it
        #when the tag is not present create tag'''
        t = Tag.objects.values("name")
        flag=0
        for x in range(len(data["Tags"])):
            for y in t:
                if(y["name"]==data["Tags"][x]):
                    flag=1

            if flag==1 :
                q.tags.add(Tag.objects.get(name=data["Tags"][x]))

            else:
                q.tags.add(Tag.objects.create(name=data["Tags"][x]))
    out="done"

    return HttpResponse(json.dumps({'status': 'success'}), content_type="application/json")



def tags(request):
    ls_tags=[]
    tags_dict={}
    t = Tag.objects.all().values("name")
    for l in t:
        ls_tags.append(l["name"])

    tags_dict["Tags"]=ls_tags

    return HttpResponse(json.dumps(tags_dict, indent=4), content_type="application/json")

def home_view(request):

    filterd_tags=request.GET.getlist('selctd_tags[]')


    html = "<html><body>It is now .</body></html>"

    ls=[]
    listid=[]
    for y in filterd_tags:

        t = Tag.objects.filter(name=y).values("question")
        if t.exists():
            for x in t:
                q_id = x['question']
                listid.append(q_id)

    listid=list(set(listid))
    for x in listid:
        try:
            questn = Question.objects.get(pk=x)
            cho_vot = (Choice.objects.filter(question=questn).values("choice_text", "votes"))
            cv_dict = {}
            for c in cho_vot:  # concatenating choice and votes
                ch = c["choice_text"]
                vo = str(c["votes"])
                cv_dict[ch] = vo  # dictionary of choices and votes
            ls_tags = []
            t = Tag.objects.filter(question=questn).values("name")
            for l in t:
                ls_tags.append(l["name"])
            # list of tags
            ls_dict = {"QID":x,"Question": questn.question_text, "OptionVote": cv_dict, "Tags": ls_tags}
            ls.append(ls_dict)
            print(ls)
        except Question.DoesNotExist:
            pass


        # instance of ques

    return HttpResponse(json.dumps(ls, indent=4), content_type="application/json")








