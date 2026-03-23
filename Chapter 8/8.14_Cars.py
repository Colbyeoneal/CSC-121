##Function
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

## Sample call - **kwargs stumped me for a moment 
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)