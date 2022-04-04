{
    'name' : 'Hospital Management',
    'author' : 'W A Geraldine',
    'summary' : 'Hospital Management Software',
    'version' : '1.0',
    'sequence' : -100,
    'description' : 'Hotel Management Software',
    'category' : 'productivity',
    'website' : 'https://www.tipskampus.wordpress.com',
    'depends' : ['sale', 'mail', 'contacts'],
    'data' : [
        'security/ir.model.access.csv',
		'data/data.xml',
		'wizard/create_appointment_view.xml',
        'wizard/create_checkin_view.xml',
        'wizard/create_checkout_view.xml',
        'wizard/create_change_room_view.xml',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/employees.xml',
        'views/service_checkup_view.xml',
        'views/room_view.xml',
        'views/nurse_view.xml',
        'views/cleaning_service_view.xml',
        'views/checkup_view.xml',
        'views/reservation_view.xml',
        'views/checkout_view.xml',
        'views/appointment_view.xml',
        'views/change_room_view.xml',
        'report/report.xml',
        'report/checkin_report.xml',
        'report/patient_card.xml'
    ],
    'demo' : [],
    'qweb' : [],
    'installable' : True,
    'application' : True,
    'auto_install' : False,
}