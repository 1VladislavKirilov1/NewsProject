from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаляет все новости из выбранной категории'

    def add_arguments(self, parser):
        parser.add_argument('postCategory', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["postCategory"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            postCategory = Category.objects.get(name=options['postCategory'])
            Post.objects.filter(postCategory=postCategory).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {postCategory.name}'))
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find postCategory'))