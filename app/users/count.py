from app.users.models import Profile
from app.vacancys.models import Vakancys

countProfileCom = Profile.objects.filter(id_type_user__type_user_name='компания').count()
countProfileProg = Profile.objects.filter(id_type_user__type_user_name='программист').count()
countVacancys = Vakancys.objects.all().count()