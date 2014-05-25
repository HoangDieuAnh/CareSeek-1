# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
def index():
    return dict()

def about():
    return dict()
def contact():
    return dict()
def dashboard():
    return dict()
def feedback():
    return dict()
def myProfile():
    return dict()
def mySchedule():
    return dict()
def help():
    return dict()
def settings():
    return dict()
def search():
    return dict()
def legal():
    return dict()
def privacy():
    return dict()

def user():
    
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    auth.settings.formstyle = 'bootstrap'
    auth.settings.register_next = URL('profile')
    auth.settings.logged_url = URL('index')

    auth.settings.login_next = URL('dashboard')
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def loadEmail():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.Email)
	for entry in user:
		email = entry.Email.email
	return email

def loadPhone():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.Contact)
	for entry in user:
		Phone = entry.Contact.Phone
	print Phone
	return Phone

def loadPass():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.Password)
	for entry in user:
		Password = entry.Password.password
	return Password

def loadFirstName():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.FirstName)
	for entry in user:
		FirstName = entry.FirstName.first_name
	return FirstName

def loadLastName():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.LastName)
	for entry in user:
		LastName = entry.LastName.last_name
	print LastName
	return LastName

def loadCV():
	if(auth.user.User_Type == "Carer"):
		query = db.Carer.UserId == auth.user.id

	elif(auth.user.User_Type == "Care Seeker"):
		query = db.Carer.UserId == auth.user.id

	user = db(query).select(db.Carer.CV)
	for entry in user:
		CV = entry.CV
	return CV

def loadInterests():
	interests = ['Playing guitar','Reading','Romantic walks to the fridge','Basketball','Breaking g-strings']
	return interests

def loadDescription():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.Description)
	user = db(query).select(db.Carer.Description)
	for entry in user:
		Description = entry.Description
	return Description

def loadProfilePic():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.ProfilePic)
	user = db(query).select(db.Carer.ProfilePic)
	for entry in user:
		ProfilePic = entry.ProfilePic
	return ProfilePic

def loadAge():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.Age)
	user = db(query).select(db.Carer.Age)
	for entry in user:
		Age = entry.Age.Age
	return Age

def loadGender():
	query = db.Carer.UserId == auth.user.id
	user = db(query).select(db.Carer.Gender)
	user = db(query).select(db.Carer.Gender)
	for entry in user:
		Gender = entry.Gender.Gender
	return Gender

# def loadProfile():
#     pass
