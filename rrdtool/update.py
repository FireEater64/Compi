average = os.getloadavg()[0]
from rrdtool import update as rrd_update
ret = rrd_update('RS0.rrd', 'N:%s' %(average))
