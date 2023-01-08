import csv
from csv import Dialect
from typing import TextIO

from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class IndexView(TemplateView):

    template_name = "csv_parser/index.html"

    def post(self, request):

        tmp_csv: TextIO = request.FILES['csv']
        decoded_file = tmp_csv.read().splitlines()
        dialect = Dialect()
        dialect.delimiter = str(';')
        reader = csv.DictReader(decoded_file, dialect=dialect)

        return render(request=request, template_name=self.template_name)

