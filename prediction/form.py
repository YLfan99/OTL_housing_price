from django import forms

Suburb_list = [('Abbotsford', 'Abbotsford'),
 ('Aberfeldie', 'Aberfeldie'),
 ('Airport West', 'Airport West'),
 ('Albanvale', 'Albanvale'),
 ('Albert Park', 'Albert Park'),
 ('Albion', 'Albion'),
 ('Alphington', 'Alphington'),
 ('Altona Meadows', 'Altona Meadows'),
 ('Altona North', 'Altona North'),
 ('Altona', 'Altona'),
 ('Ardeer', 'Ardeer'),
 ('Armadale', 'Armadale'),
 ('Arthurs Seat', 'Arthurs Seat'),
 ('Ascot Vale', 'Ascot Vale'),
 ('Ashburton', 'Ashburton'),
 ('Ashwood', 'Ashwood'),
 ('Aspendale Gardens', 'Aspendale Gardens'),
 ('Aspendale', 'Aspendale'),
 ('Attwood', 'Attwood'),
 ('Avondale Heights', 'Avondale Heights'),
 ('Avonsleigh', 'Avonsleigh'),
 ('Badger Creek', 'Badger Creek'),
 ('Balaclava', 'Balaclava'),
 ('Balnarring Beach', 'Balnarring Beach'),
 ('Balnarring', 'Balnarring'),
 ('Balwyn North', 'Balwyn North'),
 ('Balwyn', 'Balwyn'),
 ('Bangholme', 'Bangholme'),
 ('Baxter', 'Baxter'),
 ('Bayles', 'Bayles'),
 ('Bayswater North', 'Bayswater North'),
 ('Bayswater', 'Bayswater'),
 ('Beaconsfield Upper', 'Beaconsfield Upper'),
 ('Beaconsfield', 'Beaconsfield'),
 ('Beaumaris', 'Beaumaris'),
 ('Belgrave Heights', 'Belgrave Heights'),
 ('Belgrave South', 'Belgrave South'),
 ('Belgrave', 'Belgrave'),
 ('Bellfield', 'Bellfield'),
 ('Bend Of Islands', 'Bend Of Islands'),
 ('Bentleigh East', 'Bentleigh East'),
 ('Bentleigh', 'Bentleigh'),
 ('Berwick', 'Berwick'),
 ('Beveridge', 'Beveridge'),
 ('Big Pats Creek', 'Big Pats Creek'),
 ('Bittern', 'Bittern'),
 ('Black Rock', 'Black Rock'),
 ('Blackburn North', 'Blackburn North'),
 ('Blackburn South', 'Blackburn South'),
 ('Blackburn', 'Blackburn'),
 ('Blairgowrie', 'Blairgowrie'),
 ('Blind Bight', 'Blind Bight'),
 ('Bonbeach', 'Bonbeach'),
 ('Boneo', 'Boneo'),
 ('Boronia', 'Boronia'),
 ('Botanic Ridge', 'Botanic Ridge'),
 ('Box Hill North', 'Box Hill North'),
 ('Box Hill South', 'Box Hill South'),
 ('Box Hill', 'Box Hill'),
 ('Braybrook', 'Braybrook'),
 ('Briar Hill', 'Briar Hill'),
 ('Brighton East', 'Brighton East'),
 ('Brighton', 'Brighton'),
 ('Broadmeadows', 'Broadmeadows'),
 ('Brookfield', 'Brookfield'),
 ('Brooklyn', 'Brooklyn'),
 ('Brunswick East', 'Brunswick East'),
 ('Brunswick West', 'Brunswick West'),
 ('Brunswick', 'Brunswick'),
 ('Bulla', 'Bulla'),
 ('Bulleen', 'Bulleen'),
 ('Bundoora', 'Bundoora'),
 ('Bunyip North', 'Bunyip North'),
 ('Bunyip', 'Bunyip'),
 ('Burnley', 'Burnley'),
 ('Burnside Heights', 'Burnside Heights'),
 ('Burnside', 'Burnside'),
 ('Burwood East', 'Burwood East'),
 ('Burwood', 'Burwood'),
 ('Bylands', 'Bylands'),
 ('Cairnlea', 'Cairnlea'),
 ('Caldermeade', 'Caldermeade'),
 ('Camberwell', 'Camberwell'),
 ('Campbellfield', 'Campbellfield'),
 ('Cannons Creek', 'Cannons Creek'),
 ('Canterbury', 'Canterbury'),
 ('Cape Schanck', 'Cape Schanck'),
 ('Capel Sound', 'Capel Sound'),
 ('Cardinia', 'Cardinia'),
 ('Carlton North', 'Carlton North'),
 ('Carlton', 'Carlton'),
 ('Carnegie', 'Carnegie'),
 ('Caroline Springs', 'Caroline Springs'),
 ('Carrum Downs', 'Carrum Downs'),
 ('Carrum', 'Carrum'),
 ('Catani', 'Catani'),
 ('Caulfield East', 'Caulfield East'),
 ('Caulfield North', 'Caulfield North'),
 ('Caulfield South', 'Caulfield South'),
 ('Caulfield', 'Caulfield'),
 ('Chadstone', 'Chadstone'),
 ('Chelsea Heights', 'Chelsea Heights'),
 ('Chelsea', 'Chelsea'),
 ('Cheltenham', 'Cheltenham'),
 ('Chirnside Park', 'Chirnside Park'),
 ('Christmas Hills', 'Christmas Hills'),
 ('Chum Creek', 'Chum Creek'),
 ('Clarinda', 'Clarinda'),
 ('Clarkefield', 'Clarkefield'),
 ('Clayton South', 'Clayton South'),
 ('Clayton', 'Clayton'),
 ('Clematis', 'Clematis'),
 ('Clifton Hill', 'Clifton Hill'),
 ('Clyde North', 'Clyde North'),
 ('Clyde', 'Clyde'),
 ('Coburg North', 'Coburg North'),
 ('Coburg', 'Coburg'),
 ('Cockatoo', 'Cockatoo'),
 ('Coldstream', 'Coldstream'),
 ('Collingwood', 'Collingwood'),
 ('Coolaroo', 'Coolaroo'),
 ('Cora Lynn', 'Cora Lynn'),
 ('Cottles Bridge', 'Cottles Bridge'),
 ('Craigieburn', 'Craigieburn'),
 ('Cranbourne East', 'Cranbourne East'),
 ('Cranbourne North', 'Cranbourne North'),
 ('Cranbourne South', 'Cranbourne South'),
 ('Cranbourne West', 'Cranbourne West'),
 ('Cranbourne', 'Cranbourne'),
 ('Cremorne', 'Cremorne'),
 ('Crib Point', 'Crib Point'),
 ('Croydon Hills', 'Croydon Hills'),
 ('Croydon North', 'Croydon North'),
 ('Croydon South', 'Croydon South'),
 ('Croydon', 'Croydon'),
 ('Dallas', 'Dallas'),
 ('Dalmore', 'Dalmore'),
 ('Dandenong North', 'Dandenong North'),
 ('Dandenong South', 'Dandenong South'),
 ('Dandenong', 'Dandenong'),
 ('Deepdene', 'Deepdene'),
 ('Deer Park', 'Deer Park'),
 ('Delahey', 'Delahey'),
 ('Derrimut', 'Derrimut'),
 ('Devon Meadows', 'Devon Meadows'),
 ('Dewhurst', 'Dewhurst'),
 ('Diamond Creek', 'Diamond Creek'),
 ('Diggers Rest', 'Diggers Rest'),
 ('Dingley Village', 'Dingley Village'),
 ('Dixons Creek', 'Dixons Creek'),
 ('Docklands', 'Docklands'),
 ('Don Valley', 'Don Valley'),
 ('Doncaster East', 'Doncaster East'),
 ('Doncaster', 'Doncaster'),
 ('Donnybrook', 'Donnybrook'),
 ('Donvale', 'Donvale'),
 ('Doreen', 'Doreen'),
 ('Doveton', 'Doveton'),
 ('Dromana', 'Dromana'),
 ('Eaglemont', 'Eaglemont'),
 ('East Melbourne', 'East Melbourne'),
 ('East Warburton', 'East Warburton'),
 ('Eden Park', 'Eden Park'),
 ('Edithvale', 'Edithvale'),
 ('Elsternwick', 'Elsternwick'),
 ('Eltham North', 'Eltham North'),
 ('Eltham', 'Eltham'),
 ('Elwood', 'Elwood'),
 ('Emerald', 'Emerald'),
 ('Endeavour Hills', 'Endeavour Hills'),
 ('Epping', 'Epping'),
 ('Essendon North', 'Essendon North'),
 ('Essendon West', 'Essendon West'),
 ('Essendon', 'Essendon'),
 ('Eumemmerring', 'Eumemmerring'),
 ('Exford', 'Exford'),
 ('Eynesbury', 'Eynesbury'),
 ('Fairfield', 'Fairfield'),
 ('Fawkner', 'Fawkner'),
 ('Ferntree Gully', 'Ferntree Gully'),
 ('Ferny Creek', 'Ferny Creek'),
 ('Fingal', 'Fingal'),
 ('Fitzroy North', 'Fitzroy North'),
 ('Fitzroy', 'Fitzroy'),
 ('Flemington', 'Flemington'),
 ('Flinders', 'Flinders'),
 ('Footscray', 'Footscray'),
 ('Forest Hill', 'Forest Hill'),
 ('Frankston North', 'Frankston North'),
 ('Frankston South', 'Frankston South'),
 ('Frankston', 'Frankston'),
 ('Gardenvale', 'Gardenvale'),
 ('Garfield North', 'Garfield North'),
 ('Garfield', 'Garfield'),
 ('Gembrook', 'Gembrook'),
 ('Gladstone Park', 'Gladstone Park'),
 ('Gladysdale', 'Gladysdale'),
 ('Glen Huntly', 'Glen Huntly'),
 ('Glen Iris', 'Glen Iris'),
 ('Glen Waverley', 'Glen Waverley'),
 ('Glenroy', 'Glenroy'),
 ('Gowanbrae', 'Gowanbrae'),
 ('Greensborough', 'Greensborough'),
 ('Greenvale', 'Greenvale'),
 ('Gruyere', 'Gruyere'),
 ('Guys Hill', 'Guys Hill'),
 ('Hadfield', 'Hadfield'),
 ('Hallam', 'Hallam'),
 ('Hampton East', 'Hampton East'),
 ('Hampton Park', 'Hampton Park'),
 ('Hampton', 'Hampton'),
 ('Harkaway', 'Harkaway'),
 ('Hastings', 'Hastings'),
 ('Hawthorn East', 'Hawthorn East'),
 ('Hawthorn', 'Hawthorn'),
 ('Healesville', 'Healesville'),
 ('Heath Hill', 'Heath Hill'),
 ('Heatherton', 'Heatherton'),
 ('Heathmont', 'Heathmont'),
 ('Heidelberg Heights', 'Heidelberg Heights'),
 ('Heidelberg West', 'Heidelberg West'),
 ('Heidelberg', 'Heidelberg'),
 ('Highett', 'Highett'),
 ('Hillside', 'Hillside'),
 ('Hoddles Creek', 'Hoddles Creek'),
 ('Hoppers Crossing', 'Hoppers Crossing'),
 ('Hughesdale', 'Hughesdale'),
 ('Humevale', 'Humevale'),
 ('Huntingdale', 'Huntingdale'),
 ('Hurstbridge', 'Hurstbridge'),
 ('Iona', 'Iona'),
 ('Ivanhoe East', 'Ivanhoe East'),
 ('Ivanhoe', 'Ivanhoe'),
 ('Jacana', 'Jacana'),
 ('Junction Village', 'Junction Village'),
 ('Kalkallo', 'Kalkallo'),
 ('Kallista', 'Kallista'),
 ('Kalorama', 'Kalorama'),
 ('Kangaroo Ground', 'Kangaroo Ground'),
 ('Kealba', 'Kealba'),
 ('Keilor Downs', 'Keilor Downs'),
 ('Keilor East', 'Keilor East'),
 ('Keilor Lodge', 'Keilor Lodge'),
 ('Keilor North', 'Keilor North'),
 ('Keilor Park', 'Keilor Park'),
 ('Keilor', 'Keilor'),
 ('Kensington', 'Kensington'),
 ('Kew East', 'Kew East'),
 ('Kew', 'Kew'),
 ('Keysborough', 'Keysborough'),
 ('Kilsyth South', 'Kilsyth South'),
 ('Kilsyth', 'Kilsyth'),
 ('Kinglake West', 'Kinglake West'),
 ('Kinglake', 'Kinglake'),
 ('Kings Park', 'Kings Park'),
 ('Kingsbury', 'Kingsbury'),
 ('Kingsville', 'Kingsville'),
 ('Knoxfield', 'Knoxfield'),
 ('Koo Wee Rup', 'Koo Wee Rup'),
 ('Kooyong', 'Kooyong'),
 ('Kurunjang', 'Kurunjang'),
 ('Lalor', 'Lalor'),
 ('Lang Lang East', 'Lang Lang East'),
 ('Lang Lang', 'Lang Lang'),
 ('Langwarrin South', 'Langwarrin South'),
 ('Langwarrin', 'Langwarrin'),
 ('Launching Place', 'Launching Place'),
 ('Laverton', 'Laverton'),
 ('Lilydale', 'Lilydale'),
 ('Little River', 'Little River'),
 ('Longwarry', 'Longwarry'),
 ('Lower Plenty', 'Lower Plenty'),
 ('Lynbrook', 'Lynbrook'),
 ('Lyndhurst', 'Lyndhurst'),
 ('Lysterfield South', 'Lysterfield South'),
 ('Lysterfield', 'Lysterfield'),
 ('Macclesfield', 'Macclesfield'),
 ('Macleod', 'Macleod'),
 ('Maidstone', 'Maidstone'),
 ('Main Ridge', 'Main Ridge'),
 ('Malvern East', 'Malvern East'),
 ('Manor Lakes', 'Manor Lakes'),
 ('Maribyrnong', 'Maribyrnong'),
 ('Maryknoll', 'Maryknoll'),
 ('McCrae', 'McCrae'),
 ('McKinnon', 'McKinnon'),
 ('McMahons Creek', 'McMahons Creek'),
 ('Meadow Heights', 'Meadow Heights'),
 ('Melbourne', 'Melbourne'),
 ('Melton South', 'Melton South'),
 ('Melton West', 'Melton West'),
 ('Melton', 'Melton'),
 ('Mentone', 'Mentone'),
 ('Menzies Creek', 'Menzies Creek'),
 ('Mernda', 'Mernda'),
 ('Merricks Beach', 'Merricks Beach'),
 ('Merricks North', 'Merricks North'),
 ('Merricks', 'Merricks'),
 ('Mickleham', 'Mickleham'),
 ('Middle Park', 'Middle Park'),
 ('Mill Park', 'Mill Park'),
 ('Millgrove', 'Millgrove'),
 ('Mitcham', 'Mitcham'),
 ('Modella', 'Modella'),
 ('Monbulk', 'Monbulk'),
 ('Mont Albert North', 'Mont Albert North'),
 ('Mont Albert', 'Mont Albert'),
 ('Montmorency', 'Montmorency'),
 ('Montrose', 'Montrose'),
 ('Moonee Ponds', 'Moonee Ponds'),
 ('Moorabbin', 'Moorabbin'),
 ('Moorooduc', 'Moorooduc'),
 ('Mooroolbark', 'Mooroolbark'),
 ('Mordialloc', 'Mordialloc'),
 ('Mornington', 'Mornington'),
 ('Mount Burnett', 'Mount Burnett'),
 ('Mount Cottrell', 'Mount Cottrell'),
 ('Mount Dandenong', 'Mount Dandenong'),
 ('Mount Eliza', 'Mount Eliza'),
 ('Mount Evelyn', 'Mount Evelyn'),
 ('Mount Martha', 'Mount Martha'),
 ('Mount Toolebewong', 'Mount Toolebewong'),
 ('Mount Waverley', 'Mount Waverley'),
 ('Mulgrave', 'Mulgrave'),
 ('Murrumbeena', 'Murrumbeena'),
 ('Nangana', 'Nangana'),
 ('Nar Nar Goon North', 'Nar Nar Goon North'),
 ('Nar Nar Goon', 'Nar Nar Goon'),
 ('Narre Warren East', 'Narre Warren East'),
 ('Narre Warren North', 'Narre Warren North'),
 ('Narre Warren South', 'Narre Warren South'),
 ('Narre Warren', 'Narre Warren'),
 ('Newport', 'Newport'),
 ('Niddrie', 'Niddrie'),
 ('Noble Park North', 'Noble Park North'),
 ('Noble Park', 'Noble Park'),
 ('North Melbourne', 'North Melbourne'),
 ('North Warrandyte', 'North Warrandyte'),
 ('Northcote', 'Northcote'),
 ('Notting Hill', 'Notting Hill'),
 ('Nunawading', 'Nunawading'),
 ('Nutfield', 'Nutfield'),
 ('Nyora', 'Nyora'),
 ('Oak Park', 'Oak Park'),
 ('Oaklands Junction', 'Oaklands Junction'),
 ('Oakleigh East', 'Oakleigh East'),
 ('Oakleigh South', 'Oakleigh South'),
 ('Oakleigh', 'Oakleigh'),
 ('Officer', 'Officer'),
 ('Olinda', 'Olinda'),
 ('Ormond', 'Ormond'),
 ('Pakenham South', 'Pakenham South'),
 ('Pakenham Upper', 'Pakenham Upper'),
 ('Pakenham', 'Pakenham'),
 ('Panton Hill', 'Panton Hill'),
 ('Park Orchards', 'Park Orchards'),
 ('Parkdale', 'Parkdale'),
 ('Parkville', 'Parkville'),
 ('Parwan', 'Parwan'),
 ('Pascoe Vale South', 'Pascoe Vale South'),
 ('Pascoe Vale', 'Pascoe Vale'),
 ('Patterson Lakes', 'Patterson Lakes'),
 ('Pearcedale', 'Pearcedale'),
 ('Plenty', 'Plenty'),
 ('Plumpton', 'Plumpton'),
 ('Point Cook', 'Point Cook'),
 ('Point Leo', 'Point Leo'),
 ('Port Melbourne', 'Port Melbourne'),
 ('Portsea', 'Portsea'),
 ('Powelltown', 'Powelltown'),
 ('Preston', 'Preston'),
 ('Preston West', 'Preston West'),
 ('Princes Hill', 'Princes Hill'),
 ('Red Hill South', 'Red Hill South'),
 ('Red Hill', 'Red Hill'),
 ('Reefton', 'Reefton'),
 ('Research', 'Research'),
 ('Reservoir', 'Reservoir'),
 ('Richmond', 'Richmond'),
 ('Ringwood East', 'Ringwood East'),
 ('Ringwood North', 'Ringwood North'),
 ('Ringwood', 'Ringwood'),
 ('Ripponlea', 'Ripponlea'),
 ('Rockbank', 'Rockbank'),
 ('Rosanna', 'Rosanna'),
 ('Rosebud', 'Rosebud'),
 ('Rowville', 'Rowville'),
 ('Roxburgh Park', 'Roxburgh Park'),
 ('Rye', 'Rye'),
 ('Safety Beach', 'Safety Beach'),
 ('Sandhurst', 'Sandhurst'),
 ('Sandringham', 'Sandringham'),
 ('Sassafras', 'Sassafras'),
 ('Scoresby', 'Scoresby'),
 ('Seabrook', 'Seabrook'),
 ('Seaford', 'Seaford'),
 ('Seaholme', 'Seaholme'),
 ('Seddon', 'Seddon'),
 ('Selby', 'Selby'),
 ('Seville East', 'Seville East'),
 ('Seville', 'Seville'),
 ('Sherbrooke', 'Sherbrooke'),
 ('Shoreham', 'Shoreham'),
 ('Silvan', 'Silvan'),
 ('Skye', 'Skye'),
 ('Smiths Gully', 'Smiths Gully'),
 ('Somers', 'Somers'),
 ('Somerville', 'Somerville'),
 ('Sorrento', 'Sorrento'),
 ('South Kingsville', 'South Kingsville'),
 ('South Melbourne', 'South Melbourne'),
 ('South Morang', 'South Morang'),
 ('South Yarra', 'South Yarra'),
 ('Southbank', 'Southbank'),
 ('Spotswood', 'Spotswood'),
 ('Springvale South', 'Springvale South'),
 ('Springvale', 'Springvale'),
 ('St Albans', 'St Albans'),
 ('St Andrews Beach', 'St Andrews Beach'),
 ('St Andrews', 'St Andrews'),
 ('St Helena', 'St Helena'),
 ('St Kilda East', 'St Kilda East'),
 ('St Kilda West', 'St Kilda West'),
 ('St Kilda', 'St Kilda'),
 ('Steels Creek', 'Steels Creek'),
 ('Strathewen', 'Strathewen'),
 ('Strathmore Heights', 'Strathmore Heights'),
 ('Strathmore', 'Strathmore'),
 ('Sunbury', 'Sunbury'),
 ('Sunshine North', 'Sunshine North'),
 ('Sunshine West', 'Sunshine West'),
 ('Sunshine', 'Sunshine'),
 ('Surrey Hills', 'Surrey Hills'),
 ('Sydenham', 'Sydenham'),
 ('Tarneit', 'Tarneit'),
 ('Taylors Hill', 'Taylors Hill'),
 ('Taylors Lakes', 'Taylors Lakes'),
 ('Tecoma', 'Tecoma'),
 ('Templestowe Lower', 'Templestowe Lower'),
 ('Templestowe', 'Templestowe'),
 ('The Basin', 'The Basin'),
 ('The Patch', 'The Patch'),
 ('Thomastown', 'Thomastown'),
 ('Thornbury', 'Thornbury'),
 ('Three Bridges', 'Three Bridges'),
 ('Toolern Vale', 'Toolern Vale'),
 ('Tooradin', 'Tooradin'),
 ('Toorak', 'Toorak'),
 ('Tootgarook', 'Tootgarook'),
 ('Tottenham', 'Tottenham'),
 ('Travancore', 'Travancore'),
 ('Tremont', 'Tremont'),
 ('Truganina', 'Truganina'),
 ('Tuerong', 'Tuerong'),
 ('Tullamarine', 'Tullamarine'),
 ('Tyabb', 'Tyabb'),
 ('Tynong North', 'Tynong North'),
 ('Tynong', 'Tynong'),
 ('Upper Ferntree Gully', 'Upper Ferntree Gully'),
 ('Upwey', 'Upwey'),
 ('Vermont South', 'Vermont South'),
 ('Vermont', 'Vermont'),
 ('Viewbank', 'Viewbank'),
 ('Wandin East', 'Wandin East'),
 ('Wandin North', 'Wandin North'),
 ('Wantirna South', 'Wantirna South'),
 ('Wantirna', 'Wantirna'),
 ('Warburton', 'Warburton'),
 ('Warneet', 'Warneet'),
 ('Warrandyte South', 'Warrandyte South'),
 ('Warrandyte', 'Warrandyte'),
 ('Warranwood', 'Warranwood'),
 ('Waterways', 'Waterways'),
 ('Watsonia North', 'Watsonia North'),
 ('Watsonia', 'Watsonia'),
 ('Watsons Creek', 'Watsons Creek'),
 ('Wattle Glen', 'Wattle Glen'),
 ('Werribee South', 'Werribee South'),
 ('Werribee', 'Werribee'),
 ('Wesburn', 'Wesburn'),
 ('West Footscray', 'West Footscray'),
 ('West Melbourne', 'West Melbourne'),
 ('Westmeadows', 'Westmeadows'),
 ('Wheelers Hill', 'Wheelers Hill'),
 ('Whittlesea', 'Whittlesea'),
 ('Wildwood', 'Wildwood'),
 ('Williams Landing', 'Williams Landing'),
 ('Williamstown North', 'Williamstown North'),
 ('Williamstown', 'Williamstown'),
 ('Windsor', 'Windsor'),
 ('Wollert', 'Wollert'),
 ('Wonga Park', 'Wonga Park'),
 ('Woodstock', 'Woodstock'),
 ('Woori Yallock', 'Woori Yallock'),
 ('Wyndham Vale', 'Wyndham Vale'),
 ('Yallambie', 'Yallambie'),
 ('Yan Yean', 'Yan Yean'),
 ('Yannathan', 'Yannathan'),
 ('Yarra Glen', 'Yarra Glen'),
 ('Yarra Junction', 'Yarra Junction'),
 ('Yarrambat', 'Yarrambat'),
 ('Yarraville', 'Yarraville'),
 ('Yellingbo', 'Yellingbo'),
 ('Yering', 'Yering')]

class PredictForm(forms.Form):
    address = forms.CharField(label="Address", max_length=100)
    suburb = forms.ChoiceField(required=True, choices=Suburb_list, label="Suburb")
    bedrooms = forms.IntegerField(required=True, label="Bedrooms")
    bathrooms = forms.IntegerField(required=True, label="Bathrooms")
    cars = forms.IntegerField(required=True, label="Car Spaces")
    year_built = forms.IntegerField(label="Building Year")
    land_size = forms.IntegerField(label="Land Size")
    building_area = forms.IntegerField(label="Building Area")

