## Convert miliary time to standard time

u_time = input('Input military time for conversion to standard time: <2400 hours>\n')
m_time = int(u_time)
hours = m_time // 100
minutes = str(m_time - (hours * 100))

if m_time >= 1200:
    tod = 'PM'
else:
    tod = 'AM'

if hours > 12:
    hours = hours - 12
elif hours is 00:
    hours = 12

hours = str(hours)
if len(hours) is 1:
    hours = '0%s' % (hours)
if len(minutes) is 1:
    minutes = '0%s' % (minutes)

print('Military Time:', u_time)
print('Standard Time: %s:%s%s' % (hours, minutes, tod))
