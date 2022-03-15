from typing import Iterable, Union
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from api.models import FizzBuzz
from api.selectors import (
    get_fizzbuzz_by_id, 
    get_fizzbuzzes
)
from api.services import (
    create_fizzbuzz
)

class FizzBuzzView(APIView):
    class InputSerializer(serializers.Serializer):
        message = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = FizzBuzz
            fields = (
                "fizzbuzz_id",
                "useragent",
                "creation_date",
                "message"
            )

    def get(self, request, pk: int = None) -> Union[FizzBuzz, Iterable[FizzBuzz]]:
        if pk:
            try:
                fizzbuzz = get_fizzbuzz_by_id(fizzbuzz_id=pk)
                data = self.OutputSerializer(fizzbuzz).data
                return Response(data)
            except FizzBuzz.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        fizzbuzzes = get_fizzbuzzes()
        data = self.OutputSerializer(fizzbuzzes, many=True).data
        
        return Response(data)
    
    def post(self, request):
        in_serializer = self.InputSerializer(data=request.data)
        
        if not in_serializer.is_valid():
            # would maybe be more useful to provide user 
            # with more information on required fields that are missing
            # or other things that would make a successful request
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # storing "AnonymousUser" might not be useful information. Alternative would be to allow nulls for useragent field in model
        current_useragent = request.headers.get("User-Agent") or "AnonymousUser"

        fizzbuzz = create_fizzbuzz(useragent=current_useragent, **in_serializer.validated_data)

        fizzbuzz = self.OutputSerializer(fizzbuzz).data

        return Response(fizzbuzz, status=status.HTTP_201_CREATED)

