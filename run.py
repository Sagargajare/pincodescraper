import requests
data = { "ANDAMAN & NICOBAR ISLANDS": [
            "Nicobar",
            "North And Middle Andaman",
            "South Andaman"
        ],
        "ANDHRA PRADESH": [
            "Ananthapur",
            "Chittoor",
            "Cuddapah",
            "East Godavari",
            "Guntur",
            "Krishna",
            "Kurnool",
            "Nellore",
            "Prakasam",
            "Srikakulam",
            "Visakhapatnam",
            "Vizianagaram",
            "West Godavari"
        ],
        "ARUNACHAL PRADESH": [
            "Changlang",
            "Dibang Valley",
            "East Kameng",
            "East Siang",
            "Kurung Kumey",
            "Lohit",
            "Lower Dibang Valley",
            "Lower Subansiri",
            "Papum Pare",
            "Tawang",
            "Tirap",
            "Upper Siang",
            "Upper Subansiri",
            "West Kameng",
            "West Siang"
        ],
        "ASSAM": [
            "Barpeta",
            "Bongaigaon",
            "Cachar",
            "Darrang",
            "Dhemaji",
            "Dhubri",
            "Dibrugarh",
            "Goalpara",
            "Golaghat",
            "Hailakandi",
            "Jorhat",
            "Kamrup",
            "Karbi Anglong",
            "Karimganj",
            "Kokrajhar",
            "Lakhimpur",
            "Marigaon",
            "Nagaon",
            "Nalbari",
            "North Cachar Hills",
            "Sibsagar",
            "Sonitpur",
            "Tinsukia"
        ],
        "BIHAR": [
            "Arwal",
            "Banka",
            "Begusarai",
            "Bhagalpur",
            "Bhojpur",
            "Buxar",
            "Darbhanga",
            "East Champaran",
            "Gaya",
            "Jamui",
            "Jehanabad",
            "Kaimur (Bhabua)",
            "Khagaria",
            "Lakhisarai",
            "Madhubani",
            "Munger",
            "Muzaffarpur",
            "Nalanda",
            "Nawada",
            "Patna",
            "Rohtas",
            "Samastipur",
            "Sheikhpura",
            "Sitamarhi",
            "Supaul",
            "Vaishali"
        ],
        "CHANDIGARH": [
            "Chandigarh"
        ],
        "CHATTISGARH": [
            "Bastar",
            "Bijapur(CGH)",
            "Bilaspur(CGH)",
            "Dantewada",
            "Dhamtari",
            "Durg",
            "Gariaband",
            "Janjgir-champa",
            "Jashpur",
            "Kanker",
            "Kawardha",
            "Korba",
            "Koriya",
            "Mahasamund",
            "Narayanpur",
            "Raigarh",
            "Raipur",
            "Rajnandgaon",
            "Surguja"
        ],
        "DAMAN & DIU": [
            "Diu"
        ],
        "DELHI": [
            "Central Delhi",
            "East Delhi",
            "New Delhi",
            "North Delhi",
            "North East Delhi",
            "North West Delhi",
            "South Delhi",
            "South West Delhi",
            "West Delhi"
        ],
        "GOA": [
            "North Goa",
            "South Goa"
        ],
        "GUJARAT": [
            "Ahmedabad",
            "Amreli",
            "Anand",
            "Banaskantha",
            "Bharuch",
            "Bhavnagar",
            "Dahod",
            "Gandhi Nagar",
            "Jamnagar",
            "Junagadh",
            "Kachchh",
            "Kheda",
            "Mahesana",
            "Narmada",
            "Navsari",
            "Panch Mahals",
            "Patan",
            "Porbandar",
            "Rajkot",
            "Sabarkantha",
            "Surat",
            "Surendra Nagar",
            "Tapi",
            "The Dangs",
            "Vadodara"
        ],
        "HIMACHAL PRADESH": [
            "Bilaspur (HP)",
            "Hamirpur(HP)",
            "Kangra",
            "Kinnaur",
            "Kullu",
            "Lahul & Spiti",
            "Mandi",
            "Shimla",
            "Sirmaur",
            "Solan",
            "Una"
        ],
        "JAMMU & KASHMIR": [
            "Ananthnag",
            "Bandipur",
            "Baramulla",
            "Budgam",
            "Doda",
            "Jammu",
            "Kargil",
            "Kathua",
            "Kulgam",
            "Kupwara",
            "Leh",
            "Poonch",
            "Pulwama",
            "Rajauri",
            "Reasi",
            "Shopian",
            "Srinagar",
            "Udhampur"
        ],
        "JHARKHAND": [
            "Bokaro",
            "Chatra",
            "Deoghar",
            "Dhanbad",
            "Dumka",
            "East Singhbhum",
            "Garhwa",
            "Giridh",
            "Godda",
            "Gumla",
            "Hazaribag",
            "Jamtara",
            "Khunti",
            "Koderma",
            "Latehar",
            "Lohardaga",
            "Pakur",
            "Palamau",
            "Ramgarh",
            "Ranchi",
            "Sahibganj",
            "Seraikela-kharsawan",
            "Simdega",
            "West Singhbhum"
        ],
        "KARNATAKA": [
            "Bagalkot",
            "Bangalore",
            "Bangalore Rural",
            "Belgaum",
            "Bellary",
            "Bidar",
            "Bijapur(KAR)",
            "Chamrajnagar",
            "Chickmagalur",
            "Chikkaballapur",
            "Chitradurga",
            "Dakshina Kannada",
            "Davangere",
            "Dharwad",
            "Gadag",
            "Gulbarga",
            "Hassan",
            "Haveri",
            "Kodagu",
            "Kolar",
            "Koppal",
            "Mandya",
            "Mysore",
            "Raichur",
            "Ramanagar",
            "Shimoga",
            "Tumkur",
            "Udupi",
            "Uttara Kannada",
            "Yadgir"
        ],
        "KERALA": [
            "Alappuzha",
            "Ernakulam",
            "Idukki",
            "Kannur",
            "Kasargod",
            "Kollam",
            "Kottayam",
            "Kozhikode",
            "Malappuram",
            "Palakkad",
            "Pathanamthitta",
            "Thiruvananthapuram",
            "Thrissur",
            "Wayanad"
        ],
        "LAKSHADWEEP": [
            "Lakshadweep"
        ],
        "MADHYA PRADESH": [
            "Alirajpur",
            "Anuppur",
            "Ashok Nagar",
            "Balaghat",
            "Barwani",
            "Betul",
            "Bhind",
            "Bhopal",
            "Burhanpur",
            "Chhatarpur",
            "Chhindwara",
            "Damoh",
            "Datia",
            "Dewas",
            "Dhar",
            "Dindori",
            "East Nimar",
            "Guna",
            "Gwalior",
            "Harda",
            "Hoshangabad",
            "Indore",
            "Jabalpur",
            "Jhabua",
            "Katni",
            "Khandwa",
            "Khargone",
            "Mandla",
            "Mandsaur",
            "Morena",
            "Narsinghpur",
            "Neemuch",
            "Panna",
            "Raisen",
            "Rajgarh",
            "Ratlam",
            "Rewa",
            "Sagar",
            "Satna",
            "Sehore",
            "Seoni",
            "Shahdol",
            "Shajapur",
            "Sheopur",
            "Shivpuri",
            "Sidhi",
            "Singrauli",
            "Tikamgarh",
            "Ujjain",
            "Umaria",
            "Vidisha",
            "West Nimar"
        ],
        "MAHARASHTRA": [
            "Ahmed Nagar",
            "Akola",
            "Amravati",
            "Aurangabad",
            "Beed",
            "Bhandara",
            "Buldhana",
            "Chandrapur",
            "Dhule",
            "Gadchiroli",
            "Gondia",
            "Hingoli",
            "Jalgaon",
            "Jalna",
            "Kolhapur",
            "Latur",
            "Mumbai",
            "Nagpur",
            "Nanded",
            "Nandurbar",
            "Nashik",
            "Osmanabad",
            "Parbhani",
            "Pune",
            "Raigarh(MH)",
            "Ratnagiri",
            "Sangli",
            "Satara",
            "Sindhudurg",
            "Solapur",
            "Thane",
            "Wardha",
            "Washim",
            "Yavatmal"
        ],
        "MANIPUR": [
            "Bishnupur",
            "Chandel",
            "Churachandpur",
            "Imphal East",
            "Imphal West",
            "Senapati",
            "Tamenglong",
            "Thoubal",
            "Ukhrul"
        ],
        "MEGHALAYA": [
            "East Garo Hills",
            "East Khasi Hills",
            "Jaintia Hills",
            "Ri Bhoi",
            "South Garo Hills",
            "West Garo Hills",
            "West Khasi Hills"
        ],
        "MIZORAM": [
            "Aizawl",
            "Champhai",
            "Kolasib",
            "Lawngtlai",
            "Lunglei",
            "Mammit",
            "Saiha",
            "Serchhip"
        ],
        "NAGALAND": [
            "Dimapur",
            "Kiphire",
            "Kohima",
            "Longleng",
            "Mokokchung",
            "Mon",
            "Peren",
            "Phek",
            "Tuensang",
            "Wokha",
            "Zunhebotto"
        ],
        "ODISHA": [
            "Angul",
            "Balangir",
            "Baleswar",
            "Bargarh",
            "Bhadrak",
            "Boudh",
            "Cuttack",
            "Debagarh",
            "Dhenkanal",
            "Gajapati",
            "Ganjam",
            "Jagatsinghapur",
            "Jajapur",
            "Jharsuguda",
            "Kalahandi",
            "Kandhamal",
            "Kendrapara",
            "Kendujhar",
            "Khorda",
            "Koraput",
            "Malkangiri",
            "Mayurbhanj",
            "Nabarangapur",
            "Nayagarh",
            "Nuapada",
            "Puri",
            "Rayagada",
            "Sambalpur",
            "Sonapur",
            "Sundergarh"
        ],
        "PONDICHERRY": [
            "Karaikal",
            "Mahe",
            "Pondicherry"
        ],
        "PUNJAB": [
            "Amritsar",
            "Barnala",
            "Bathinda",
            "Faridkot",
            "Fatehgarh Sahib",
            "Fazilka",
            "Firozpur",
            "Gurdaspur",
            "Hoshiarpur",
            "Jalandhar",
            "Kapurthala",
            "Ludhiana",
            "Mansa",
            "Moga",
            "Mohali",
            "Muktsar",
            "Nawanshahr",
            "Pathankot",
            "Patiala",
            "Ropar",
            "Rupnagar",
            "Sangrur",
            "Tarn Taran"
        ],
        "RAJASTHAN": [
            "Ajmer",
            "Alwar",
            "Banswara",
            "Baran",
            "Barmer",
            "Bharatpur",
            "Bhilwara",
            "Bikaner",
            "Bundi",
            "Chittorgarh",
            "Churu",
            "Dausa",
            "Dholpur",
            "Dungarpur",
            "Ganganagar",
            "Hanumangarh",
            "Jaipur",
            "Jaisalmer",
            "Jalor",
            "Jhalawar",
            "Jhujhunu",
            "Jodhpur",
            "Karauli",
            "Kota",
            "Nagaur",
            "Pali",
            "Rajsamand",
            "Sawai Madhopur",
            "Sikar",
            "Sirohi",
            "Tonk",
            "Udaipur"
        ],
        "SIKKIM": [
            "East Sikkim",
            "North Sikkim",
            "South Sikkim",
            "West Sikkim"
        ],
        "TAMIL NADU": [
            "Ariyalur",
            "Chennai",
            "Coimbatore",
            "Cuddalore",
            "Dharmapuri",
            "Dindigul",
            "Erode",
            "Kanchipuram",
            "Kanyakumari",
            "Karur",
            "Krishnagiri",
            "Madurai",
            "Nagapattinam",
            "Namakkal",
            "Nilgiris",
            "Perambalur",
            "Pudukkottai",
            "Ramanathapuram",
            "Salem",
            "Sivaganga",
            "Thanjavur",
            "Theni",
            "Tiruchirappalli",
            "Tirunelveli",
            "Tiruvallur",
            "Tiruvannamalai",
            "Tiruvarur",
            "Tuticorin",
            "Vellore",
            "Villupuram",
            "Virudhunagar"
        ],
        "TELANGANA": [
            "Adilabad",
            "Hyderabad",
            "K.V.Rangareddy",
            "Karim Nagar",
            "Khammam",
            "Mahabub Nagar",
            "Medak",
            "Nalgonda",
            "Nizamabad",
            "Warangal"
        ],
        "TRIPURA": [
            "Dhalai",
            "North Tripura",
            "South Tripura",
            "West Tripura"
        ],
        "UTTAR PRADESH": [
            "Agra",
            "Aligarh",
            "Allahabad",
            "Ambedkar Nagar",
            "Auraiya",
            "Azamgarh",
            "Bagpat",
            "Bahraich",
            "Ballia",
            "Balrampur",
            "Banda",
            "Barabanki",
            "Bareilly",
            "Basti",
            "Bijnor",
            "Budaun",
            "Bulandshahr",
            "Chandauli",
            "Chitrakoot",
            "Deoria",
            "Etah",
            "Etawah",
            "Faizabad",
            "Farrukhabad",
            "Fatehpur",
            "Firozabad",
            "Gautam Buddha Nagar",
            "Ghaziabad",
            "Ghazipur",
            "Gonda",
            "Gorakhpur",
            "Hamirpur",
            "Hardoi",
            "Hathras",
            "Jalaun",
            "Jaunpur",
            "Jhansi",
            "Jyotiba Phule Nagar",
            "Kannauj",
            "Kanpur Dehat",
            "Kanpur Nagar",
            "Kaushambi",
            "Kheri",
            "Kushinagar",
            "Lalitpur",
            "Lucknow",
            "Maharajganj",
            "Mahoba",
            "Mainpuri",
            "Mathura",
            "Mau",
            "Meerut",
            "Mirzapur",
            "Moradabad",
            "Muzaffarnagar",
            "Pilibhit",
            "Pratapgarh",
            "Raebareli",
            "Rampur",
            "Saharanpur",
            "Sant Kabir Nagar",
            "Sant Ravidas Nagar",
            "Shahjahanpur",
            "Shrawasti",
            "Siddharthnagar",
            "Sitapur",
            "Sonbhadra",
            "Sultanpur",
            "Unnao",
            "Varanasi"
        ],
        "UTTARAKHAND": [
            "Almora",
            "Bageshwar",
            "Chamoli",
            "Champawat",
            "Dehradun",
            "Haridwar",
            "Nainital",
            "Pauri Garhwal",
            "Pithoragarh",
            "Rudraprayag",
            "Tehri Garhwal",
            "Udham Singh Nagar",
            "Uttarkashi"
        ],
        "WEST BENGAL": [
            "Bankura",
            "Bardhaman",
            "Birbhum",
            "Cooch Behar",
            "Darjiling",
            "East Midnapore",
            "Hooghly",
            "Howrah",
            "Jalpaiguri",
            "Kolkata",
            "Malda",
            "Medinipur",
            "Murshidabad",
            "Nadia",
            "North 24 Parganas",
            "North Dinajpur",
            "Puruliya",
            "South 24 Parganas",
            "South Dinajpur",
            "West Midnapore"
        ]
        }
cookies = {
    'feedify_trackvisit': '1615370390488.',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'X-Requested-With': 'XMLHttpRequest',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Referer': 'https://www.indiatvnews.com/pincode/maharashtra/buldhana/aland/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers',
}
def getAlllinks():
    output = []

    for i in data:
        print("-----------------")
        print()
        m = i.lower().replace(" ","-").replace('&','and')
        for j in data[i]:
            n = j.lower().replace(" ","-").replace('&','and')
            # https://www.indiatvnews.com/pincode/ajaxpostofficeload/west-bengal/north-dinajpur/
            
            # print(f'https://www.indiatvnews.com/pincode/ajaxpostofficeload/{m}/{n}/')
            res = requests.get(f'https://www.indiatvnews.com/pincode/ajaxpostofficeload/{m}/{n}/', headers=headers, cookies=cookies)
            if res.status_code != 200:
                print(m,n)
            elif(res.status_code == 200):
                for i in res.json():
                    output.append(f"https://www.indiatvnews.com/pincode/{m}/{n}/{ i['url']}/")
                    # print(  m , n  ,  i["url"])
                    print(output)
            else:
                print("error")
        # print(res.json())
    return output
    

# south-24-parganas
# south-24-parganas
# getAlllinks()