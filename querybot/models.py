from django.db import models

# Create your models here.

ENTITY_TYPES = (
    ('manual', 'manual'),
    ('snips', 'snips'),
)

class Entity(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    automatically_extensible = models.BooleanField(default=True)
    use_synonyms = models.BooleanField(default=True)
    matching_strictness = models.FloatField(default=1.0)
    entity_type = models.CharField(max_length=50, choices=ENTITY_TYPES, default='')
    metadata = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)



class EntityRecord(models.Model):
    entity = models.ForeignKey(Entity, related_name='values', on_delete=models.CASCADE)
    word = models.CharField(max_length = 200)
    metadata = models.CharField(max_length=300, blank=True, null=True)

    def __unicode__(self):
        return str(self.entity.name) + ' - ' + str(self.word)

    def __str__(self):
        return str(self.entity.name) + ' - ' + str(self.word)



class Synonym(models.Model):
    entity_record = models.ForeignKey(EntityRecord, related_name='synonyms', on_delete=models.CASCADE)
    word = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.entity_record.word) + ' - ' + str(self.word)

    def __str__(self):
        return str(self.entity_record.word) + ' - ' + str(self.word)


class Intent(models.Model):
    name = models.CharField(max_length=400, primary_key=True)
    category = models.CharField(max_length=100, default='General')
    related_entities = models.ManyToManyField(Entity, related_name='intents', blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

class EntitySlot(models.Model):
    name = models.CharField(max_length=50)
    entity = models.ForeignKey(Entity, related_name='slots', on_delete=models.CASCADE)
    intent = models.ForeignKey(Intent, related_name='slots', on_delete=models.CASCADE)
    example_value = models.CharField(max_length=250, blank=True, null=True)


    def __unicode__(self):
        return str(self.intent.name) + ' - ' + str(self.name)

    def __str__(self):
        return str(self.intent.name) + ' - ' + str(self.name)

class Utterance(models.Model):
    text = models.TextField()
    intent = models.ForeignKey(Intent, related_name='utterances', on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.intent.name) + ' - ' + str(self.text)

    def __str__(self):
        return str(self.intent.name) + ' - ' + str(self.text)