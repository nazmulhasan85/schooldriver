import dal
from .models import StudentWorker
from ecwsp.sis.dal_registry import UserAutocomplete

dal.register(StudentWorker, UserAutocomplete)
