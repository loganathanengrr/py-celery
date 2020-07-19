import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

class Template:
	template_name = ""
	context = None

	def __init__(self, template_name="", context=None, *args, **kwargs):
		self.template_name = template_name
		self.context = context

	def get_template(self):
		template_path = os.path.join(TEMPLATE_DIR, self.template_name)
		if not os.path.exists(template_path):
			raise Exception("The path does not exists")
		template_str = ""
		with open(template_path, 'r') as file_object:
			template_str = file_object.read()

		return template_str

	def render(self, context=None):
		render_context = context
		if self.context is not None:
			render_context = self.context
		if not isinstance(render_context, dict):
			render_context = {}
		template_str = self.get_template()

		return template_str.format(**render_context)


