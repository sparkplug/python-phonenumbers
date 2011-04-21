"""Auto-generated file, do not edit by hand. TL metadata"""
from phonenumbers import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_TL = PhoneMetadata(id='TL', country_code=670, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern=u'[2-47-9]\d{6}', possible_number_pattern=u'\d{7}'),
    fixed_line=PhoneNumberDesc(national_number_pattern=u'(?:2[1-5]|3[1-9]|4[1-4])\d{5}', possible_number_pattern=u'\d{7}', example_number=u'2112345'),
    mobile=PhoneNumberDesc(national_number_pattern=u'7[2-4]\d{5}', possible_number_pattern=u'\d{7}', example_number=u'7212345'),
    toll_free=PhoneNumberDesc(national_number_pattern=u'80\d{5}', possible_number_pattern=u'\d{7}', example_number=u'8012345'),
    premium_rate=PhoneNumberDesc(national_number_pattern=u'90\d{5}', possible_number_pattern=u'\d{7}', example_number=u'9012345'),
    shared_cost=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    personal_number=PhoneNumberDesc(national_number_pattern=u'70\d{5}', possible_number_pattern=u'\d{7}', example_number=u'7012345'),
    voip=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    pager=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    uan=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern=u'NA', possible_number_pattern=u'NA'),
    number_format=[NumberFormat(pattern='(\d{3})(\d{4})', format=u'\\1 \\2')])