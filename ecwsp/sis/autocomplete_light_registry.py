import dal
from .models import Student, EmergencyContact, Faculty

class UserAutocomplete(dal.AutocompleteModelBase):
    split_words = True
    search_fields = ['first_name', 'last_name']
    attrs = {
        'placeholder': 'Lookup Student(s)',
    }

class FacultyAutocomplete(UserAutocomplete):
    attrs = {
        'placeholder': 'Lookup Faculty',
    }

    
class ActiveStudentAutocomplete(UserAutocomplete):
    choices=Student.objects.filter(is_active=True)

class LookupStudentAutocomplete(UserAutocomplete, dal.AutocompleteModelTemplate):
    autocomplete_template = 'sis/lookup_student.html'

class ContactAutocomplete(dal.AutocompleteModelTemplate):
    split_words = True
    search_fields = ['fname', 'lname']
    attrs = {
        'placeholder': 'Lookup Contact(s)',
    }
    choice_template = 'sis/autocomplete_contact.html'

dal.register(EmergencyContact, ContactAutocomplete)
dal.register(Student, UserAutocomplete)
dal.register(Student, ActiveStudentAutocomplete)
dal.register(Faculty, FacultyAutocomplete)
dal.register(Student, LookupStudentAutocomplete)
