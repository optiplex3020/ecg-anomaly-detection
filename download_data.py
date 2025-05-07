import wfdb
import os
wfdb.dl_database('mitdb', dl_dir='mitdb')
records = wfdb.get_record_list('mitdb')
print(records[:10], '…', len(records), 'enregistrements au total')