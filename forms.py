from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError, SubmitField
from flask import Flask, request, redirect, render_template

#ContactForm class that specifies the format for a correct input
class ContactForm(FlaskForm):
	to_num = StringField('Enter number here (ex. +12345678901)', [validators.Required('Try again with a number.')])
	submit = SubmitField()
