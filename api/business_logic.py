import csv
from.models import *


def reading_and_writing(media):
    errors = []
    with open('media/' + str(media.file), "r") as f_obj:
        reader = csv.DictReader(f_obj)
        for row in reader:
            if len(row) != 5:
                errors.append('file structure error')
                return errors
            try:
                is_exist = Customer.objects.filter(username=row['customer']).count()
            except KeyError:
                errors.append('file structure error')
                return errors
            if is_exist == 0:
                try:
                    new_customer = Customer.objects.create(username=row['customer'],
                                                       spent_money=int(row['total']))
                except (ValueError, KeyError):
                    errors.append('file structure error')
                    return errors
            else:
                try:
                    new_customer = Customer.objects.get(username=row['customer'])
                    new_customer.spent_money += int(row['total'])
                    new_customer.save(update_fields=['spent_money'])
                except (ValueError, KeyError):
                    errors.append('file structure error')
                    return errors
            try:
                Deal.objects.create(gem_name=row['item'],
                                    quantity=row['quantity'],
                                    date_of_deal=row['date'],
                                    total_price=row['total'],
                                    customer=new_customer)
            except KeyError:
                errors.append('file structure error')
                return errors
    FileCSV.objects.get(id=media.id).file.delete()
    FileCSV.objects.get(id=media.id).delete()
    return errors