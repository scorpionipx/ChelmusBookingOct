from __future__ import absolute_import

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.template.defaultfilters import slugify
from . import get_current_user

NAME_MAX_LENGTH = 100
DESCRIPTION_MAX_LENGTH = 1500
PHONE_MAX_LENGTH = 20
SLUG_MAX_LENGTH = 255

DEFAULT_DESCRIPTION = 'fara descriere'
DEFAULT_PHONE = 'nespecificat'
DEFAULT_MAIL = 'nespecificat'
DEFAULT_SITE = 'nespecificat'


class Advertisement(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=True, related_name='advertisements',
                             verbose_name='author')

    name = models.CharField(max_length=NAME_MAX_LENGTH, blank=False, null=False, verbose_name='Titlu',
                            help_text='Titlul anuntului <br>Titlul anuntului este primul lucru observat de client. <br>'
                                      'Acesta ar trebui sa contina informatii concrete si atragatare.<br>Nu se accepta'
                                      ' nume nule (goale)!')

    main_image = models.ImageField(blank=True, null=True, default=None, verbose_name='Imaginea de profil',
                                   upload_to='profiles/%Y/%m/%d',
                                   help_text='Imaginea de prezentare<br><br><br>Galerie foto')

    description = models.TextField(max_length=DESCRIPTION_MAX_LENGTH, blank=True,
                                   verbose_name='Descriere', help_text='Descriere amanuntita a anuntului')

    CATEGORY_CHOICES = (('HOT', 'Hotel'), ('PEN', 'Pensiune'), ('HOS', 'Hostel'), ('APA', 'Apartament'),
                        ('VIL', 'Vila'), ('CAB', 'Cabana'), ('GAR', 'Garsoniera'), ('BIR', 'Birou'),
                        ('SPA', 'Spatiu comercial'), ('ALT', 'Altceva'))
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0],
                                verbose_name='Categorie', help_text='Tipul anuntului')

    city = models.CharField(max_length=100, blank=False, null=False, verbose_name='Localitate')

    COUNTY_CHOICES = (('AB', 'Alba'), ('AG', 'Arges'), ('AR', 'Arad'), ('B', 'Bucuresti'), ('BC', 'Bacau'),
                      ('BH', 'Bihor'), ('BN', 'Bistrita-Nasaud'), ('BR', 'Braila'), ('BT', 'Botosani'),
                      ('BV', 'Brasov'), ('BZ', 'Buzau'), ('CJ', 'Cluj'), ('CL', 'Calarasi'), ('CS', 'Caras-Severin'),
                      ('CT', 'Constanta'), ('CV', 'Covasna'), ('DB', 'Dambovita'), ('DJ', 'Dolj'), ('GJ', 'Gorj'),
                      ('GL', 'Galati'), ('GR', 'Giurgiu'), ('HD', 'Hunedoara'), ('HR', 'Harghita'), ('IF', 'Ilfov'),
                      ('IL', 'Ialomita'), ('IS', 'Iasi'), ('MH', 'Mehedinti'), ('MM', 'Maramures'), ('MS', 'Mures'),
                      ('NT', 'Neamt'), ('OT', 'Olt'), ('PH', 'Prahova'), ('SB', 'Sibiu'), ('SJ', 'Salaj'),
                      ('SM', 'Satu Mare'), ('SV', 'Suceava'), ('TL', 'Tulcea'), ('TM', 'Timis'), ('TR', 'Teleorman'),
                      ('VL', 'Valcea'), ('VN', 'Vrancea'), ('VS', 'Vaslui'))
    county = models.CharField(max_length=2, choices=COUNTY_CHOICES, default=COUNTY_CHOICES[0], blank=False, null=False,
                              verbose_name='Judet')

    price = models.IntegerField(default=0, verbose_name='Pret', help_text='Pretul in euro')

    wifi = models.BooleanField(default=False, verbose_name='Wi-Fi')
    parking = models.BooleanField(default=False, verbose_name='Parcare')
    children_playground = models.BooleanField(default=False, verbose_name='Loc de joaca pentru copii', )
    swimming_pool = models.BooleanField(default=False, verbose_name='Piscina')
    launch = models.BooleanField(default=False, verbose_name='Mic dejun')
    spa = models.BooleanField(default=False, verbose_name='SPA')

    date_created = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='created')

    site = models.URLField(blank=True, verbose_name='Site', help_text='Adresa web a proprietatii')
    mail = models.EmailField(blank=True, verbose_name='Email', help_text='Adresa de email')
    phone = models.CharField(max_length=PHONE_MAX_LENGTH, verbose_name='Telefon',
                             help_text='Numarul de telefon')
    stars = models.IntegerField(blank=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)],
                                editable=True, verbose_name='Stele',
                                help_text='Daca acest argument nu se aplica anuntului dumneavoastra, utilizati valoarea'
                                          ' 0!<br><br><h3>Servicii oferite</h3>')

    image_0 = models.ImageField(blank=True, null=True, default=None, verbose_name='Imaginea de galerie 1',
                                   upload_to='profiles/%Y/%m/%d')
    image_1 = models.ImageField(blank=True, null=True, default=None, verbose_name='Imaginea de galerie 2',
                                   upload_to='profiles/%Y/%m/%d')
    image_2 = models.ImageField(blank=True, null=True, default=None, verbose_name='Imaginea de galerie 3',
                                   upload_to='profiles/%Y/%m/%d')
    image_3 = models.ImageField(blank=True, null=True, default=None, verbose_name='Imaginea de galerie 4',
                                   upload_to='profiles/%Y/%m/%d')
    image_4 = models.ImageField(blank=True, null=True, default=None, verbose_name='Imaginea de galerie 5',
                                   upload_to='galery/%Y/%m/%d')

    slug = models.SlugField(max_length=SLUG_MAX_LENGTH, blank=True, editable=False)

    class Meta:
        # unique_together = ('user', 'name')
        ordering = ('date_created', )

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):

        if self.description is None or self.description == '':
            self.description = DEFAULT_DESCRIPTION
            print(self.description)

        if self.mail is None or self.mail == '':
            self.mail = DEFAULT_MAIL

        if self.site is None or self.site == '':
            self.site = DEFAULT_SITE

        if self.phone is None or self.phone == '':
            self.phone = DEFAULT_PHONE

        current_request_user = get_current_user.get_thread_user()
        self.user = current_request_user.user
        self.slug = slugify(str(self.user.username) + '-' + str(self.name) + '-id-' + str(self.pk))
        
        super(Advertisement, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return 'advertisements:DetailAdvertisement', (), {'slug': self.slug}






