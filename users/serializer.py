from rest_framework import serializers
from .models import User

from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterSerializer(serializers.ModelSerializer):


        class Meta:
            model=User
            fields=['username','email','password','token','role']
            # extra_kwargs={
            #      'role':{'read_only':True}
            # }
        

        token=serializers.SerializerMethodField('get_token')

        def get_token(self,obj) ->str:
          return self.context.get('token')
