from django.db import models

# Create your models here.
class Athlete(models.Model):
    athlete_id = models.IntegerField(primary_key=True)
    athlete_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}선수'.format(self.sport, self.athlete_name)

    class Meta:
        db_table = 'Athlete'

class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=2)
    country_name = models.CharField(unique=True, max_length=30)

    def __str__(self):
        return self.country_name
    
    class Meta:
        db_table = 'Country'
        
class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=30)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name
    
    class Meta:
        db_table = 'City'


class Game(models.Model):
    game_id = models.IntegerField(primary_key=True)
    olympic = models.ForeignKey('Olympic', on_delete=models.CASCADE)
    sport = models.ForeignKey('Sport', on_delete=models.CASCADE)
    gender = models.CharField(max_length=4, blank=True, null=True)
    game_name = models.CharField(max_length=40)
    medal_type = models.CharField(max_length=2)

    def __str__(self):
        return '{} {} 종목 {} {}메달'.format(self.olympic, self.sport, self.game_name, self.medal_type)
    
    class Meta:
        db_table = 'Game'
        unique_together = (('game_id', 'medal_type'),)

class Olympic(models.Model):
    olympic_id = models.IntegerField(primary_key=True)
    host_year = models.IntegerField()
    season = models.CharField(max_length=4)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} 올림픽'.format(self.host_year, self.city)
    
    class Meta:
        db_table = 'Olympic'

class Participate(models.Model):
    game = models.OneToOneField('Game', on_delete=models.CASCADE, primary_key=True)
    athlete = models.ForeignKey('Athlete', on_delete=models.CASCADE)
    medal_type = models.CharField(max_length=2)

    def __str__(self):
        return '{} {}'.format(self.game, self.athlete)
    

    class Meta:
        db_table = 'Participate'
        unique_together = (('athlete', 'medal_type', 'game'),)


class Sport(models.Model):
    sport_id = models.IntegerField(primary_key=True)
    sport_name = models.CharField(unique=True, max_length=20)
    season = models.CharField(max_length=4)

    def __str__(self):
        return self.sport_name
    
    class Meta:
        db_table = 'Sport'