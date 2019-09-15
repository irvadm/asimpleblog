from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from posts.models import Post, Comment


POSTS = [
    {'title': 'Nam ea dicunt mentitum pertinacia', 'body': 'At tota audiam sed, iusto accusata necessitatibus mei te, ius tempor lobortis eu. Probo tation sea no. Legimus debitis placerat nam in. An vix amet iriure viderer. Pri hinc fabulas dissentias et, at sea audire tamquam rationibus. Pri in case putent, et pro dicta decore verear, eu pri autem tollit.'},
    {'title': 'Utamur accusamus per ad', 'body': 'An mea regione aliquid. Ex vix postea semper molestiae, ad eos melius indoctum. Pro dicit iracundia ea, graeci molestie petentium cu vel, his et reque clita repudiare. Consul euripidis omittantur ne sit, mei amet principes id.'},
    {'title': 'Vis graece gloriatur tincidunt ut', 'body': 'Nusquam oporteat has in, his eu quaeque minimum epicurei. An agam veri comprehensam qui. Dictas iriure sit ut. Ne mea cibo nulla repudiare, ut rebum nihil philosophia nam. Usu falli omnesque in, voluptua antiopam nec eu. Platonem suscipiantur ex vim, cibo epicuri repudiandae ad has.'},
    {'title': 'Has no impetus antiopa', 'body': 'Ad causae mentitum complectitur mel, pro choro maluisset no. Purto liberavisse definitionem in pri, ex pri fabellas neglegentur necessitatibus, no dolores patrioque est. Vix altera ponderum deterruisset et, ei congue salutandi complectitur pri, honestatis efficiantur eam ut. Ignota postea copiosae no has, nam te purto nonumy. Erat minim no vim, ex cum modus utroque fastidii.'},
    {'title': 'Lorem ipsum dolor sit amet', 'body': 'Pro omnesque appellantur at, an nec omnes saepe, rebum dicunt equidem ea vim. Sed et simul labores, mel ea homero viderer. Falli graeco sit at, at has utinam corrumpit consetetur. Nam invidunt mediocritatem eu, ex per dicunt saperet interesset. Detraxit appellantur ex sea, audire consulatu hendrerit duo id. Errem legere duo no.'},
    {'title': 'Errem habemus ea mel', 'body': 'Nam affert inimicus ad, ea pro aliquam facilisis referrentur. An est simul forensibus. Melius equidem verterem an sea, dolor legere atomorum mel te. Tantas albucius mea ea, id lorem appareat prodesset eam. Pro tempor noluisse ex, vel eu utinam accusam copiosae, vel aliquip inciderint cu. At idque fabellas pro, ei his quod decore.'},
    {'title': 'Error docendi usu ex.', 'body': 'Hinc ipsum cu pri, te illud solet interpretaris mea, ius ne aeque congue. Id quod dignissim usu. Nam id fierent expetenda deseruisse, in noluisse torquatos vim. Est ex veri timeam dissentiet, stet electram sed ne, ubique blandit nominati at sea. Assum nostro option ea eam, id novum molestie luptatum his.'},
    {'title': 'Usu nibh denique conclusionemque et', 'body': 'Lorem ipsum dolor sit amet, est no error homero iisque, purto malorum scriptorem his at, ex simul eligendi vim. Mel ei clita labitur lucilius, aliquid laoreet propriae et eos. In alii probatus molestiae vim, pro at ferri eloquentiam instructior, ne vel option facilis. Ex causae appareat lucilius duo. Cum melius alterum recusabo ea, novum definitionem sit te.'},
    {'title': 'An mea regione aliquid', 'body': 'Id oblique delenit appellantur cum. Justo alterum accusamus cu sit. Debitis maluisset intellegebat pri ut, fuisset adipisci dissentias ne mea, mel maiestatis definitionem id. Tota constituto mediocritatem ea mei, ad quo meis omnes cetero.'},
    {'title': 'Ex vix postea semper molestiae', 'body': 'Vim elit corrumpit persequeris eu. Vix case tation scriptorem ad, id mutat regione est, nonumy salutandi eu sed. Sea paulo labitur ancillae ne, nam ad atqui munere soluta. Et nam iusto ancillae, ius ei nobis rationibus. Et vel iriure quaestio salutatus, natum accumsan et pri. Quis molestiae deseruisse ut nec, et vel tibique gubergren. Perfecto platonem eu vis, posse admodum mel at, ne veri harum democritum sea. Amet decore oportere eu cum. Sea animal virtute consequuntur ad. Pro sumo inani voluptatibus no.'},
]

COMMENTS = [
    'Ne sea consul primis erroribus, vis ad fugit affert. Qui id sint hinc reprehendunt, vix an expetenda iracundia mnesarchum.',
    'Est an ipsum oportere, no pri latine integre lobortis.',
    'Nam ea dicunt mentitum pertinacia.',
    'Vero omnis recusabo et quo, ex quot modus comprehensam eam, eu diam porro numquam vis.',
    'At eam mollis delenit intellegat.',
    'Lorem ipsum dolor sit amet, mazim libris vel no.',
    'Id inani constituam pri, odio verterem inciderint te cum, veniam corrumpit ex eos.',
    'Cum amet dicam tation an, sint patrioque sententiae per et.',
    'Ut dolor maiestatis reprehendunt cum, sea aliquam definitiones et.',
    'Duo ei fastidii facilisis. Posse mollis vix ad, homero antiopam mel at. Vis quodsi impetus cu. Quaestio sadipscing at vix.',
]


class Command(BaseCommand):
    help = 'Create posts and comments'

    def handle(self, *args, **kwargs):
        user = User.objects.get(username='admin')
        for i in range(10):
            post = Post.objects.create(
                title=POSTS[i]['title'],
                body=POSTS[i]['body'],
                creator=user
            )
            for j in range(10):
                Comment.objects.create(
                    content=COMMENTS[j],
                    creator=user,
                    post=post
                )
