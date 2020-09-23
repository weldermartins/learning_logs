from django.db import models

class Topic(models.Model):
	""" Um assunto sobre o qual o usuário esta aprendendo. """
	text = models.CharField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		""" Devolve uma representação em string do modelo."""
		return self.text
		
class Entry(models.Model):
	""" Algo especifico aprendido sobre um assunto"""
	# essa chave associa cada entrada a um assunto.
	topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	
class Meta:
	verbose_name_plural = 'entries'
	
	def __str__(self):
		""" Devolve uma representação em string do modelo"""
		return self.text[:50] + "..."





