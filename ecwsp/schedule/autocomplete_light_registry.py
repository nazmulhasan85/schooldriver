import dal
from .models import CourseSection

class CourseSectionAutocomplete(dal.AutocompleteModelBase):
    split_words = True
    search_fields = ['name', 'course__fullname', 'course__shortname']

dal.register(CourseSection, CourseSectionAutocomplete)
