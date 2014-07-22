from collections import defaultdict
import matplotlib.pyplot as plt
import csv, sys, datetime

reader=csv.DictReader(open(sys.argv[1],'r'))

obamadonations = defaultdict(lambda:0)
mccaindonations = defaultdict(lambda:0)

for row in reader:
    name = row['cand_nm']
    datestr = row['contb_receipt_dt']
    amount = float(row['contb_receipt_amt'])
    date = datetime.datetime.strptime(datestr,'%d-%b-%y')

    if 'Obama' in name:
	obamadonations[date]=amount
    if 'McCain' in name:
	mccaindonations[date]=amount

sorted_by_date_obama=sorted(obamadonations.items(),key=lambda(key,val):key)
sorted_by_date_mccain=sorted(mccaindonations.items(),key=lambda(key,val):key)
xs,ys=zip(*sorted_by_date_obama)
zs,ws=zip(*sorted_by_date_mccain)
plt.plot(xs,ys,label='Obama')
plt.plot(zs,ws,label='McCain')
plt.legend(loc='upper cente', ncol=4)
plt.savefig('donations_cumulative.png',format='png')

