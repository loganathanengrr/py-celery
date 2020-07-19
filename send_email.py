import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from templates import Template

username = "<your_email>"
password = "<your_password>"

class Emailer:
	from_email = "<your email>"

	def __init__(self, subject="", context={}, template_name=None, template_html=None, to_emails=None):
		if template_name == None and template_html==None:
			raise Exception("You must be set a template txt/html")
		assert isinstance(to_emails, list)

		self.subject = subject
		self.template_name = template_name
		self.template_html = template_html
		self.context = context
		self.to_emails = ', '.join(to_emails)

	def format_message(self):
		msg = MIMEMultipart('alternative')
		msg['From'] = self.from_email
		msg['To'] =  self.to_emails
		msg['subject'] = self.subject

		if self.template_name is not None:
			template_obj = Template(self.template_name, self.context)
			text_part =  MIMEText(template_obj.render(), 'plain')
			msg.attach(text_part)
		elif self.template_html is not None:
			template_obj =  Template(self.template_html, self.context)
			html_part = MIMEText(template_obj.render(), 'html')
			msg.attach(html_part)
		else:
			pass

		msg_str = msg.as_string()
		return msg_str

	def send(self):
		did_send = False

		msg =  self.format_message()
		with smtplib.SMTP(host='smtp.gmail.com', port='587') as server:
			server.ehlo()
			server.starttls()
			server.login(username, password)
			try:
				server.sendmail(self.from_email, self.to_emails, msg)
				did_send =  True
			except:
				did_send = False
		return did_send
