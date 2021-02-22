periods = [' year', ' month', ' day', ' hour', ' min', ' sek']
user_time = 3601 + 3602 + 60 + 36000000

m_in = 60
hour = 60 * m_in
day = 24 * hour
month = 30 * day
year = 365 * day
rest_months = user_time % year
rest_days = rest_months % month
rest_hours = rest_days % day
rest_mins = rest_hours % hour
rest_seks = rest_mins % m_in

if user_time >= year:
    print(user_time // year, periods[0],
          rest_months // month, periods[1],
          rest_days // day, periods[2],
          rest_hours // hour, periods[3],
          rest_mins // m_in, periods[4],
          rest_seks, periods[5])

elif user_time >= month:
    print(rest_months // month, periods[1],
          rest_days // day, periods[2],
          rest_hours // hour, periods[3],
          rest_mins // m_in, periods[4],
          rest_seks, periods[5])

elif user_time >= day:
    print(rest_days // day, periods[2],
          rest_hours // hour, periods[3],
          rest_mins // m_in, periods[4],
          rest_seks, periods[5])

elif user_time >= hour:
    print(rest_hours // hour, periods[3],
          rest_mins // m_in, periods[4],
          rest_seks, periods[5])

elif user_time >= m_in:
    print(rest_mins // m_in, periods[4],
          rest_seks, periods[5])

else:
    print(user_time, periods[5])
