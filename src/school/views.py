from django.shortcuts import render
from school.models import Question
from account.models import Account

# Create your views here.

def home_screen_view(request):
	context = {}
	# list_of_values = []
	# list_of_values.append("first entry")
	# list_of_values.append("second entry")
	# list_of_values.append("third entry")
	# list_of_values.append("fourth entry")

	# nameList = ["Theo", "Kaiah", "Josh", "Joyce"]

	# context = {
	# 	'some_string': "this is some string i'm passing into view",
	# 	'some_num': 23124234,
	# 	'list_of_values': list_of_values,
	# 	'nameList': nameList,
	# }

	# questions = Question.objects.all()
	# context['questions'] = questions

	accounts = Account.objects.all()
	context['accounts'] = accounts



	return render(request, "school/home.html", context)