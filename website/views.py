from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
	return render(request, 'index.html', {})

def about(request):
	return render(request, 'about.html', {})

def covid(request):
	return render(request, 'covid.html', {})

def generalPractice(request):
	return render(request, 'generalPractice.html', {})


def womensHealth(request):
	return render(request, 'womensHealth.html', {})

def OGUK(request):
	return render(request, 'OGUK.html', {})

def occupational(request):
	return render(request, 'occupational.html', {})

def seafarers(request):
	return render(request, 'seafarers.html', {})

def cruise(request):
	return render(request, 'cruise.html', {})

def employment(request):
	return render(request, 'employment.html', {})
	

def contact(request):
	if request.method == "POST":
		message = request.POST['main-message']
		name = request.POST['message-name']
		email = request.POST['message-email']
		subject = request.POST['message-subject']

		#Send an email
		send_mail(
			subject, #subject
			message,#Message
			email,#from email
			['kennethtingweihock@gmail.com'],#to email

			)

		return render(request, 'contact.html', {'message-name':name})


	else: 
		return render(request, 'contact.html', {})

def appointment(request):

	if request.method == "POST":
		your_name = request.POST['your-name']
		your_email = request.POST['your-email']
		your_number = request.POST['your-number']
		your_service = request.POST['your-service']
		your_time = request.POST['your-time']
		your_note = request.POST['your-note']
		your_date = request.POST['your-date']


		#Send an email
		send_mail(
			'Appointment Request', #subject
			'name: ' + your_name + 
			'\nemail: ' + your_email + 
			'\nnumber: ' + your_number + 
			'\nservice: ' + your_service + 
			'\ntime: ' + your_time + 
			'\ndate: ' + your_date + 
			'\nnote: ' + your_note, #Message
			your_email,#from email
			['kennethtingweihock@gmail.com'],#to email

			)

		return render(request, 'appointment.html', {
			'your_name': your_name,
			'your_email': your_email,
			'your_number': your_number,
			'your_service': your_service,
			'your_time': your_time,
			'your_note': your_note,
			'your_date': your_date,

			})


	else: 
		return render(request, 'index.html', {})



def covidAppointment(request):

	if request.method == "POST":
		your_first_name = request.POST['your-first-name']
		your_last_name = request.POST['your-last-name']
		your_DOB = request.POST['your-date-of-birth']
		your_email = request.POST['your-email']
		your_number = request.POST['your-number']
		your_PPS = request.POST['your-pps']
		your_cohort = request.POST['your-cohort']
		your_factors = request.POST.getlist('your-factors')
		further_information = request.POST['further-information']

		your_factors_str = ""
		for factor in your_factors:
			your_factors_str = your_factors_str + factor + " || "


		#Send an email
		send_mail(
			'Appointment Request', #subject
			'First name: ' + your_first_name + 
			'\nLast name: ' + your_last_name + 
			'\nDate of Birth: ' + your_DOB + 
			'\nemail: ' + your_email + 
			'\nnumber: ' + your_number + 
			'\npps: ' + your_PPS +
			'\ncohort: ' + your_cohort + 
			'\nFactors: ' + your_factors_str + 
			'\nfurther information: ' + further_information, #Message
			your_email,#from email
			# ['kennethtingweihock@gmail.com'],#to email
			['ryanting2001@gmail.com'],#to email


			)


		return render(request, 'covidAppointment.html', {
			'your_first_name': your_first_name,
			'your_last_name': your_last_name,
			'your_date_of_birth': your_DOB,
			'your_email': your_email,
			'your_number': your_number,
			'your_PPS': your_PPS,
			'your_cohort': your_cohort,
			'your_factors': your_factors_str,
			'further_information': further_information,

			})


	else: 
		return render(request, 'index.html', {})


