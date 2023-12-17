from django.db.models import Count
from django.views.generic import ListView , DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

from django.views import View


class Builder:
    def __init__(self, model,GLOBAL_PAGINATION=2):
        self.model = model
        self.GLOBAL_PAGINATION = GLOBAL_PAGINATION

    def add_list_values(self,template_name,extra_context):
        self.template_name = template_name
        self.extra_context = extra_context
        return self
    
    def with_fields(self, fields):
        self.fields = fields
        return self
    
    def detail_update_template(self, detail_template=None):
        if not detail_template:
            template_parts = self.template_name.split(".")
            template_parts[0] += "_detail"
            updated_template = ".".join(template_parts)
            self.updated_template = updated_template
        else:
            self.updated_template = detail_template
        return self
    
    def detail_page(self,page_template=None):
        if not page_template:
            template_parts = self.template_name.split(".")
            template_parts[0] += " detail"
            updated_template,_ = template_parts
            self.extra_context_detail = {"page":updated_template }
        else:
            self.extra_context = {"page":page_template}
        
        return self
    
    def add_cols_json(self, *cols):
        self.cols=cols
        return self


    def detail_build(self):
        class Detail(LoginRequiredMixin,DetailView):
            model = self.model
            template_name = self.updated_template
            extra_context = self.extra_context_detail
            fields = '__all__'

                
            def get(self, request, *args, **kwargs):
                self.object = self.get_object()  
                context = self.get_context_data(object=self.object)
                return self.render_to_response(context)

            
            def get_fields(self, obj):
                if not self.fields == '__all__':
                    return {field: getattr(obj, field) for field in self.fields}
                
                return {field.name: getattr(obj, field.name) for field in obj._meta.fields}
        
        return Detail
    
    def list_view(self):
        class List(LoginRequiredMixin,ListView):
            model = self.model
            template_name = self.template_name
            extra_context = self.extra_context
            paginate_by = self.GLOBAL_PAGINATION
            fields = '__all__'

        return List
    
    def per_user_view(self):

        class ListViewFilter(LoginRequiredMixin, View):
            model = self.model
            cols = self.cols

            def get(self, request, *args, **kwargs):
                user = request.user

                consulta = self.model.objects.filter(user=user)
                consulta_data = list(consulta.values(*self.cols))
        
                total_count = consulta.aggregate(total=Count('user'))['total']
    
                return JsonResponse({"data":consulta_data,"total":total_count}, safe=False)

        return ListViewFilter



