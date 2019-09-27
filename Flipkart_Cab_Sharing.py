class Flipkart_Data:
    def add_user(self):
        user = [x for x in input().split()]
        print(user)

    def add_vehicle(self):
        vehicle = [x for x in input().split()]
        print(vehicle)

    def offer_ride(self):
        print("In Offer ride, enter ride details")
        offer_ride_entry = []
        for _ in range(4):
            offer_ride_entry.append([x for x in input().split()])
        return offer_ride_entry

def select_ride(offer_ride):
    print("In select, enter select ride")

    select_ride_entry = [x for x in input().split()]
    select_range = [x for x in range(len(offer_ride)) if select_ride_entry[1] == offer_ride[x][1] and select_ride_entry[2] == offer_ride[x][4]]
    select_list =[]
    for i in select_range:
        select_list.append(offer_ride[i])
    if len(select_range)>1:
        if select_ride_entry[3] == 'Fastest_Ride':
            select_list = sorted(select_list, key=offer_ride[6])[0]
        if select_ride_entry[3] == 'Earliest_ride':
            select_list = sorted(select_list, key=offer_ride[5])[0]
    print(f'efficient ride: {select_list[0]}')

    return select_ride_entry[0], select_list[0][6], select_list[0][0]

def fuel_saved(offer_ride):
    fuel_save = {}
    print("For Fuel Saved Please enter original offer ride")
    fuel_save_data_name, fuel_save_data_duration, offered  = select_ride(offer_ride)
    fuel_save[fuel_save_data_name] = fuel_save_data_duration
    print(fuel_save)

def ride_count(offer_ride):
    taken_name, fuel_save_data_duration, offered_name = select_ride(offer_ride)
    print(f'{taken_name}: 1 Taken, 0 Offered')
    print(f'{offered_name}: 0 Taken, 1 Offered')

f = Flipkart_Data()
print("Add user")
for _ in range(5):
    f.add_user()
while True:
     print("Enter your choice\n"
           "1 ---> Add vehicle\n"
           "q ---> quit\n")
     do = input('Enter name? ').split()
     n = do[0].strip().lower()
     if n == 1:
         f.add_vehicle()
     if n == 'q':
        break

offer_ride = f.offer_ride()
select_ride(offer_ride)
fuel_saved(offer_ride)


# while True:
#     print("Enter your choice\n"
#           "1 ---> Add user\n"
#           "2 ---> Add Vehicle\n"
#           "3 ---> Add Offer ride details\n"
#           "4 ---> Find Rides\n"
#           "5 ---> Fuel saved\n"
#           "q ---> to quit\n")
#     do = input('What would you like to do? ').split()
#     n = do[0].strip().lower()
#
#     if n == "1":
#         f.add_user()
#     if n == "2":
#         f.add_vehicle()
#     if n == "3":
#         f.offer_ride()
#     if n == "4":
#         select_ride(f.offer_ride())
#     if n == "5":
#         fuel_saved(f.offer_ride())
#     if n == "6":
#         ride_count(f.offer_ride())
#     if n == "q":
#         break
# print("Success..!!")
