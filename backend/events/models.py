from django.db import models
from django.db.models.signals import post_save, post_save
from django.dispatch import receiver
from django.db.models import Q, F

# Create your models here.

class IEvent(models.Model):
    title = models.CharField("Заголовок",max_length=250)
    place = models.CharField("Місце проведення",max_length=250)
    date_start = models.DateField("Дата початку")
    date_end = models.DateField("Дата завершення",null=True,blank=True)
    is_archived = models.BooleanField("Архівовано",default=False)
    is_completed = models.BooleanField("Завершено",default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.title} ({self.place},{self.date_start})"


COMPETITION_PLACE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )

class CompetitionResult(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE, related_name="participant_to_competition",verbose_name="Спортсмен")
    competition = models.ForeignKey('Competition',on_delete=models.CASCADE, related_name = 'competition_to_participant')

    sparing_place = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True,verbose_name="Місце по спарингам")
    tul_place = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True,verbose_name="Місце по тулях")
    spec_tech_place  = models.PositiveSmallIntegerField(choices=COMPETITION_PLACE, blank=True,null=True,verbose_name="Місце по спецтехніці")

    comment = models.CharField("Коментар",max_length=300,blank=True)

    class Meta:
        verbose_name="Результат спортсмена"
        verbose_name_plural="Результати спортсменів"


class CompetitionJudgment(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE, related_name="judge_to_competition",verbose_name="Суддя")
    competition = models.ForeignKey('Competition',on_delete=models.CASCADE, related_name = 'competition_to_judge')

    result = models.CharField(max_length=250, blank=True,null=True,verbose_name="Ким судив")
    comment = models.CharField("Коментар",max_length=300,blank=True,null=True)

    class Meta:
        verbose_name="Результат судді"
        verbose_name_plural="Результати суддів"

class Competition(IEvent):
    COMPETITION_TYPE = (
        ('t-1','Місцеве змагання'),
        ('t-2','Регіональне змагання',),
        ('t-3','Кубок області'),
        ('t-4','Чемпіонат області'),
        ('t-5','Кубок України'),
        ('t-6','Чемпіонат України'),
        ('t-7','Кубок Європи'),
        ('t-8','Чемпіонат Європи'),
        ('t-9','Кубок Світу'),
        ('t-10','Чемпіонат Світу')
    )

    competition_type = models.CharField("Тип змагання",max_length=4, choices=COMPETITION_TYPE)
    command_sparing = models.PositiveSmallIntegerField("Місце клубу по спарингам",choices=COMPETITION_PLACE, blank=True,null=True)
    command_tul = models.PositiveSmallIntegerField("Місце клубу по тулям",choices=COMPETITION_PLACE, blank=True,null=True)

    participants = models.ManyToManyField('account.BaseUser',through="CompetitionResult", related_name='competition_participant',verbose_name="Учасники")
    judgment = models.ManyToManyField('account.BaseUser',through="CompetitionJudgment", related_name='competition_judge',verbose_name="Судді")
    is_rating_calculated = models.BooleanField(default=False)


    def total_medals(self):
        table = self.competition_to_participant.all()
        golden = 0
        silver = 0
        bronze = 0
        for i in table:
            if(i.sparing_place == 1):
                golden += 1
            elif(i.sparing_place == 2):
                silver += 1
            elif(i.sparing_place == 3):
                bronze += 1

            if(i.tul_place == 1):
                golden +=1
            elif(i.tul_place == 2):
                silver += 1
            elif(i.tul_place == 3):
                bronze += 1

            if(i.spec_tech_place == 1):
                golden += 1
            elif(i.spec_tech_place == 2):
                silver += 1
            elif(i.spec_tech_place == 3):
                bronze += 1

        return f"{golden},{silver},{bronze}"

    class Meta:
        verbose_name="Змагання"
        verbose_name_plural="Змагання"




class AttestationResult(models.Model):
    participant = models.ForeignKey('account.BaseUser',on_delete=models.CASCADE, related_name="participant_to_attestation",verbose_name="Спортмен")
    attestation = models.ForeignKey('Attestation',on_delete=models.CASCADE, related_name="attestation_to_participant")

    from_belt = models.ForeignKey('account.Belt', on_delete=models.SET_NULL, null=True, related_name='attestation_from_belt',verbose_name="З поясу")
    to_belt = models.ForeignKey('account.Belt', on_delete=models.SET_NULL, null=True, related_name='attestation_to_belt',verbose_name="На пояс")
    comment = models.CharField("Коментар",max_length=300,blank=True)

    class Meta:
        verbose_name="Результат спортсмена"
        verbose_name_plural="Результати спортсменів"
    def __str__(self):
        return self.participant.full_name
    
class Attestation(IEvent):
    participants = models.ManyToManyField('account.BaseUser',through="AttestationResult", related_name='attestation_participant',verbose_name="Спортсмени")
    class Meta:
        verbose_name="Атестацію"
        verbose_name_plural="Атестації"



###SIGNALS
@receiver([post_save],sender=Attestation)
def handle_attestation(sender,instance,**kwargs):
    if(instance.is_completed):
        for result in instance.attestation_to_participant.all():
            if(result.participant.belt !=result.to_belt ):
                result.participant.belt = result.to_belt
                result.participant.save()
        Attestation.objects.filter(pk=instance.pk).update(is_archived=True)

@receiver([post_save],sender=Competition)
def handle_rating_calc(sender,instance,**kwargs):
    if(instance.is_completed and not instance.is_rating_calculated):
        koef = [5,4,3,2,1]
        competition_type = int(instance.competition_type.split('-')[1])
        comp_results = CompetitionResult.objects.filter(competition=instance)
        for result in comp_results:
            res = 0
            if result.sparing_place:
                res += koef[result.sparing_place-1]
            if result.tul_place:
                res += koef[result.tul_place-1]
            if result.spec_tech_place:
                res += koef[result.spec_tech_place-1]
            res *= competition_type
            result.participant.rating += int(res)
            result.participant.save()
        
        Competition.objects.filter(pk=instance.pk).update(is_rating_calculated=True)
        print("Рейтинг перераховано")




