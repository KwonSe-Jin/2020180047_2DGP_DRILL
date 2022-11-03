table = {
"SLEEP": {"HIT"     : "WAKE"},
"WAKE" : {"TIMER10"  : "SLEEP"}
}

cur_state = 'SLEEP'
event = 'HIT'
next_state = table[cur_state][event]
print(table[cur_state]['HIT'])
print(table['WAKE']['TIMER10'])
