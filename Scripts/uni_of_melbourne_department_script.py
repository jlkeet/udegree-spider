with open("../udegreeScraper/data/courses/uni_of_melbourne.json", "r+") as file:
    lines = file.readlines()
    wanted = ['"title": "ACCT',
              '"title": "ACTL',
              '"title": "ADMX',
              '"title": "AGRI',
              '"title": "ANAT',
              '"title": "ANCW',
              '"title": "ANSC',
              '"title": "ANTH',
              '"title": "ARBC',
              '"title": "ARCH',
              '"title": "ACUR',
              '"title": "AHIS',
              '"title": "ARTS',
              '"title": "AMGT',
              '"title": "ASIA',
              '"title": "ATOC',
              '"title": "AUDI',
              '"title": "AIND',
              '"title": "AUST',
              '"title": "BCMB',
              '"title": "BINF',
              '"title": "BIOL',
              '"title": "BMEN',
              '"title": "BMSC',
              '"title": "BIOM',
              '"title": "BIEN',
              '"title": "BTCH',
              '"title": "BOTA',
              '"title": "BUSA',
              '"title": "BISY',
              '"title": "BLAW',
              '"title": "CEDB',
              '"title": "CHEN',
              '"title": "CHEM',
              '"title": "CHIN',
              '"title": "CICU',
              '"title": "CVEN',
              '"title": "CLAS',
              '"title": "CLRS',
              '"title": "CMCE',
              '"title": "CCDP',
              '"title": "COMP',
              '"title": "CONS',
              '"title": "CREA',
              '"title": "CWRI',
              '"title": "CRIM',
              '"title": "XNTS',
              '"title": "CUMC',
              '"title": "CULS',
              '"title": "DNCE',
              '"title": "DENT',
              '"title": "DESN',
              '"title": "DPSS',
              '"title": "DEVT',
              '"title": "DASC',
              '"title": "DRAM',
              '"title": "ERTH',
              '"title": "ECOL',
              '"title": "ECOM',
              '"title": "ECON',
              '"title": "EDUC',
              '"title": "ELEN',
              '"title": "ENGR',
              '"title": "ENGM',
              '"title": "ENGL',
              '"title": "ESLA',
              '"title": "ENEN',
              '"title": "EVSC',
              '"title": "ENST',
              '"title": "ENVS',
              '"title": "EURO',
              '"title": "EXCH',
              '"title": "FLTV',
              '"title": "FNCE',
              '"title": "FINA',
              '"title": "FOOD',
              '"title": "FRST',
              '"title": "FREN',
              '"title": "GEND',
              '"title": "GENP',
              '"title": "GENE',
              '"title": "GEOG',
              '"title": "GEOL',
              '"title": "GEOM',
              '"title": "GERM',
              '"title": "GDES',
              '"title": "HLTH',
              '"title": "HEBR',
              '"title": "HIST',
              '"title": "HPSC',
              '"title": "HORT',
              '"title": "NUTR',
              '"title": "INAM',
              '"title": "INDG',
              '"title": "INDO',
              '"title": "INFO',
              '"title": "ISYS',
              '"title": "IBUS',
              '"title": "INHL',
              '"title": "INTS',
              '"title": "ISLM',
              '"title": "ITAL',
              '"title": "JAPN',
              '"title": "JEWI',
              '"title": "JOUR',
              '"title": "KORE',
              '"title": "LARC',
              '"title": "LANG',
              '"title": "LTAM',
              '"title": "LAWS',
              '"title": "LING',
              '"title": "MGMT',
              '"title": "MFEN',
              '"title": "MKTG',
              '"title": "MREN',
              '"title": "MAST',
              '"title": "MCEN',
              '"title": "MECM',
              '"title": "MEED',
              '"title": "MEDI',
              '"title": "MEDS',
              '"title": "MIIM',
              '"title": "MGRK',
              '"title": "MULT',
              '"title": "MUSI',
              '"title": "MUST',
              '"title": "NRMT',
              '"title": "NEUR',
              '"title": "NURS',
              '"title": "OBGY',
              '"title": "OPHT',
              '"title": "OPTO',
              '"title": "ORAL',
              '"title": "OTOL',
              '"title": "PAED',
              '"title": "PATH',
              '"title": "PERF',
              '"title": "PHRM',
              '"title": "PHIL',
              '"title": "PHYC',
              '"title": "PHYS',
              '"title": "PHTY',
              '"title": "PLAN',
              '"title": "POLS',
              '"title": "POPH',
              '"title": "PROP',
              '"title": "PSYT',
              '"title": "PSYC',
              '"title": "PADM',
              '"title": "PPMN',
              '"title": "PUBL',
              '"title": "RADI',
              '"title": "REHB',
              '"title": "RURA',
              '"title": "RUSS',
              '"title": "SCIE',
              '"title": "SINF',
              '"title": "SCRN',
              '"title": "SKIL',
              '"title": "SOTH',
              '"title": "SCWK',
              '"title": "SOLS',
              '"title": "SOCI',
              '"title": "SWEN',
              '"title": "SPAN',
              '"title": "SMED',
              '"title": "STDY',
              '"title": "SURG',
              '"title": "SWED',
              '"title": "THTR',
              '"title": "THEO',
              '"title": "TRAN',
              '"title": "UNIB',
              '"title": "URBD',
              '"title": "VETS',
              '"title": "VISM',
              '"title": "WELF',
              '"title": "WOHT',
              '"title": "ZOOL']

    replacement = [
        "Accounting",
        "Actuarial Studies",
        "Administrative",
        "Agriculture",
        "Anatomy",
        "Ancient World Studies",
        "Animal Science",
        "Anthropology",
        "Arabic",
        "Architecture",
        "Art Curatorship",
        "Art History",
        "Arts",
        "Arts Management",
        "Asian Studies",
        "Atmosphere and Ocean Sciences",
        "Audiology",
        "Australian Indigenous Studies",
        "Australian Studies",
        "Biochemistry and Molecular Biology",
        "Bioinformatics",
        "Biology",
        "Biomedical Engineering",
        "Biomedical Science",
        "Biomedicine",
        "Biomolecular Engineering",
        "Biotechnology",
        "Botany",
        "Business Administration",
        "Business Information Systems",
        "Business Law",
        "Cell and Developmental Biology",
        "Chemical Engineering",
        "Chemistry",
        "Chinese",
        "Cinema and Cultural Studies",
        "Civil Engineering",
        "Classics",
        "Clinical Research",
        "Commerce",
        "Community Cultural Development Practice",
        "Computer Science",
        "Construction",
        "Creative Arts",
        "Creative Writing",
        "Criminology",
        "Cross - institutional",
        "Cultural Materials Conservation",
        "Cultural Studies",
        "Dance",
        "Dentistry",
        "Design",
        "Design\ u0026 Prod",
        "Development Studies",
        "Domestic Animal Science",
        "Drama",
        "Earth Sciences",
        "Ecology",
        "Econometrics",
        "Economics",
        "Education",
        "Electrical Engineering",
        "Engineering",
        "Engineering Management",
        "English",
        "English as a Second Language",
        "Environmental Engineering",
        "Environmental Science",
        "Environmental Studies",
        "Environments",
        "European Studies",
        "Exchange",
        "Film and Television",
        "Finance",
        "Fine Art",
        "Food Science",
        "Forest Science",
        "French",
        "Gender Studies",
        "General Practice",
        "Genetics",
        "Geography",
        "Geology",
        "Geomatics",
        "German",
        "Graphic Design",
        "Health",
        "Hebrew",
        "History",
        "History and Philosophy of Science",
        "Horticulture",
        "Human Nutrition",
        "Indigenous Arts Management",
        "Indigenous Studies",
        "Indonesian",
        "Informatics",
        "Information Systems",
        "International Business",
        "International Health",
        "International Studies",
        "Islamic Studies",
        "Italian",
        "Japanese",
        "Jewish Studies",
        "Journalism",
        "Korean Studies",
        "Landscape Architecture",
        "Language",
        "Latin American Studies",
        "Law",
        "Linguistics and Applied Linguistics",
        "Management",
        "Manufacturing Engineering",
        "Marketing",
        "Materials Engineering",
        "Mathematics and Statistics",
        "Mechanical Engineering",
        "Media and Communications",
        "Medical Education",
        "Medicine",
        "Medicine / Surgery",
        "Microbiology and Immunology",
        "Modern Greek",
        "Multidisciplinary subject",
        "Music",
        "Music Theatre",
        "Natural Resource Management",
        "Neuroscience",
        "Nursing Science",
        "Obstetrics\ u0026 Gynaecology",
        "Ophthalmology",
        "Optometry and Vision Sciences",
        "Oral Health",
        "Otolaryngology",
        "Paediatrics",
        "Pathology",
        "Performing Arts",
        "Pharmacology",
        "Philosophy",
        "Physics",
        "Physiology",
        "Physiotherapy",
        "Planning",
        "Political Science",
        "Population Health",
        "Property",
        "Psychiatry",
        "Psychology",
        "Public Administration",
        "Public Policy and Management",
        "Publishing",
        "Radiology",
        "Rehabilitation Therapy",
        "Rural Health",
        "Russian",
        "Science",
        "Science Informatics",
        "Screen Studies",
        "Skills",
        "Social Theory",
        "Social Work",
        "Socio - Legal Studies",
        "Sociology",
        "Software Engineering",
        "Spanish and Latin American Studies",
        "Sports Medicine",
        "Study Abroad",
        "Surgery",
        "Swedish",
        "Theatre Studies",
        "Theology",
        "Translation and Interpretation",
        "University Breadth",
        "Urban Design",
        "Veterinary Science",
        "Visual Media",
        "Welfare Studies",
        "Women 's Health",
        "Zoology"]
    # this will put the seek pointer to the end of file
    file.seek(0, 2)
    maxcount=len(lines)
    count = 0

    for text in lines:
        file.write(text)
        for x in wanted:
            if x in text:
                new_line = '        "department": ' + '"' + replacement[wanted.index(x)] + '",'
                file.write(new_line + "\n")
    file.close()