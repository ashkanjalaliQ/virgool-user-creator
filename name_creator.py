import random


def get_name():
    first_name = [
        'مهدی',
        'امیر',
        'علیرضا',
        'قاسم',
        'ویدا',
        'نگین',
        'محمدرضا',
        'آرمین',
        'آرزو',
        'خلیل'
    ]

    last_name = [
        'نجداد',
        'رضایی',
        'حاجعلی',
        'نصیری',
        'سلطانی',
        'آهنگر',
        'جمشیدی',
        'میمری',
        'بابارحمتی',
        'ولی زاده'
    ]

    return first_name[random.randint(0, len(first_name) - 1)] + ' ' + last_name[random.randint(0, len(last_name) - 1)]
