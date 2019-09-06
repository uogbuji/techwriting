def serve_table(tabnum):
    yield f'Welcome. Please sit at table {tabnum}. Here are your menus.'
    order = yield f'Table {tabnum}, what will you be having today?'
    yield 'OK I\'ll get that order in.'
    yield f'Table {tabnum}, here is your meal, {order}.'
    yield f'Table {tabnum}, did you enjoy your meal? Here is your check.'
    yield f'Thanks for visiting us, table {tabnum}!'

