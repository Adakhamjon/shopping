from django import template

register = template.Library()
@register.filter
def get_page_links(request,*args,**kwargs):
	page_num = kwargs["page"]
	items = kwargs["obj"]
	if items.has_previous:
		if bool(request.GET):
			return f"{request.get_full_path}&{page_num}"
		else:
			return f"?{page_num}"

	else:
		return "#"