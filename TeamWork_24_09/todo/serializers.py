from rest_framework import serializers
from .models import Todo, Category


class TodoSerializers(serializers.ModelSerializer):
    days = serializers.SerializerMethodField()
    category =serializers.StringRelatedField() # buradaki category todo modelindeki field, default
    class Meta:
         model=Todo
         fields="__all__"
    def get_days(self,obj):
        return(now()-obj.createDate).days
    def validate_task(self,value):
        if value .lower()=="python":
            raise serializers.validationError("python cannot be our task")
            return
        


class CategorySerializers(serializers.ModelSerializer):

    categorys=TodoSerializers(many=True)  #tüm todo geldi 
    # categorys =serializers.StringRelatedField(many=True)  # sadece str meotodu geldi
    # categorys =serializers.PrimaryKeyRelatedField(many=True, read_only=True)  #  sadece id geldi
class Meta:
         model=Category
         fields="__all__"
