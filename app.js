allStste = document.querySelectorAll('//*[@id="state"]/div/select/option');

[
    "",
    "ANDAMAN_AND_NICOBAR_ISLANDS",
    "ANDHRA_PRADESH",
    "ARUNACHAL_PRADESH",
    "ASSAM",
    "BIHAR",
    "CHANDIGARH",
    "CHHATTISGARH",
    "DADRA_AND_NAGAR_HAVELI",
    "DAMAN_AND_DIU",
    "DELHI",
    "GOA",
    "GUJARAT",
    "HARYANA",
    "HIMACHAL_PRADESH",
    "JAMMU_AND_KASHMIR",
    "JHARKHAND",
    "KARNATAKA",
    "KERALA",
    "LAKSHADWEEP",
    "MADHYA_PRADESH",
    "MAHARASHTRA",
    "MANIPUR",
    "MEGHALAYA",
    "MIZORAM",
    "NAGALAND",
    "ORISSA",
    "PONDICHERRY",
    "PUNJAB",
    "RAJASTHAN",
    "SIKKIM",
    "TAMIL_NADU",
    "TELANGANA",
    "TRIPURA",
    "UTTAR_PRADESH",
    "UTTARAKHAND",
    "WEST_BENGAL"
]

allStste = document.querySelectorAll('#state > div> select > option');
var lst = []
for(var i = 0;i<allStste.length;i++){
    console.log(allStste[i].value);
    lst.push(allStste[i].value);
}

console.log(lst);


["andaman-and-nicobar-islands", "andhra-pradesh", "arunachal-pradesh", "assam", "bihar", "chandigarh", "chattisgarh", "daman-and-diu", "delhi", "goa", "gujarat", "himachal-pradesh", "jammu-and-kashmir", "jharkhand", "karnataka", "kerala", "lakshadweep", "madhya-pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha", "pondicherry", "punjab", "rajasthan", "sikkim", "tamil-nadu", "telangana", "telangana", "tripura", "uttar-pradesh", "uttarakhand", "west-bengal"]