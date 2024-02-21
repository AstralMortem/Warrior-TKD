from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Competition,Attestation, CompetitionJudgment, CompetitionResult, AttestationResult



class AttestationResultSerializer(ModelSerializer):
    class Meta:
        model = AttestationResult
        fields = "__all__"


class AttestationSerializer(ModelSerializer):

    class Meta:
        model = Attestation
        fields = "__all__"


class CompetitionResultSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = CompetitionResult
        fields = ['total']

    def get_total(self,obj):
        title = obj.competition.title
        date = obj.competition.date.lower
        res = f"{title}({date}) | "
        if obj.sparing_place:
            res += f"Спаринг - {obj.sparing_place}, "
        if obj.tul_place:
            res += f"Туль - {obj.tul_place}, "
        if obj.spec_tech_place:
            res += f"Спец.Техніка - {obj.spec_tech_place}"
        return res


class CompetitionJudgmentSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = CompetitionJudgment
        fields = ['total']

    def get_total(self,obj):
        title = obj.competition.title
        date = obj.competition.date.lower
        res = f"{title}({date}) | "
        if(obj.result):
            res += obj.result
        return res


class CompetitionSerializer(ModelSerializer):
    # participants = CompetitionResultSerializer(many=True,source="competition_to_participant")
    # judgment = CompetitionJudgmentSerializer(many=True, source="competition_to_judge")
    total_medals = SerializerMethodField()
    class Meta:
        model = Competition
        fields = "__all__"

    def get_total_medals(self,obj):
        return obj.total_medals()