# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class emp_details(models.Model):
    _name = 'emp_details.emp_details'

    name = fields.Char('Name', size=40, required=True)
    code = fields.Char('Code')
    email = fields.Char('Email ID', size=40)
    pan = fields.Char('Pan No')
    mobile = fields.Char('Mobile Number +91', required=True, size=10)
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        'Blood Group')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender'), ('not to say', 'Not to say')],
        'Gender', required=True)
    marital = fields.Selection(
        [('married', 'Married'), ('unmarried', 'Unmarried')], 'Marital State', required=True)
    birth_date = fields.Date('Birth Date', required=True)
    father = fields.Char('Father name')
    mother = fields.Char('Mother name')
    fourWheeler = fields.Char('Four Wheeler No')
    twoWheeler = fields.Char('Two Wheeler No')
    smartcard = fields.Char('Smart Card No')
    bank = fields.Char('Bank Account Number')
    officialEmail = fields.Char('Official Email Id')
    relligion = fields.Selection(
        [('Hinduism', 'Hinduism'), ('jainism', 'Jainism'), ('muslimism', 'Muslimism'), ('other', 'Other'), ],
        'Relligion', required=True)
    nationality = fields.Many2one('res.country', 'Nationality', required=True)
    fingerprint = fields.Char('Finger Print No', required=True)
    uid = fields.Char('UID', size=10)
    differently = fields.Selection(
        [('no', 'No'), ('a', 'A'), ('b', 'B'), ('other', 'Other'), ], 'Differently abled', required=True)
    extension = fields.Char('Extension Number', size=4)
    reservation = fields.Selection([('gm', 'GM'), ('sc', 'SC'), ('st', 'ST'), ('obc', 'OBC'),
                                    ], 'Reservation Category', required=True)
    minority = fields.Selection([('yes', 'YES'), ('no', 'NO')], 'Minority', required=True)
    telephone1 = fields.Char('Telephone (Residence)')
    telephone2 = fields.Char('Telephone (Office)')
    image = fields.Binary('Upload Photo', help="Select image here")
    address_id = fields.One2many("employee.address", "address_id", "Address Details")

    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date > fields.Date.today():
                raise ValidationError("Birth Date can't be greater than current date!")

    @api.one
    @api.constrains('mobile')
    def _check_first_mobile(self):
        if re.match("^[0-9]{10}?$", self.mobile) == None:
            raise ValidationError("Invalid (Please Enter valid mobile number")

    @api.one
    @api.constrains('email')
    def _check_first_email(self):
        if re.match("^[a-z0-9_]+\@[a-z]+\.[a-z]{2,3}$", self.email) == None:
            raise ValidationError("Invalid (Please Enter valid EmailId!")

        @api.one
        @api.constrains('officialEmail')
        def _check_first_officialEmail(self):
            if re.match("^[a-z0-9_]+\@[a-z]+\.[a-z]{2,3}$", self.officialEmail) == None:
                raise ValidationError("Invalid (Please Enter valid officialEmail!")

    @api.one
    @api.constrains('name')
    def _check_first_name(self):
        if re.match("^[a-zA-Z_]", self.name) == None:
            raise ValidationError("Invalid (Please Enter valid Name!")
# ------------------------------___________________________________________________________________------------------------
# Address
# ------------------------------___________________________________________________________________------------------------
class address(models.Model):
    _name = "employee.address"

    address_id = fields.Many2one("emp_details.emp_details","Address")
    c_address_line1 = fields.Char(string='Address line1', required=True)
    c_address_line2 = fields.Char(string='Address line2')
    c_city = fields.Char('City', states={'done': [('readonly', True)]}, required=True)
    c_zip = fields.Char('Zip', size=8, states={'done': [('readonly', True)]})
    c_state = fields.Many2one(
        'res.country.state', 'States', states={'done': [('readonly', True)]}, required=True)
    c_country = fields.Many2one(
        'res.country', 'Country', states={'done': [('readonly', True)]}, required=True)

    address_line1 = fields.Char(string='Address line1', required=True)
    address_line2 = fields.Char(string='Address line2')
    city = fields.Char('City', states={'done': [('readonly', True)]}, required=True)
    zip = fields.Char('Zip', size=8, states={'done': [('readonly', True)]})
    state = fields.Many2one(
        'res.country.state', 'States', states={'done': [('readonly', True)]}, required=True)
    country = fields.Many2one(
        'res.country', 'Country', states={'done': [('readonly', True)]}, required=True)


