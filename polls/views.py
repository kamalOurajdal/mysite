from django.db.models.expressions import F
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic.detail import DetailView as DjangoDetailView
from django.views.generic.list import ListView

from .models import Question, Choice


# Create your views here.

class IndexView(ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(DjangoDetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(DjangoDetailView):
    model = Question
    template_name = "polls/results.html"

def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. 1aa4396d is the polls index.")
    return response



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
