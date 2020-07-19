from celery import Celery
from send_email import Emailer


"""

# sync way to sending emails.

email_obj = Emailer(
	subject = "From Python",
	context = {"name":"Loganathan"},
	template_html = 'hello.html',
	to_emails = ['loganathandeveloper.k@gmail.com']
	)
send = email_obj.send()

print(send)

"""

# rabbitMq as broker here to hold the information in queues"

application = Celery('tasks', 
	broker="amqp://vbyyygia:Ig3H5zAilTR5hmecnBXz0g91iLOqakbA@lionfish.rmq.cloudamqp.com/vbyyygia", 
	backend="db+sqlite:///db.sqlite3"
	)

@application.task
def send_email(subject, context, template_html, to_emails):
	email_obj = Emailer(subject, context, template_html, to_emails)
	send = email_obj.send()

	if send:
		to = ', '.join(to_emails)
		message = f"Hey e-mail has sent successfully to {to}"
		return message

	return "e-mail was not sent"

