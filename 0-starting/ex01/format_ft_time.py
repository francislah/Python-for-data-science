import datetime as dt

today = dt.date.today()

diff = dt.datetime.now() - dt.datetime(1970, 1, 1)

diff_float = '{:,.4f}'.format(diff.total_seconds())
diff_sci = '{:.2e}'.format(diff.total_seconds())
print(f"Seconds since January 1, 1970: {diff_float} or \
    {diff_sci} in scientific notation$")

print(today.strftime("%B %d %Y"))
