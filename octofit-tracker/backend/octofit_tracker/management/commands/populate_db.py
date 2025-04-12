from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test data
        user1 = User(username='thundergod', email='thundergod@mhigh.edu', password='password')
        user2 = User(username='metalgeek', email='metalgeek@mhigh.edu', password='password')
        user1.save()
        user2.save()

        team = Team(name='Blue Team')
        team.save()
        team.members.add(user1, user2)

        # Correct the duration field to use timedelta
        activity = Activity(user=user1, activity_type='Cycling', duration=timedelta(hours=1))
        activity.save()

        leaderboard = Leaderboard(user=user1, score=100)
        leaderboard.save()

        workout = Workout(name='Cycling Training', description='Training for a road cycling event')
        workout.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
