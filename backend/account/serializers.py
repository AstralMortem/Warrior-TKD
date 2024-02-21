from rest_framework.serializers import ModelSerializer
from .models import BaseUser,Belt,BeltDescription
from events.serializers import CompetitionResultSerializer, CompetitionJudgmentSerializer, AttestationResultSerializer




class BeltListSerializer(ModelSerializer):
    class Meta:
        model = Belt
        fields = "__all__"

class BeltDescriptionSerializer(ModelSerializer):
    class Meta:
        model = BeltDescription
        exclude=['id']

class BeltDetailSerializer(ModelSerializer):
    description = BeltDescriptionSerializer(read_only=True)
    class Meta:
        model = Belt
        fields = ['code','title','photo','description']



class UserListSerializer(ModelSerializer):
    belt = BeltListSerializer(many=False)
    class Meta:
        model = BaseUser
        fields = ['id','full_name','photo', 'is_staff','mobile','belt']


class UserDetailSerializer(ModelSerializer):
    coach = UserListSerializer(many=False)
    belt = BeltListSerializer(many=False)
    competitions = CompetitionResultSerializer(source="participant_to_competition", many=True)
    judgments = CompetitionJudgmentSerializer(source="judge_to_competition", many=True)
    attestations = AttestationResultSerializer(source="participant_to_attestation",many=True)
    class Meta:
        model = BaseUser
        exclude = [
            "groups",
            "date_joined",
            "is_active",
            "user_permissions",
            "last_login",
            "is_superuser",
            "password"
        ]   

