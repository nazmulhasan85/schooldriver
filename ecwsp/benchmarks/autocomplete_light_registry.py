import dal
from .models import Benchmark

class BenchmarkAutocomplete(dal.AutocompleteModelBase):
    search_fields = ['number', 'name']

dal.register(Benchmark, BenchmarkAutocomplete)
