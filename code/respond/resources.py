resources = [
    {
        "name": "clinic",
        "keywords": (
            "clinic doctor nurse practitioner office sick ill illness vomiting pain flu influenza injury injured wounded",
        ),
        "phrase": ("a medical clinic",),
        "options": ("What kind of clinic are you needing?",),
        "children": (
            {
                "name": "urgent-care",
                "keywords": ("urgent-care urgent walk-in",),
                "phrase": ("an urgent-care clinic",),
                "children": [
                    {
                        "name": "northwest urgent-care",
                        "keywords": ("1 Northwest",),
                        "info": ({
                            "Address": "3271 E US 412 Hwy",
                            "Phone": "479-215-3080",
                            "Location": "Near Lowes on 412",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Northwest Urgent Care",),
                    }
                ]
            },
            {
                "name": "primary-care",
                "keywords": ("primary-care primary family-care family-practice",),
                "phrase": ("a primary-care clinic",),
                "children": [
                    {
                        "name": "Community Clinic",
                        "keywords": ("1 Community",),
                        "info": ({
                            "For": "Kids + Adults",
                            "Phone": "500 S Mt Olive",
                            "Address": "855-438-2280",
                            "Location": "Across from library",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Community Clinic",),
                    },
                    {
                        "name": "Panther Clinic",
                        "keywords": ("2 Panther",),
                        "info": ({
                            "For": "Kids + Adults",
                            "Phone": "479-524-8175",
                            "Address": "1500 N Mt Olive",
                            "Location": "In Intermediate School",
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Panther Clinic",),
                    },
                ]
            },
            {
                "name": "pediatric-care",
                "keywords": ("pediatrician pediatric child",),
                "phrase": ("a children's clinic",),
                "children": [
                    {
                        "name": "Panther Clinic",
                        "keywords": ("1 Panther",),
                        "info": ({
                            "For": "Children + Adults",
                            "Phone": "479-524-8175",
                            "Address": "1500 N Mt Olive",
                            "Location": "In Intermediate School",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Panther Clinic",),
                    },
                    {
                        "name": "Sager Creek",
                        "keywords": ("2 Sager Creek",),
                        "info": ({
                             "For": "Children",
                             "Phone": "479-549-4228",
                             "Address": "1101-2 N Progress Ave",
                             "Location": "Near hospital",
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Sager Creek",),
                    }
                ]
            },
            {
                "name": "vaccines",
                "keywords": ("vaccine vaccination immunization immunize shot",),
                "phrase": ("a vaccination clinic",),
                "children": [
                    {
                        "name": "Public Health",
                        "keywords": ("1 Public",),
                        "info": ({
                            "Phone": "479-549-3790",
                            "Address": "101 W University St",
                            "Location": "Downtown Siloam",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Public Health",),
                    },
                    {
                        "name": "Panther Clinic",
                        "keywords": ("2 Panther",),
                        "info": ({
                            "Phone": "479-524-8175",
                            "Address": "1500 N Mt Olive",
                            "Location": "In Intermediate School",
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Panther Clinic",),
                    },
                    {
                        "name": "Community Clinic",
                        "keywords": ("3 Community",),
                        "info": ({
                            "Phone": "500 S Mt Olive",
                            "Address": "855-438-2280",
                            "Location": "Across from library",
                        },),
                        "isLeaf": True,
                        "phrase": ("3.Community Clinic",),
                    },
                ],
            },
        )
    },
    {
        "name": "emergency",
        "keywords": (
            "hospital emergency murder murdering murdered shoot shooting shot gun kill killing killed wreck crash crashed crashing kidnap kidnapped kidnapping abduct abducted abducting blood bleeding",
        ),
        "phrase": ("emergency help",),
        "children": (
            {
                "name": "911",
                "keywords": ("1 911 emergency",),
                "info": ({
                    "phone": "911",
                    "address": "603 N. Progress Ave",
                    "location": "ER across from Highschool"
                },),
                "isLeaf": True,
                "phrase": ("1.emergency help",),
            },
            {
                "name": "other",
                "keywords": ("2 other",),
                "info": ({
                    "Other options": "try replying 'suicide' or 'abuse'",
                },),
                "isLeaf": True,
                "phrase": ("2.other",),
            },
        )
    },
    {
        "name": "suicide",
        "keywords": ("suicide slit slitting slitted cut cutting death",),
        "phrase": ("urgent help with thoughts of suicide or harm",),
        "children": (
            {
                "name": "911",
                "keywords": ("1 911 emergency",),
                "info": ({
                             "phone": "911",
                             "address": "603 N. Progress Ave",
                             "location": "ER across from Highschool"
                         },),
                "isLeaf": True,
                "phrase": ("1.emergency help",),
            },
            {
                "name": "Suicide Lifeline",
                "keywords": ("2 lifeline",),
                "info": ({
                             "phone": "800-273-8255",
                             "hours": "24/7",
                         },),
                "isLeaf": True,
                "phrase": ("2.suicide lifeline",),
            },
            {
                "name": "Crisis Hotline",
                "keywords": ("3 crisis hotline",),
                "info": ({
                             "phone": "888-274-7472",
                             "hours": "M-F 8am-1am, Sat-Sun 2pm-midnight",
                         },),
                "isLeaf": True,
                "phrase": ("3.crisis hotline",),
            },
        )
    },
    {
        "name": "domestic violence",
        "keywords": ("domestic violence violent abuse hit hitting beat beaten beating bruise bruised bruising punch punched punchin grab grabbed",),
        "phrase": ("urgent help with violence at home",),
        "children": (
            {
                "name": "911",
                "keywords": ("1 911 emergency",),
                "info": ({
                    "phone": "911",
                    "address": "603 N. Progress Ave",
                    "location": "ER across from Highschool"
                },),
                "isLeaf": True,
                "phrase": ("1 emergency help",),
            },
            {
                "name": "Domestic Abuse Hotline",
                "keywords": ("2 hotline",),
                "info": ({
                    "phone": "800-799-7233",
                    "hours": "24/7",
                    "website": "www.thehotline.org/"
                },),
                "isLeaf": True,
                "phrase": ("2 violence hotline",),
            },
            {
                "name": "Child Abuse Hotline",
                "keywords": ("3 abuse hotline",),
                "info": ({
                     "phone": "800-482-5964",
                     "hours": "24/7",
                },),
                "isLeaf": True,
                "phrase": ("3 child abuse hotline",),
            },
        )
    },
    {
        "name": "rehabilitation",
        "keywords": ("rehab rehabilitation recover recovery addict addiction addicted dependent drug alcohol beer wine liquor vodka cocaine crack meth methamphetamine marijuana",),
        "phrase": ("addiction or rehab help",),
        "children": (
            {
                "name": "Teen Rehab",
                "keywords": ("adolescent teen",),
                "phrase": ("a teen rehab",),
                "children": (
                    {
                        "name": "Decision Point",
                        "keywords": ("1 decision point",),
                        "info": ({
                            "Phone": "479-756-1060",
                        },),
                        "isLeaf": True,
                        "phrase": ("1 Decision Point",),
                    },
                )
            },
            {
                "name": "Adult Rehab",
                "keywords": ("adult",),
                "phrase": ("an adult rehab",),
                "children": (
                    {
                        "name": "Decision Point",
                        "keywords": ("1 decision point",),
                        "info": ({
                            "Phone": "479-756-1060",
                        },),
                        "isLeaf": True,
                        "phrase": ("1 Decision Point",),
                    },
                    {
                        "name": "Alcohol and Drug Detox",
                        "keywords": ("2 detox",),
                        "info": ({
                            "Phone": "479-715-4957",
                            "Location": "Fayetteville",
                        },),
                        "isLeaf": True,
                        "phrase": ("2 Alcohol and Drug Detox",),
                    },
                    {
                        "name": "Decision Point",
                        "keywords": ("2 decision point",),
                        "info": ({
                            "Phone": "464-1060",
                            "Location": "Bentonville",
                        },),
                        "isLeaf": True,
                        "phrase": ("2 Alcohol and Drug Detox",),
                    },
                )
            },
            {
                "name": "Men Rehab",
                "keywords": ("men",),
                "phrase": ("a rehab for men",),
                "children": (
                    {
                        "name": "Harbor House",
                        "keywords": ("1 decision point",),
                        "info": ({
                            "Phone": "479-785-4083",
                            "Location": "Fort Smith",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Alcohol and Drug Detox",),
                    },
                )
            }
        )
    },
    {
        "name": "mental health",
        "keywords": ("mental behavioral depressed depressing depression sad grief crying anxiety panic insane crazy nuts nervous nerve breakdown",),
        "phrase": ("a mental health service",),
        "options": ("What kind of service are you needing?",),
        "children": (
            {
                "name": "counselor",
                "keywords": ("counselor behavioral",),
                "phrase": ("a counseling service",),
                "children": [
                    {
                        "name": "JBU Care Clinic",
                        "keywords": ("1 JBU",),
                        "info": ({
                            "phone": "479-524-7300",
                            "address": "2125 W. University Street",
                            "location": "Across from JBU"
                        },),
                        "isLeaf": True,
                        "phrase": ("1.JBU Care Clinic",),
                    },
                    {
                        "name": "Glenhaven Counseling",
                        "keywords": ("2 Glenhaven",),
                        "info": ({
                            "phone": "479-238-3950",
                            "address": "500 S. Broadway",
                            "location": "Across from Library"
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Glenhaven Counseling",),
                    },
                    {
                        "name": "Ozark Guidance",
                        "keywords": ("3 OGC Ozark Guidance",),
                        "info": ({
                            "phone": "479-524-8618",
                            "address": "710 Holly Street",
                            "location": "Across from the Middle School"
                        },),
                        "isLeaf": True,
                        "phrase": ("3.Ozark Guidance",),
                    }
                ]
            },
            {
                "name": "psychiatrist",
                "keywords": ("psychiatry psychiatrist nurse-practitioner",),
                "phrase": ("a psychiatry service",),
                "children": [
                    {
                        "name": "Ozark Guidance",
                        "keywords": ("OGC Ozark Guidance",),
                        "info": ({
                            "phone": "479-524-8618",
                            "address": "710 Holly Street",
                            "location": "Across from the Middle School"
                        },),
                        "isLeaf": True,
                        "phrase": ("Ozark Guidance",),
                    }
                ]
            },
        )
    },
    {
        "name": "food",
        "keywords": ("food meal hungry",),
        "phrase": ("a food service",),
        "options": ("What kind of food help do you need?",),
        "children": (
            {
                "name": "food for children",
                "keywords": ("children",),
                "phrase": ("food for children",),
                "children": [
                    {
                        "name": "WIC",
                        "keywords": ("1 WIC",),
                        "info": ({
                            "Phone": "479-549-3790",
                            "Address": "101 W University St",
                            "Location": "Downtown Siloam",
                        },),
                        "isLeaf": True,
                        "phrase": ("WIC",),
                    },
                    {
                        "name": "Food Stamps/SNAP",
                        "keywords": ("1 stamps SNAP",),
                        "info": ({
                            "Phone": "501-682-8650",
                            "Website": "https://www.benefits.gov/benefit/1108",
                        },),
                        "isLeaf": True,
                        "phrase": ("Food Stamps/SNAP",),
                    },
                    {
                        "name": "Summer Food Program",
                        "keywords": ("2 summer",),
                        "info": ({
                            "Locations": "Allen Elementary 11-1, Bob Henry Park 11:30",
                            "Website": "http://www.fns.usda.gov/summerfoodrocks",
                        },),
                        "isLeaf": True,
                        "phrase": ("Summer Food Program",),
                    },
                ]
            },
            {
                "name": "food pantry",
                "keywords": ("pantry locker bank",),
                "phrase": ("a food pantry",),
                "children": [
                    {
                        "name": "Manna Center",
                        "keywords": ("1 Manna Center",),
                        "info": ({"address": "670 Heritage Ct.", "near": "The intersection of S. Carl and W. Tulsa"},),
                        "isLeaf": True,
                        "phrase": ("1.The Manna Center",),
                    },
                    {
                        "name": "Only Believe",
                        "keywords": ("2 Tabernacle",),
                        "info": ({
                            "Phone": "479-790-3678",
                            "Address": "1700 A South Pointe",
                            "Location": "Off of 59 south of 412",
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Only Believe Tabernacle",),
                    },
                    {
                        "name": "Hunger and Thirst Ministries",
                        "keywords": ("3 thirst ministry",),
                        "info": ({
                            "Phone": "479-373-6220",
                            "Address": "3298 E Kenwood St",
                            "Location": "Off of 16 south of 412",
                        },),
                        "isLeaf": True,
                        "phrase": ("3.Hunger & Thirst",),
                    }
                ]
            },
        )
    },
    {
        "name": "housing",
        "keywords": ("house housing homeless apartment flat evict evicted evicting place room sleep",),
        "phrase": ("housing assistance",),
        "options": ("What kind of housing help do you need?",),
        "children": (
            {
                "name": "rent/hotel assistance",
                "keywords": ("house housing rent renting hotel motel over-night",),
                "phrase": ("rent/hotel assistance",),
                "children": [
                    {
                        "name": "Housing Authority",
                        "keywords": ("1 authority",),
                        "info": ({
                            "Phone": "479-524-8117",
                            "Address": "1255 W Tulsa",
                            "Locations": "Near Middle School",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Housing Authority",),
                    },
                    {
                        "name": "Genesis House",
                        "keywords": ("2 Genesis",),
                        "info": ({
                            "Phone": "479-549-3438",
                            "Address": "1402 N Inglewood",
                            "Locations": "Across from Dollar General on Cheri Whitlock",
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Genesis House",),
                    },
                ]
            },
            {
                "name": "shelter",
                "keywords": ("shelter temporary",),
                "phrase": ("a shelter",),
                "children": [
                    {
                        "name": "general shelter",
                        "keywords": ("general",),
                        "phrase": ("a general shelter",),
                        "children": [
                            {
                                "name": "Salvation Army",
                                "keywords": ("1 Salvation Army",),
                                "info": ({
                                    "Phone": "855-251-0857",
                                    "Location": "Bentonville, Fayetteville",
                                },),
                                "isLeaf": True,
                                "phrase": ("1.Salvation Army",),
                            },
                            {
                                "name": "Havenwood",
                                "keywords": ("1 Havenwood",),
                                "info": ({
                                    "Phone": "479-273-1060",
                                    "For": "single parents",
                                    "Location": "Bentonville",
                                },),
                                "isLeaf": True,
                                "phrase": ("1.Havenwood",),
                            },
                        ]
                    },
{
                        "name": "childrens shelter",
                        "keywords": ("child children boy girl youth baby",),
                        "phrase": ("children's shelter",),
                        "children": [
                            {
                                "name": "NWA Children's Shelter",
                                "keywords": ("1 NWA",),
                                "info": ({
                                    "Phone": "479-795-2417",
                                    "Location": "Bentonville",
                                },),
                                "isLeaf": True,
                                "phrase": ("1.NWA Children's Shelter",),
                            },
                            {
                                "name": "EOA Children's House",
                                "keywords": ("2 EOA",),
                                "info": ({
                                    "Phone": "479-927-1232",
                                    "Location": "Springdale",
                                },),
                                "isLeaf": True,
                                "phrase": ("2.EOA Children's House",),
                            },
                            {
                                "name": "YouthBridge",
                                "keywords": ("3 Bridge",),
                                "info": ({
                                    "Phone": "479-521-1532",
                                    "Location": "Fayetteville",
                                },),
                                "isLeaf": True,
                                "phrase": ("3.Youth Bridge",),
                            },
                        ]
                    },
                    {
                        "name": "womens shelter",
                        "keywords": ("women woman ladies lady",),
                        "phrase": ("women's shelter",),
                        "children": [
                            {
                                "name": "NW Womens Shelter",
                                "keywords": ("1 NW northwest",),
                                "info": ({
                                    "Phone": "800-775-9011",
                                },),
                                "isLeaf": True,
                                "phrase": ("1.NW Women's Shelter",),
                            },
                            {
                                "name": "Restoration Village",
                                "keywords": ("1 Restoration Restore",),
                                "info": ({
                                    "Phone": "479-631-7345",
                                    "For": "women & children",
                                    "Location": "Little Flock",
                                },),
                                "isLeaf": True,
                                "phrase": ("1.Restoration Village",),
                            },
                            {
                                "name": "Oasis of NWA",
                                "keywords": ("2 NW northwest",),
                                "info": ({
                                    "Phone": "479-268-4340",
                                    "For": "women & children",
                                    "Location": "Bentonville",
                                },),
                                "isLeaf": True,
                                "phrase": ("2.Oasis of NWA",),
                            },
                            {
                                "name": "Hannah House",
                                "keywords": ("3 Hannah",),
                                "info": ({
                                    "Phone": "479-782-5683",
                                    "For": "young women",
                                    "Location": "Fort Smith",
                                },),
                                "isLeaf": True,
                                "phrase": ("3.Hannah House",),
                            },
                        ]
                    },
                    {
                        "name": "mens shelter",
                        "keywords": ("men man",),
                        "phrase": ("men shelter",),
                        "children": [
                            {
                                "name": "Souls Harbor",
                                "keywords": ("1 Soul Harbor",),
                                "info": ({
                                    "Phone": "479-631-7878",
                                },),
                                "isLeaf": True,
                                "phrase": ("1.Soul's Harbor",),
                            },
                        ]
                    },
                ]
            },
        )
    },
    {
        "name": "clothing",
        "keywords": ("clothes clothing shirt pants shoe sock coat jacket hat underwear panties bra",),
        "phrase": ("help with clothing",),
        "options": ("What kind are you looking for?",),
        "children": (
            {
                "name": "child clothing",
                "keywords": ("child children boy girl youth baby infant toddler",),
                "phrase": ("child clothing",),
                "children": [
                    {
                        "name": "BrightFutures",
                        "keywords": ("1 Bright Futures Future",),
                        "info": ({
                            "Phone": "479-524-8175",
                            "Address": "1500 N Mt Olive",
                            "Location": "In Intermediate School",
                        },),
                        "isLeaf": True,
                        "phrase": ("1.Bright Futures",),
                    },
                    {
                        "name": "Potter's House",
                        "keywords": ("2 Potter",),
                        "info": ({
                                    "Phone": "479-373-6373",
                                    "Address": "2101 US-412",
                                    "Location": "Across from 2B's Auto",
                                    "For": "all ages"
                        },),
                        "isLeaf": True,
                        "phrase": ("2.Potter's House",),
                    },
                ]
            },
            {
                "name": "adult clothing",
                "keywords": ("adult man woman lady old",),
                "phrase": ("adult clothing",),
                "children": [
                    {
                        "name": "Potter's House",
                        "keywords": ("1 Potter",),
                        "info": ({
                                     "Phone": "479-373-6373",
                                     "Address": "2101 US-412",
                                     "Location": "Across from 2B's Auto",
                                 },),
                        "isLeaf": True,
                        "phrase": ("1.Potter's House",),
                    },
                ]
            },
        )
    },
    {
        "name": "jobs",
        "keywords": ("job work career employ employment employed fired laid",),
        "phrase": ("help finding a job",),
        "options": ("What kind of job help are you looking for?",),
        "children": (
            {
                "name": "Genesis House",
                "keywords": ("1 Genesis",),
                "info": ({
                    "Phone": "479-549-3438",
                    "Address": "1402 N Inglewood",
                    "Locations": "Across from Dollar General on Cheri Whitlock",
                },),
                "isLeaf": True,
                "phrase": ("1.Genesis House",),
            },
            {
                "name": "Goodwill",
                "keywords": ("2 Goodwill",),
                "info": ({
                     "Phone": "479-373-6137",
                     "Address": "1001 S Mt Olive St",
                     "Location": "Corner of 412 & Mt Olive",
                },),
                "isLeaf": True,
                "phrase": ("2.Goodwill",),
            },
        )
    },
    {
        "name": "smoking cessation",
        "keywords": ("smoking smoke smokes smoker vape vaping vaper vapes tobacco",),
        "phrase": ("help stopping tobacco",),
        "options": ("What help with tobacco do you need?",),
        "children": (
            {
                "name": "Tobacco Helpline",
                "keywords": ("1 Helpline",),
                "info": ({
                    "Phone": "833-283-9355",
                },),
                "isLeaf": True,
                "phrase": ("1.Helpline",),
            },
            {
                "name": "SmokefreeTXT",
                "keywords": ("2 Text",),
                "info": ({
                     "Phone": "Text 'Arkansas' 47848",
                },),
                "isLeaf": True,
                "phrase": ("2.Text Program",),
            },
        )
    },
]
