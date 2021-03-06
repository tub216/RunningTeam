from django.contrib.auth.models import User

def get_runner(self):
    """
    Get a runner instance for a given user.
    """
    from team.models import Runner
    return Runner.objects.get(user=self.id)

User.get_runner = get_runner
