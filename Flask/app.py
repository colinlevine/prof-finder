from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

# methods = ['GET', 'POST'] allows our route to take in
# ONLY GET or POST methods
# by default, it's only GET, so we need to add a POST.
profsThatTeach = []

@app.route('/', methods=['GET', 'POST'])
def home():
    # this 'if' block executes when we visit http://localhost:5000
    # on our browser (essentially a GET request)
    if request.method == 'GET':
        return render_template('index.html')

    # code here executes when we make a HTTP POST request
    # essentially when we click on the 'submit' button

    # identifying our values by department (department field in input element)
    department = request.form.get('department')
    course = request.form.get('course')

    # doing stuff with input values
    # replace this with whatever processing you wish to do
    courseName = department+course
    # IMPORTANT - you still need to render_template
    # but now you can pass in additional data to the frontend
    # which you can display there however you want

    #csceDict = {"prof_name": ["course1, course2", "professor_rating", "professor_difficulty"]}
    csceDict = {'Riccardo Bettati': [['CSCE313', 'CSCE410', 'CSCE611'], 2.6, 4.8, 50],
                'Martin Carlisle': [['CSCE120', 'CSCE121', 'CSCE222', 'CSCE465', 'CSCE489', 'CSCE704'], 4.5, 3.5, 85.3659],
                'James Caverlee': [['CSCE489', 'CSCE670'], 4.4, 3, 100],
                'Christiana Chamon': [['CSCE120', 'CSCE121', 'CSCE206'], 4.5, 3.1, 100],
                'Theodora Chaspari': [['CSCE421'], 5, 2.5, 100],
                'Jianer Chen': [['CSCE411', 'CSCE608', 'CSCE629'], 2.5, 4.3, 44.4444],
                'Yoonsuck Choe': [['CPSC420', 'CPSC625', 'CS633', 'CSCE420', 'csce421'], 4, 3.9, 100],
                'Dilma Silva': [['CSCE121', 'CSCE365', 'CSCE410', 'CSCE465'], 4.5, 3.3, 90],
                'Paula deWitte': [['CSCE402', 'CSCE702'], 5, 2.5, 100],
                'Guofei Gu': [['CSCE465'], 1.9, 4.6, 12.5],
                'Ricardo Gutierrez-Osuna': [['CPSC689', 'CPSCSECT', 'CSCE000', 'CSCE481', 'CSCE482', 'CSCE491', 'CSCE630', 'CSCE681'], 1.6, 2.5, 40],
                'Drew Hamilton': [['CSCE410', 'CSCE611'], 2, 3.5, 100],
                'Tracy Hammond': [['CSCE222', 'CSCE482', 'CSCE689'], 2.1, 3.6, None],
                'Maristela Holanda': [['CSCE121'], 3.1, 3.9, 100],
                'Ruihong Huang': [['CSCE470', 'CSCE638'], 2.3, 3, 40],
                'Thomas Ioerger': [['CSCE121', 'CSCE420'], 4.5, 2.8, 100],
                'Shuiwang Ji': [['CSCE636'], 1.9, 5, 25],
                'Anxiao Jiang': [['CPSC222', 'CSCE222', 'CSCE411', 'CSCE629', 'CSCE689'], 4.5, 3.3, 90],
                'Daniel Jimenez': [['CSCE614'], 4.5, 3.5, 100],
                'Nima Kalantari': [['CSCE441', 'CSCE489'], 3.4, 2.9, 80],
                'John Keyser': [['CSCE181', 'CSCE430'], 4.9, 2.9, 100],
                'Eun Kim': [['CSCE312', 'CSCE614'], 4.3, 4.3, 72.7273],
                'Jeeeun Kim': [['CSCE436', 'CSCE667'], 2.3, 1.5, 83.3333],
                'Andreas Klappenecker': [['CSCE222', 'CSCE311', 'CSCE411', 'CSCE629'], 2.5, 4.4, 41.6667],
                'Alan Kuhnle': [['CSCE222'], 2, 5, "n/a"],
                'Sandeep Kumar': [['CSCE111', 'CSCE222'], 3.3, 4.4, 100],
                'Hyunyoung Lee': [['CSCE222', 'CSCE314'], 2.5, 4.2, 44],
                'Teresa Leyk': [['CPCS221', 'CPCS222', 'CPSC211', 'CPSC211311', 'CPSC221', 'CPSC311', 'CSCE121', 'CSCE206', 'CSCE221', 'CSCE221222', 'CSCE222'], 4.4, 4, 69.8795],
                'Robert Lightfoot': [['CSCE111', 'CSCE121', 'CSCE315', 'CSCE412'], 4.1, 2.7, 95.6522],
                'Jyh Liu': [['CSCE451', 'CSCE462'], 1.5, 4, 37.5], 'Dmitri Loguinov': [['CSCE313', 'CSCE463'], 5, 4.5, 100],
                'Shawn Lupoli': [['CMSC104', 'CMSC151', 'CMSC201', 'CMSC331', 'CMSC341', 'CMSC433', 'CSC201', 'CSCE221'], 3.4, 3.4, 61.9048],
                'Rabi Mahapatra': [['CPSC321', 'CPSC489', 'CSCE312', 'CSCE350', 'CSCE462', 'CSCE482', 'CSCE617'], 1.8, 3.9, None],
                'Michael Moore': [['CSCE121', 'CSCE221', 'CSCE436', 'CSCE489', 'CSCE689'], 2.6, 3.6, 57],
                'Bobak Mortazavi': [['CSCE421'], 3.4, 4.3, 57.1429],
                'Robin Murphy': [['CSCE483', 'CSCE625'], 1.3, 3.7, None],
                'Abdullah Muzahid': [['CSCE312', 'CSCE350'], 2.4, 4.1, 42.8571],
                "Jason O'Kane": [['CSCE215', 'CSCE350', 'CSCE374', 'CSCE574', 'CSCE750', 'CSCE774'], 4.4, 3.1, 81.8182],
                'Michael Quinn': [['CSCE121', 'CSCE689'], 3, 3.6, 60], 
                'Philip Ritchey': [['CSCE121', 'CSCE221', 'CSCE221H', 'CSCE222', 'CSCE489', 'CSCE689', 'CSCE701', 'ENGR111', 'ENGR112'], 2.7, 4.2, 38.9831],
                'Vivek Sarin': [['CPSC442', 'CSCE222', 'CSCE435', 'CSCE735', 'ENGR111'], 4.3, 2.9, 100],
                'Scott Schaefer': [['CSCE181', 'CSCE221','CSCE221H', 'CSCE441'], 4.8, 1.7, 100],
                'Dylan Shell': [['CSCE121', 'CSCE314', 'CSCE420', 'CSCE482'], 3.1, 4.1, 51.4286],
                'Frank Shipman': [['CSCE445', 'CSCE477', 'CSCE679'], 5, 1.8, 100],
                'Radu Stoleru': [['CSCE410', 'CSCE438', 'CSCE464', 'CSCE662'], 4.8, 4.1, 100],
                'Shinjiro Sueda': [['CSCE441', 'CSCE489'], 4.9, 3.8, 90.9091],
                'Sing-Hoi Sze': [['BICH419', 'CSCE222', 'CSCE411', 'CSCE629'], 5, 3, 100],
                'Paul Taele': [['CSCE120', 'CSCE121', 'CSCE315'], 5, 4.3, 92.6829],
                'Shawna Thomas': [['CSCE315', 'CSCE411'], 5, 3.3, 100],
                'Aakash Tyagi': [['CSCE181', 'CSCE221', 'CSCE312', 'CSCE313', 'CSCE314'], 5, 4.6, 96.7213],
                'Pauline Wade': [['CSCE431', 'CSCE482', 'ENGR181', 'ENGR181H', 'ENGR381'], 1.4, 3.2, 10.3448],
                'Duncan Walker': [['ECEN680'], 4, 3, None],
                'Ronald Ward': [['CSCE222'], 2.3, 4, "n/a"],
                'Ki Hwan Yum': [['COS206', 'CSCE110', 'CSCE206', 'CSCE312'], 2.8, 3.6, 60]}
    
    mathDict = {'Angela Allen': [['105', 'ALEGR112', 'GRWT101', 'MAT110', 'MAT112', 'MAT113', 'MAT129', 'MAT156', 'MATH105', 'MATH110', 'MATH112'], 3.3, 3, 20], 'Patricia Ruiz': [['MATH304', 'MATH425'], 5, 3.4, 100], 'Michael Anshelevich': [['MATH172', 'MATH220', 'MATH311', 'MATH409', 'MATH446', 'MATH447'], 4.4, 3.9, 91.6667], 'Amy Austin': [['CALC152', 'CALCULUS', 'M152', 'MAH151', 'MATH142', 'MATH151', 'MATH151152', 'MATH152', 'MATH172', 'MATH251'], 5, 3.9, 96.748], 'Dean Baskin': [['MATH151', 'MATH171', 'MATH308', 'MATH323', 'MATH460'], 3.7, 3.5, 76.9231], 'Guy Battle': [['409', 'MAT151', 'MATH151', 'MATH152', 'MATH251', 'MATH308', 'MATH309', 'MATH311', 'MATH401', 'MATH409', 'MATH411'], 4, 3.1, 64.8649], 'Florent Baudier': [['MATH151', 'MATH172', 'MATH220', 'MATH251', 'MATH308', 'MATH409', 'SUB'], 3.8, 3.3, 43.75], 'Gregory Berkolaiko': [['MATH308', 'MATH411', 'MATH412', 'MATH425', 'MATH602'], 4.5, 3.5, 100], 'Harold Boas': [['436', '617618', 'MATH171', 'MATH300', 'MATH407', 'MATH409', 'MATH436', 'MATH618'], 5, 3, 100], 'Irina Bobkova': [['MTH 161', 'MTH161', 'MTH161MTH142', 'MTH162', 'MTH164', 'MTH172'], 2.8, 3.8, 66.6667], 'Kathryn Bollinger': [['141', '142', 'MATH', 'MATH131', 'MATH140', 'MATH141', 'MATH142', 'MATH166', 'MATH167'], 3, 4, 39.7059], 'Andrea Bonito': [['MATH151'], 2.7, 4, 100], 'Justin Cantu': [['MATH131', 'MATH140', 'MATH148', 'MATH151', 'MATH221', 'MATH251', 'Math300', 'MATH304', 'MATH521'], 5, 2.8, 100], 'Tamara Carter': [['MATH140', 'MATH166', 'MATH167', 'MATH365', 'MATH366'], 4.1, 3.3, 85.9649], 'Simone Cecchini': [['Math-304', 'Math-407'], 2.6, 4, 100], 'Goong Chen': [['MATH251', 'MATH308', 'MATH401', 'MATH685'], 4.6, 2.4, 100], 'Liwei Chen': [['MATH007A', 'MATH007B', 'MATH009B', 'MATH046', 'MATH146B', 'MATH7A'], 4.1, 2.9, 87.5], 'Vanessa Coffelt': [['MATH1140', 'MATH140', 'MATH147', 'MATH150', 'MATH151', 'MATH508', 'MTH147'], 5, 4.6, 67.0213], 'Andrew Comech': [['308', 'MATH308'], 2.9, 3.6, 55.5556], 'Prabir Daripa': [['MATH304', 'MATH311', 'MATH442'], 2.6, 3.6, 54.5455], 'Alan Demlow': [['MA113', 'MA114', 'MA214', 'MATH308', 'MS214'], 4.3, 3.1, 100], 'Ken Dykema': [['MATH151', 'MATH221'], 2.9, 3.6, 75], 'Yalchin Efendiev': [['MATH308', 'MATH417'], 4.6, 2, 100], 'Janice Epstein': [['141', 'MATH140', 'MATH141', 'MATH151', 'MATH166', 'MATH167'], 2.4, 3.6, 41.4634], 'Tamas Erdelyi': [['MATH151', 'MATH152'], 2.3, 4.2, 31.3433], 'John Fisk': [['MATH140', 'MATH142', 'MATH151'], 5, 3.8, 94.2308], 'Ali Foran': [['151', 'MATH1325', 'MATH141', 'MATH150'], 5, 2.6, 100], 'Simon Foucart': [['MATH323', 'MATH677'], 3, 4, None], 'Bradford Garcia': [['MATH140', 'Math142', 'MATH151'], 4.9, 3.4, 93.75], 'Nataliia Goncharuk': [['MATH308', 'MATH3110'], 2.3, 4.3, 100], 'Sherry Gong': [['MATH304'], 5, 1.8, 100], 'Rostislav Grigorchuk': [['MATH304', 'MATH415'], 3.5, 3.4, 100], 'Jean-Luc Guermond': [['MATH601', 'PDE'], 2.3, 4.5, None], 'Alexandru Hening': [['MATH135', 'MATH32'], 5, 3.5, 100], 'Yvette Hester': [['MATH 142', 'MATH142', 'MATH147', 'MATH148'], 3.5, 4.2, 50], 'Irina Holmes': [['MATH152', 'MATH172', 'MATH308'], 5, 3.4, 90.9091], 'Peter Howard': [['ANY', 'ANYTHING', 'CLA1100', 'CLA2200', 'CLA2223', 'CLA2260', 'GRKSECT', 'HON2200', 'LAT101', 'LATIN', 'MTH1100', 'MYTH', 'MYTH1', 'MYTH101', 'MYTH1101', 'MYTH2260', 'MYTHOLOGY'], 4.9, 1.9, 90], 'Bill Johnson': [['1301SOCIO', 'MARFA1301', 'SOC1301', 'SOCI1301', 'SOCI2301', 'SOCI2319', 'SOCIO1301', 'SOCIO2301', 'SOCIOLOGY', 'SOCIOLOGY1301', 'SPCI1301'], 5, 2, 94.4444], 'Joe Kahlig': [['152', '251', 'BUSN141', 'MATH141', 'MATH151', 'MATH151527', 'MATH152', 'MATH166', 'MATH251', 'MATH325'], 5, 4, 85.2174], 'Kendra Kilmer': [['141', '142', 'CALC111', 'MATH131', 'MATH140', 'MATH141', 'MATH142', 'MATH147'], 4.8, 4.4, 58.9595], 'Joungdong Kim': [['MATH151'], 5, 3, 100], 'Patricia Klein': [['HORT301', 'HORT306'], 4.6, 2.4, 90], 'Jeffrey Kuan': [['MATH251', 'MATH409', 'MATH411'], 3.8, 3.5, 69.2308], 'Peter Kuchment': [['MATH200', 'MATH308', 'MATH311', 'MATH611'], 3.8, 3.3, 60], 'Joseph Landsberg': [['MATH220', 'MATH411', 'MATH423'], 1.9, 4.5, 20], 'David Larson': [['255', 'BUS205', 'BUS245', 'BUS255', 'BUSINESSSTAT', 'BUSN255', 'BUSSTAT', 'ECO216', 'MACROECONOMICS', 'STAT', 'STATISTICS', 'STATS', 'STATS2'], 2.6, 2.3, None], 'Jong Lee': [['10525', 'C2444', 'COLLALG101', 'MATH101', 'MATH10530', 'MATH208', 'MATH20804231', 'MATH32932', 'MATH62436'], 3.6, 3.9, 100], 'Sang Lee': [['SCKW170', 'SCWK121', 'SCWK140', 'SCWK170', 'SW110', 'SW170'], 4.3, 2.5, 83.3333], 'Chun-Hung Liu': [['ECE3423', 'ECE4813'], 3.4, 4.3, 100], 'Wencai Liu': [['2A', '3A', 'MATH121A', 'MATH2A', 'MATH2B', 'MATH3A', 'MATH44110'], 4.5, 3.1, 87.0968], 'Xin Liu': [['193A', 'CSE15', 'ECS015', 'ECS15', 'ECS152A', 'ECS193AB', 'ECS289I'], 2.6, 3.3, 50], 'Bret Lockhart': [['MATH140', 'MATH142', 'MATH150', 'MATH151', 'MATH152', 'MTH140'], 5, 4, 66.4671], 'Jonas Luhrmann': [['MATH412'], 5, 1, 100], 'Benjamin Lynch': [['MATH150', 'MATH151', 'MATH151H', 'MATH152', 'MATH304', 'MATH308'], 4, 3, 86.2069], 'Matthias Maier': [['MATH5485', 'MATH639'], 5, 3.5, 100], 'David Manuel': [['151521', '171', 'CALC152', 'MATH131', 'MATH140', 'MATH142', 'MATH147', 'MATH148', 'MATH151', 'MATH152', 'MATH166', 'MATH168', 'MATH171', 'MATH172', 'MATH308'], 5, 3.9, 84.4444], 'Riad Masri': [['MATH151', 'MATH300', 'MATH304', 'MATH323', 'MATH323H', 'MATH407'], 3.5, 4, 62.069], 'Laura Matusevich': [['MATH171', 'MATH172', 'MATH304'], 2.9, 4, 55.5556], 'Francis Narcowich': [['MATH414', 'MATH601'], 2.8, 4, "n/a"], 'Volodymyr Nekrashevych': [['MATH304', 'MATH308', 'MATH416', 'MATH647'], 2.4, 3.6, 25], 'Constantin Onica': [['167', 'MATH142', 'MATH150', 'MATH151', 'MATH152', 'MATH166', 'MATH167', 'MATH308'], 3.9, 3.5, 77.2277], 'Patrick Orchard': [['MATH140', 'MATH141', 'MATH142', 'MATH506'], 5, 4.4, 62.6437], 'Grigoris Paouris': [['MATH308', 'MATH323'], 1.3, 4.7, None], 'Matthew Papanikolas': [['MATH172', 'MATH172H', 'MATH221', 'MATH251'], 3.8, 3.9, 100], 'Gregory Pearlstein': [['221', 'MATH221'], 2.5, 3.9, 14.2857], 'Rosanna Pearlstein': [['151', '545', 'CALCULUS3', 'MATH141', 'MATH151', 'MATH152', 'MATH221', 'MATH251'], 2.3, 4, 36.5217], 'Guergana Petrova': [['MATH308', 'MATH414', 'MATH417'], 3.6, 3.8, 57.1429], 'Bojan Popov': [['MATH304', 'MATH308'], 2.3, 4.3, 50], 'Robert Rahm': [['MATH140', 'MATH151', 'MATH152', 'MATH172', 'MATH221', 'MATH251', 'MATH304', 'MATH308', 'MATH412', 'MATH603'], 3.3, 3.5, 68.75], 'Kumbakonam Rajagopal': [['MEEN305'], 1.8, 4.8, 100], 'Heather Ramsey': [['147', 'MATH141', 'MATH147', 'MATH148', 'MATH150', 'MATH166', 'math171', 'MATH325', 'MATH419', 'SCEN289'], 5, 3.4, 91.1111], 'Kamran Reihani': [['12132', '141', 'MATH141', 'MATH151', 'MATH151H', 'MATH152', 'MATH251', 'MATH308', 'MATH401', 'MATH409', 'MATH411', 'MATH411MATH409', 'MATH412'], 2.5, 4.4, 28.5714], 'J. Rojas': [['1211L', '750B', 'CHEM121', 'CHEM122', 'CHEM122LAB'], 4.7, 3.4, 93.75], 'Eric Rowell': [['152', 'MES152', 'MES153'], 1.5, 4.7, 13.5135], 'William Rundell': [['MATH171H', 'MATH300H', 'MATH308H', 'MATH311', 'MATH407', 'MATH409', 'MATH470', 'MATH471', 'MATH472'], 1.8, 5, 50], 'Vince Schielack': [['MATH366', 'MATH367', 'MATH375', 'MATH467'], 2.5, 3.5, 23.0769], 'Thomas Schlumprecht': [['172', '172504', 'MATH151', 'MATH171', 'MATH171502', 'MATH171503', 'MATH172', 'MATH308', 'MATH409', 'MATH503'], 3.8, 4, 80.7692], 'Todd Schrader': [['CALC152', 'MAT151', 'MATH140', 'MATH150', 'MATH151', 'MATH152', 'MATH171', 'MATH251'], 4.7, 2.8, 95.3191], 'Sinjini Sengupta': [['151', 'MATH131', 'MATH140', 'MATH141', 'MATH150', 'MATH151', 'MATH152', 'MATH251', 'MATH252'], 5, 3.6, 88.1657], 'Oksana Shatalov': [['MATH171', 'MATH172', 'MATH220', 'MATH221', 'MATH300', 'MATH689'], 4.2, 3.6, 94.1176], 'Anne Shiu': [['MATH147', 'MATH220', 'MATH300', 'MATH415'], 3.8, 4.4, 60], 'John Slattery': [['ECO2013', 'ECO2023', 'ECONMACR'], 3.8, 2.4, 61.5385], 'Roger Smith': [['MATH171', 'MATH172', 'MATH304', 'MATH308', 'MATH407', 'MATH411'], 4, 3.5, 74], 'Frank Sottile': [['MAT707', 'MATH151', 'MATH171', 'MATH220', 'MATH300'], 2.5, 4.6, 20], 'Peter Stiller': [['MATH304', 'MATH427', 'MATH470'], 3, 4, 40], 'Emil Straube': [['MATH171', 'MATH308', 'MATH618', 'MATH650'], 2.8, 2.9, 25], 'Steven Taliaferro': [['308', 'MATH308', 'MATH601'], 2.8, 4.5, 50], 'Kyle Thicke': [['MATH251', 'MATH308'], 5, 3, 100], 'Minh-Binh Tran': [['CS421', 'MATH319', 'MATH421'], 3.7, 4, 55.5556], 'Jessica Tripode': [['MATH140', 'MATH142', 'MATH147', 'MATH150', 'MATH167'], 5, 3.6, 86.2069], 'Mariya Vorobets': [['142', '152', 'CALC151', 'CALC2', 'CALC221', 'MATH142', 'MATH151', 'MATH152', 'MATH152H', 'MATH172', 'MATH221', 'MATH251', 'MATH308'], 4.4, 4, 75.641], 'Yaroslav Vorobets': [['MATH304', 'MATH311', 'MATH323', 'MATH409', 'MATH415', 'MATH433'], 3.8, 3.1, 86.6667], 'Kun Wang': [['CHEM', 'CHEM233', 'CHEM235', 'CHEM339', 'CHEMM322'], 3.3, 3.4, 42.8571], 'John Weeks': [['409', 'GEOG102', 'GEOG385', 'GEOG573', 'HILD2CUCSD', 'HIST109', 'HIST409', 'HIST409410', 'HIST410', 'HIST411', 'HIST413', 'HIST440', 'HISTORY410', 'HISTORY411', 'HISTORY413', 'HST413', 'USHISTORY'], 3.8, 2.8, 100], 'Jennifer Whitfield': [['MATH140', 'MATH142', 'MATH147', 'MATH151', 'MATH171', 'MATHH142'], 5.3, 3.5, 82.3529], 'Michael Willis': [['INTROTOSOC', 'MINOR3203', 'SOC20113203', 'SOC3203'], 3.7, 2.5, 33.3333], 'Sarah Witherspoon': [['171', '415', 'MATH171', 'MATH172', 'MATH172H', 'MATH220', 'MATH365', 'MATH415', 'MAYH171'], 3.8, 3.1, 62.5], 'Stephan Wojtowytsch': [['CALC120', 'math410'], 1.5, 2, None], 'Guangbo Xu': [['MATH308'], 5, 2, 100], 'Catherine Yan': [['BIOCHEM', 'BIOCHEMISTRY', 'CHEM0741', 'CHEM07560'], 1.1, 3.8, None], 'Tian Yang': [['MATH221', 'MATH304', 'MATH308', 'MATH323'], 5, 3.6, 95.6522], 'Philip Yasskin': [['151', '311', 'MATH151', 'MATH152', 'MATH171', 'MATH172', 'MATH172H', 'MATH221', 'MATH221H', 'MATH251', 'MATH253', 'MATH311'], 2.3, 4, 37.2093], 'Matthew Young': [['ME366', 'ME466'], 4.1, 3.1, 100], 'Igor Zelenko': [['MATH251', 'MATH308', 'MATH439', 'MATH622'], 3.6, 3.4, 80], 'Jianxin Zhou': [['MATH304', 'MATH308', 'MATH311'], 2.8, 4.9, 47.3684]}

    ecenDict = {'Shankar Bhattacharyya': [['ECEN420'], 5, 2.4, 100], 'Adam Birchfield': [['ECEN214', 'ECEN460'], 4.1, 2.9, 87.5], 'Ulisses Braga-Neto': [['ECEN214', 'ECEN215', 'ECEN303', 'ECEN649', 'ECEN689', 'MSEN660'], 3.4, 3.8, 83.3333], 'Karen Butler-Purry': [[], 0, 0, -1], 'Jean-Francois Chamberland': [['ECEN303', 'ECEN601', 'ECEN662', 'ECEN689', 'ENGR289'], 2.9, 3.9, 42.8571], 'Gwan Choi': [['ECEN248', 'ECEN454', 'ECEN714'], 2, 3.5, 31.25], 'Aniruddha Datta': [['ECEN214', 'ECEN419', 'ECEN420', 'ECEN609', 'ELN420'], 4.3, 3.3, 83.3333], 'Katherine Davis': [['ECEN214', 'ECEN340', 'ECEN460'], 3, 3, 67], 'Nick Duffield': [['ECEN689', 'ECEN758'], 4.5, 2, 100], 'Mehrdad Ehsani': [['ECEN441', 'ECEN442', 'ECEN686', 'ENG111'], 3.9, 2.3, 75], 'Kamran Entesari': [['ECEN322', 'ECEN325', 'ECEN625', 'ECEN665', 'MMIC'], 3.8, 3.6, 87.5], 'Paul Gratz': [['ECEN350', 'ECEN449'], 5, 3.4, 100], 'Arum Han': [[], 0, 0, -1], 'Rusty Harris': [['ECEN215', 'ECEN315', 'ECEN370', 'ECEN472', 'ECEN473'], 1.5, 4.3, 10], 'Philip Hemmer': [['ECEN214', 'ECEN370'], 2.1, 4.1, 100], 'I-Hong Hou': [['ECEN248', 'ECEN424', 'ECEN757'], 4, 4, 100], 'Sebastian Hoyos': [['ECEN325', 'ECEN474', 'ECEN610'], 2.3, 3.2, 40], 'Marco Iskander': [['ECEN214', 'ECEN215'], 5, 3, 100], 'Jim Ji': [['ECEN314', 'ECEN410'], 5, 2.5, 100], 'Stavros Kalafatis': [['ECEN403'], 4.5, 3, 100], 'Dileep Kalathil': [['ECEN303', 'ECEN689'], 2.8, 4.3, 50], 'Aydin Karsilayan': [['ECEN214', 'ECEN325', 'ECEN326', 'ECEN704'], 2.8, 5, 38.8889], 'Linda Katehi': [['130A', 'ECEN322H', 'EEC130', 'EEC130A', 'ENG100'], 3.5, 2.5, 72.7273], 'Mladen Kezunovic': [['ECEN666'], 1, 1, None], 'Sunil Khatri': [['ECEN449'], 3.1, 4.6, 33.3333], 'Soaram Kim': [['ECEN215'], 4, 2, 100], 'Laszlo Kish': [['ECEN461', 'ECEN489', 'ECEN658', 'ECEN771'], 4.8, 1.8, 100], 'Panganamala Kumar': [['ECEN434'], 5, 3, 100], 'Pao-Tai Lin': [['ECEN314', 'ECEN491'], 2.3, 3.8, 25], 'Tie Liu': [['ECEN303', 'ECEN314', 'ECEN434'], 4.7, 3.1, 100], 'Mi Lu': [['ECEN248', 'ECEN350', 'ECEN651'], 2.6, 3.9, 58], 'John Lusher': [['ECEN215', 'ECEN350', 'ECEN403'], 4.9, 3.5, 95], 'Christi Madsen': [['102', 'LCD306'], 3.3, 3, None], 'Krzysztof Michalski': [['ECEN322', 'ECEN445'], 1.3, 4, 25], 'Scott Miller': [['DEP', 'DEP3053', 'DEP3503', 'DEP3533', 'DEP4704', 'DEV', 'PSY'], 3.1, 3.3, -1], 'Oscar Moreira': [['ECEN214', 'ECEN215', 'ECEN325', 'ECEN350', 'ECEN607'], 3, 4.6, 48], 'Krishna Narayanan': [['COSC111', 'COSC211', 'COSC314', 'COSC471', 'COSC472', 'COSC481'], 3.8, 3.8, 50], 'Robert Nevels': [['ECEN322', 'ECEN445'], 3.1, 4, 63.6364], 'Sam Palermo': [['ECEN325', 'ECEN720'], 4.6, 2.4, 100], 'Xiaofeng Qian': [['MEEN222', 'MSEN325', 'MSEN691'], 3.3, 3.4, 50], 'Xiaoning Qian': [['ECEN303', 'ECEN333', 'ECEN765', 'MEEN222'], 4.3, 3.6, 90.9091], 'Michael Quinn': [['160', 'BUS160', 'COB202', 'GBUS', 'GBUS100', 'GBUS101', 'GBUS106', 'GBUS120', 'GBUS160', 'GBUS160B', 'GBUS180', 'GBUS210', 'GBUSA', 'GBUSGBUS', 'GUBS160', 'HTM298', 'HTM298DISNEY', 'MKTG382'], 3.3, 3.1, -1], 'Mina Rahimian': [['ECEN215'], 3.6, 3.5, 76.1905], 'Jeyavijayan Rajendran': [['ECEN248', 'ECEN426'], 4.9, 3.1, 90], 'Peter Rentzepis': [['1B', 'CHEM01', 'CHEM1', 'CHEM101', 'CHEM130B', 'CHEM131', 'CHEM131A', 'CHEM153', 'CHEM1A', 'CHEM1B', 'CHEM1P', 'CHEMGEN', 'CHEMISTRY1B', 'CLASSSECT', 'HSLH100', 'PHYSCHEM'], 1.9, 4.2, 100], 'Raffaella Righetti': [['ECEN314', 'ECEN412'], 4.9, 2.9, 100], 'B. Russell': [['HEALT011', 'HEALT11', 'HEALT3054', 'HEALTH', 'HEALTH08', 'HEALTH11', 'HELTH11', 'HLTH11'], 4.7, 1.1, -1], 'Serap Savari': [['ECEN303', 'ECEN455', 'ECEN646'], 2, 5, 37.5], 'Srinivas Shakkottai': [['ECEN424', 'ECEN750'], 4.6, 3.3, 100], 'Yang Shen': [['ENG1500', 'ENGG1500'], 2, 4.3, 36.3636], 'Weiping Shi': [['ECEN248'], 1.8, 4.4, 16.6667], 'Jose Silva-Martinez': [['ECEN325', 'ECEN489', 'ECEN610', 'ECEN620'], 3.4, 3.8, 72.7273], 'Alex Sprintson': [['ECEN248', 'ECEN350'], 3.6, 3.3, 66.6667], 'Chao Tian': [['304864', 'MATH231', 'MATH251'], 2.4, 4, -1], 'Hamid Toliyat': [['ECEN214'], 2.8, 3.3, 60], 'John Tyler': [['314', 'ECEN214', 'ECEN215', 'ECEN248', 'ECEN322', 'ECEN325', 'ELEN214', 'ELEN215'], 4.3, 3.3, 79.3103], 'Karan Watson': [['ECEN248'], 5, 2.7, 100], 'Mark Weichold': [['ECEN370'], 2.4, 4.9, 100], 'R. Williams': [['ANY1', 'BIO109', 'BIO119', 'OCEAN119', 'SCI000', 'SCI101', 'SCI102', 'SCI109', 'SCI109102', 'SCI110', 'SCI119'], 4.5, 2.8, -1], 'Steven Wright': [['103I', '103I43', 'MA043', 'MAI', 'MATH', 'MATH040', 'MATH103', 'MATH103I', 'MATH103IMATH43', 'MATH43', 'MATH43103I', 'STAT108'], 4.6, 1.6, 66.6667], 'Le Xie': [['CS232', 'CS49371', 'CSCI49371'], 3, 3.4, None], 'Zixiang Xiong': [['ECEN314'], 1, 5, None], 'Suin Yi': [['ECEN-248'], 4.9, 3, 100], 'Byung-Jun Yoon': [['ECEN314'], 5, 3, 100], 'Xi Zhang': [['ECEN423', 'ECEN619'], 2.1, 1, 50], 'Jun Zou': [['420AT2UM', '420MNAUM', '420TL6UM', 'BARF1901', 'DATABASE123', 'IN123'], 4.5, 2.1, 100]}


    #Not found on rate my professor : ['Marcus Botacin', 'Victoria Crawford', 'Juan Garay', 'Dezhen Song', 'Chia-Che Tsai']
    global profsThatTeach
    profsThatTeach = []

    #department = input("Enter the course department (ex: CSCE, MATH, etc.): ")
    if department == "CSCE":
        for i in csceDict:
            #print(i)

            courseList = csceDict[i][0]
            #print(courseList)
            rating = csceDict[i][1]
            difficulty = csceDict[i][2]
            wouldTakeAgain = csceDict[i][3]

            for j in courseList: #adds prof to list if they teach the course
                    if j == courseName:
                        profsThatTeach.append(i + f" | Rating: {rating} / 5.0" + f" | Difficulty: {difficulty} / 5.0" + f" | Would Take Again: {wouldTakeAgain}%<br>")
                    else:
                        continue
    elif department == "MATH":
        for i in mathDict:
            #print(i)

            courseList = mathDict[i][0]
            #print(courseList)
            rating = mathDict[i][1]
            difficulty = mathDict[i][2]
            wouldTakeAgain = mathDict[i][3]

            for j in courseList: #adds prof to list if they teach the course
                    if j == courseName:
                        profsThatTeach.append(i + f" | Rating: {rating} / 5.0" + f" | Difficulty: {difficulty} / 5.0" + f" | Would Take Again: {wouldTakeAgain}%<br>")
                    else:
                        continue
    
    answer = ""
    for i in profsThatTeach:
         answer+=(i+"<br>")
    if answer == "":
        return f'<p style="font-family: sans-serif;">"No results found"</p>'
    
    else:
        return f'<p style="font-family: sans-serif;">{answer}</p>'


@app.route('/bug-report', methods=['GET', 'POST'])
def bugReport():
    if request.method == 'GET':
        return render_template('bug_report.html')

    # code here executes when we make a HTTP POST request
    # essentially when we click on the 'submit' button

    # identifying our values by department (department field in input element)
    bugReport = request.form.get('bugReport')
    dateToday = str(date.today())


    if bugReport != "":
       with open('mysite//Bugs.csv', 'a') as f:
            f.write(f"\n{dateToday},{bugReport}")
       return f'<p style="font-family: sans-serif;">Bug reported</p>'
    
if __name__ == '__main__':
    app.run()