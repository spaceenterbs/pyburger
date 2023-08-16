from django.db import models


class Burger(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    calories = models.IntegerField(default=0)

    def __str__(self):
        return self.name


"""
class 햄버거:
    이름
    가격
    칼로리
    
models.Model 클래스를 상속받아야 한다.
Django가 제공하는 models.Model 클래스는 정의한 클래스가 데이터베이스에서 하나의 테이블 역할을 할 수 있도록 도와준다.
"""
