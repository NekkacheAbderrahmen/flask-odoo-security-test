from odoo import models, fields, api
import pdb, hashlib, requests

class Wiz_tab_one(models.TransientModel):
	_name="import.tab.one"
	_description="first wizard to import fils"

	user_name=fields.Char("nom de l'utilisateure ",required="true")
	secure_key=fields.Char("clé de securité ",required="true")
	file_data=fields.Binary(string="le fichier a importer")

	@api.multi
	def action_importe (self):
		URL = "http://127.0.0.1:5000/verify"
		user_name_encoded=self.user_name.encode()
		s_key_encoded=self.secure_key.encode()
		encryption= hashlib.md5()
		encryption.update(user_name_encoded)
		encryption.update(s_key_encoded)
		crypted = encryption.hexdigest()
		parameters = {'crp_key': crypted}
		req = requests.get(url = URL, params = parameters)
		if req.text == "true":
			env=self.env['files.tab']
			data={
				'file':self.file_data,
				'user_name':self.user_name
			}
			env.create(data)



class Wiz_tab_two(models.TransientModel):
	_name="import.tab.two"
	_description="seconde wizard to import fils"

	user_name=fields.Char("nom de l'utilisateure ",required="true")
	secure_key=fields.Char("clé de securité ",required="true")
	file_data=fields.Binary(string="le fichier a importer")

	@api.multi
	def action_importe (self):
		URL = "http://127.0.0.1:5000/verify"
		user_name_encoded=self.user_name.encode()
		s_key_encoded=self.secure_key.encode()
		encryption= hashlib.md5()
		encryption.update(user_name_encoded)
		encryption.update(s_key_encoded)
		crypted = encryption.hexdigest()
		parameters = {'crp_key': crypted}
		req = requests.get(url = URL, params = parameters)
		if req.text == "true":
			env=self.env['files.tab']
			data={
				'file':self.file_data,
				'user_name':self.user_name
			}
			env.create(data)
	
			


class Wiz_tab_three(models.TransientModel):
	_name="import.tab.three"
	_description="third wizard to import fils"

	user_name=fields.Char("nom de l'utilisateure ",required="true")
	secure_key=fields.Char("clé de securité ",required="true")
	file_data=fields.Binary(string="le fichier a importer")

	@api.multi
	def action_importe (self):
		URL = "http://127.0.0.1:5000/verify"
		user_name_encoded=self.user_name.encode()
		s_key_encoded=self.secure_key.encode()
		encryption= hashlib.md5()
		encryption.update(user_name_encoded)
		encryption.update(s_key_encoded)
		crypted = encryption.hexdigest()
		parameters = {'crp_key': crypted}
		req = requests.get(url = URL, params = parameters)
		if req.text == "true":
			env=self.env['files.tab']
			data={
				'file':self.file_data,
				'user_name':self.user_name
			}
			env.create(data)


class files_tab(models.Model):
	_name="files.tab"
	_description="files table"

	user_name=fields.Char(string="l'utilisateure conserner")
	file=fields.Binary(string="fichier importer ")
